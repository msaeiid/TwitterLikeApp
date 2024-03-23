const tweetContainerElement = document.getElementById('tweets')
const tweetCreateFormEl = document.getElementById('tweet-create-form')
tweetCreateFormEl.addEventListener('submit', handleTweetCreateFormDidSubmit)

function handleTweetFormError(msg, display) {
    var errorDiv = document.getElementById("tweet-create-form-error")
    if (display === true) {
        errorDiv.setAttribute("class", "alert alert-danger")
        errorDiv.innerText = msg
    }
    else {
        errorDiv.setAttribute("d-none class", "alert alert-danger")
    }
}

function handleTweetCreateFormDidSubmit(event) {
    event.preventDefault()
    const myForm = event.target
    const myFormData = new FormData(myForm)
    const endpoint = myForm.getAttribute('action')
    const method = myForm.getAttribute('method')
    const responseType = "json"
    const xhr = new XMLHttpRequest()
    xhr.responseType = responseType
    xhr.open(method, endpoint)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function () {
        if (xhr.status === 201) {
            handleTweetFormError("", false)
            const newTweetJson = xhr.response
            console.log(newTweetJson.likes)
            const ogHtml = tweetContainerElement.innerHTML
            const newTweetElement = formatTweetElement(newTweetJson)
            tweetContainerElement.innerHTML = newTweetElement + ogHtml
            myForm.reset()
        }
        else if (xhr.status === 400) {
            const errorJson = xhr.response
        const contentError = errorJson.content
        let contentErrorMsg;
        if (contentError) {
            contentErrorMsg = contentError[0]
            if (contentErrorMsg) {
                handleTweetFormError(contentErrorMsg, true)
            }
            else {
                alert('An error occurred, Please try again later.')
            }
        }
    }
    else if (xhr.status === 400) {
        const errorJson = xhr.response
        alert(errorJson)
    }
}
xhr.onerror(function () {
    alert('An error occurred, Please try again later.')
})
xhr.send(myFormData)
loadTweets(tweetsEl)

}
function handleDidLike(id, numberOfLikes) {
    console.log(id, numberOfLikes)
}

function likeBtn(tweet) {
    return `<button class='btn btn-primary' onclick=handleDidLike(${tweet.id},${tweet.likes})>${tweet.likes} Likes</button>`

}

function formatTweetElement(tweet) {
    var formattedTweet = `<div class='col-12 col-md-10 col-auto border rounded mb-4 py-4' id=tweet-${tweet.id}>
<p>${tweet.content}</p>
<div class='btn-group'>${likeBtn(tweet)}</div>
</div>`
    return formattedTweet
}

function loadTweets(tweetsElements) {
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    const url = '/tweet/list/'
    const responseType = 'json'

xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = function () {
    const serverResponse = xhr.response
    const listedItems = serverResponse.response
    var finalTweetStr = ""
    var i;
    for (i = 0; i < listedItems.length; i++) {
        var tweetObj = listedItems[i]
        var currentItem = formatTweetElement(tweetObj)
        finalTweetStr += currentItem
    }
    tweetsElements.innerHTML = finalTweetStr

    }
    xhr.send()
}
loadTweets(tweetContainerElement)