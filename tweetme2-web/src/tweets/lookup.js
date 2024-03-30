import { lookup } from '../lookup'

export function apiTweetCreate(newTweet, callback) {
    lookup("POST", "tweet/create/", callback, { content: newTweet });
  }
  
  
  export function apiTweetList(callback) {
    lookup("GET", "tweet/", callback);
  }