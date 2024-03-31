import { lookup } from '../lookup';

export function apiTweetCreate(newTweet, callback) {
    lookup("POST", "tweet/create/", callback, { content: newTweet });
}
  

export function apiTweetDetail(tweet_id, callback) {
  const endpoint = `tweet/${tweet_id}`;
  lookup("GET", endpoint, callback);
}
  
  
export function apiTweetList(username, callback) {
  let endpoint = "tweet/";
  if (username) {
    endpoint = `tweet/?username=${username}`;
  }
  lookup("GET", endpoint, callback);
}
  
export function apiTweetAction(tweet_id, action, callback) {
  const data = { id: tweet_id, action: action };
  lookup("POST", "tweet/action/", callback,data);
}