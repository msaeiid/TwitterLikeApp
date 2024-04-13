import React, { useEffect, useState } from 'react';
import { apiTweetFeed } from './lookup';
import { Tweet } from './detail';

export function FeedList(props) {
  const [tweetsInit, setTweetsInit] = useState([]);
  const [tweets, setTweets] = useState([]);
  const [nextUrl, setNextUrl] = useState(null);
  const [tweetDidSet, setTweetDidSet] = useState(false);
  useEffect(() => {
    let final = tweetsInit;
    if (final.length !== tweets.length) {
      setTweets(final);
    };
  }, [tweetsInit, props.newTweets, tweets]);
  useEffect(() => {
    if (tweetDidSet === false) {
      const handleTweetListLookup = (response, status) => {
        if (status === 200) {
          setNextUrl(response.next)
          setTweetsInit(response.results);
          setTweetDidSet(true);
        }
      };
      apiTweetFeed(handleTweetListLookup);
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
  const handleLoadNext=(event) => {
    event.preventDefault();
    if (nextUrl !== null) {
      const handleLoadNextResponse = (response, status) => {
        if (status === 200) {
          setNextUrl(response.next)
          const newTweets = [...tweets].concat(response.results);
          setTweetsInit(newTweets);
          setTweets(newTweets);
        }      
      }

      apiTweetFeed(handleLoadNextResponse, nextUrl);
    }
  }
  return <React.Fragment> {tweets.map((item, index) => {
    return <Tweet tweet={item}
      didRetweet={handleDidRetweet}
      className='my-5 py-5 border bg-white text-dark'
      key={`${index}-{item.id}`} />
  })}
    {nextUrl  !==null && <button onClick={handleLoadNext} className='btn btn-outline-primary'>Next Page</button>}
    </React.Fragment>

}