import React, { useEffect, useState } from 'react';
import { apiTweetCreate,apiTweetList } from './lookup';


export function TweetComponent(props) {
  const textAreaRef = React.createRef();
  const [newTweets, setNewTweets] = useState([]);
  const handleSubmit = (event) => {
    event.preventDefault();
    const newVal = textAreaRef.current.value;


    const handleBackendUpdate = (response, status) => {
      let tempNewTweets = [...newTweets];
      if (status === 201) {
        tempNewTweets.unshift(response); 
        setNewTweets(tempNewTweets);
      }
      else {
        console.log(response,status)
        alert('An error ocurred,please try again!');
      }
    }

    apiTweetCreate(newVal,handleBackendUpdate);
    textAreaRef.current.value = '';
  }
  return <div className={props.className}>
    <div className='col-12 mb-3'>
      <form onSubmit={handleSubmit}>
        <textarea ref={textAreaRef} required={true} name='tweet' className='form-control'></textarea>
        <button type='submit' className='btn btn-primary my-3'>Tweet</button>
      </form>
    </div>
    <TweetLists newTweets={newTweets} />
  </div>;
};

  
  export function TweetLists(props) {
    const [tweetsInit, setTweetsInit] = useState([]);
    const [tweets, setTweets] = useState([]);
    const [tweetDidSet, setTweetDidSet] = useState(false);
    useEffect(() => {
      let final = [...props.newTweets].concat(tweetsInit);
      if (final.length !== tweets.length) {
        setTweets(final);
      };
    }, [tweetsInit, props.newTweets, tweets]);
    
    useEffect(() => {
      if (tweetDidSet === false) {
        const handleTweetListLookup = (response, status) => {
          if (status === 200) {
            setTweetsInit(response);
            setTweetDidSet(true);
          }
          else {
            alert('There was an error with this');
          }
        };
        apiTweetList(handleTweetListLookup);
      };
    }, [setTweetsInit, tweetDidSet, setTweetDidSet]);
    return tweets.map((item, index) => {
      return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`} />;
    });
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