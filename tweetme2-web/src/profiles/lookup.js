import { lookup } from "../lookup";

export function apiProfileDetail(username, callback) {
    const endpoint = `profile/${username}`;
    lookup("GET", endpoint, callback);
}  
  


export function apiProfileFollowToggle(username, action, callback) {
  const data = { action: `${action && action}`.toLowerCase() };
  const endpoint = `profile/${username}/follow/`;
  lookup("POST", endpoint, callback, data);
}  