import { lookup } from "../lookup";

export function apiProfileDetail(username, callback) {
    const endpoint = `profile/${username}`;
    lookup("GET", endpoint, callback);
  }  