import React, { useEffect, useState } from 'react';
import { apiTweetList } from './lookup';
import { Tweet } from './detail';

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
      apiTweetList(props.username, handleTweetListLookup);
    };
  }, [setTweetsInit, tweetDidSet, setTweetDidSet, props.username]);
  const handleDidRetweet = (newTweet) => {
    const updateTweetInit = [...tweetsInit];
    updateTweetInit.unshift(newTweet);
    setTweetsInit(updateTweetInit);
    const updateFinalTweets = [...tweets];
    updateFinalTweets.unshift(newTweet);//he make's a bug here
    setTweets(updateFinalTweets);
  }
  return tweets.map((item, index) => {
    return <Tweet tweet={item}
      didRetweet={handleDidRetweet}
      className='my-5 py-5 border bg-white text-dark'
      key={`${index}-{item.id}`} />
  });
}