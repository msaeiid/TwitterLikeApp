import React, { useState,useEffect } from 'react';
import { TweetLists } from './lists';
import { TweetCreate } from './create';
import { apiTweetDetail } from './lookup';
import { Tweet } from './detail';
import { FeedList } from './feed';

export function TweetComponent(props) {
  const [newTweets, setNewTweets] = useState([]);
  const canTweet = props.canTweet === "false" ? false : true;
  const handleNewTweet = (newTweets) => {
    let tempNewTweets = [...newTweets];
    tempNewTweets.unshift(newTweets);
    setNewTweets(tempNewTweets);
  }
  return <div div className={props.className} >
    {canTweet === true && <TweetCreate didTweet={handleNewTweet} className='col-12 mb-3' />}
    <TweetLists newTweets={newTweets} {...props} />
  </div>
}


export function FeedComponent(props) {
  //const [newTweets, setNewTweets] = useState([]);
  const canTweet = props.canTweet === "false" ? false : true;
  const handleNewTweet = (newTweets) => {
    //let tempNewTweets = [...newTweets];
    console.log('here there');
    //tempNewTweets.unshift(newTweets);
    //setNewTweets(tempNewTweets);
  }
  return <div div className={props.className} >
    {canTweet === true && <TweetCreate didTweet={handleNewTweet} className='col-12 mb-3' />}
    <FeedList {...props} />
  </div>
}



export function TweetDetailComponent(props) {
  const { tweetId } = props;
  const [didLookup, setDidLookup] = useState(false);
  const [tweet, setTweet] = useState(null);

  const handleBackendLookup = (response, status) => {
    if (status === 200) {
      setTweet(response);
    }
    else {
      alert("There was an error finding your tweet.")
    }
    
  }

  useEffect(() => {
    if (didLookup === false) {
      apiTweetDetail(tweetId,handleBackendLookup);
      setDidLookup(true);
    }
    
  }, [didLookup, setDidLookup, tweetId]);
  
  return tweet === null ?
    null :
    <Tweet tweet={tweet} className={props.className} />;
}