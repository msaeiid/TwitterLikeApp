import React, { useState } from 'react';
import { TweetLists } from './lists';
import { TweetCreate } from './create';

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