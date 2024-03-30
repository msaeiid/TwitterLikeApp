
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}



function lookup(method, endpoint, callback, data) {
  let jsonData;
  if (data) {
    jsonData = JSON.stringify(data);
  }
  const url = `http://127.0.0.1:8000/api/${endpoint}`;
  const xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader("content-type", "application/json");
  const csrftoken = getCookie('csrftoken');
  if (csrftoken) {
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest");
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);  
  }
  xhr.onload = function () {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = function () {
    callback({"message":"An error ocurred!"}, xhr.status);
  };
  xhr.send(jsonData);
}



export function createTweet(newTweet, callback) {
  lookup("POST", "tweet/create/", callback, { content: newTweet });
}


export function loadTweets(callback) {
  lookup("GET", "tweet/", callback);
}