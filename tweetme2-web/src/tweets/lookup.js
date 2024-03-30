import { lookup } from '../lookup';

export function apiTweetCreate(newTweet, callback) {
    lookup("POST", "tweet/create/", callback, { content: newTweet });
  }
  
  
  export function apiTweetList(callback) {
    lookup("GET", "tweet/", callback);
}
  
export function apiTweetAction(tweet_id, action, callback) {
  const data = { id: tweet_id, action: action };
  lookup("POST", "tweet/action/", callback,data);
}