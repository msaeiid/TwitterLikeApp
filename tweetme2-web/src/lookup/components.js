
export function lookup(method, endpoint, callback, data) {
  let jsonData;
  if (data) {
    jsonData = JSON.stringify(data);
  }
  const url = `http://127.0.0.1:8000/api/${endpoint}`;
  const xhr = new XMLHttpRequest();
  xhr.responseType = "json";
  xhr.open(method, url);
  xhr.onload = function () {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = function () {
    callback({"message":"An error ocurred!"}, xhr.status);
  };
  xhr.send(jsonData);
};


export function loadTweets(callback) {
  lookup("GET","tweet/",callback)
  }