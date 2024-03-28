import React, { useEffect, useState } from 'react';
import { loadTweets } from '../lookup';


  
  export function TweetLists(props) {
    const [tweets, setTweets] = useState([])
    
    useEffect(() => {
      const myCallback = (response, status) => {
        if (status === 200) {
          setTweets(response) 
        }
        else {
          alert('There was an error with this')
        }
      }
      loadTweets(myCallback)
    }, [])
    return tweets.map((item, index) => {
      return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`} />
    })
  }

export function ActionBtn(props) {
  const { tweet, action } = props;
  const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
  const [userLike,setUserLike]=useState(tweet.userLike === true?true:false)
  const className = props.className ? props.className : 'btn btn-primary btn-sm';
  const actionDisplay = action.display ? action.display : 'action'
  const display = action.display === "like" ? `${likes} ${actionDisplay}` : actionDisplay;
  const handleClick = (event) => {
    if (action.type === 'like') {
      if (userLike === true) {
        setUserLike(false) 
        setLikes(likes-1)
      }
      else {
        setUserLike(true) 
        setLikes(likes+1)
      }
    }    
  }  
    return <button className={className} onClick={handleClick}>{ display}</button>
  }
  
  
 export function Tweet(props) {
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
      <p>
        {tweet.id} - {tweet.content}
      </p>
      <div className='btn btn-group'>
        <ActionBtn tweet={tweet} action={{ type: "like",display:"like" }} />
        <ActionBtn tweet={tweet} action={{ type: "unlike", display: "unlike" }} />
        <ActionBtn tweet={tweet} action={{ type: "retweet",display:"retweet" }} />
        
        </div>
    </div>
  }