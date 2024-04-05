
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const SAFE_HTTP_METHODS = ['GET'];

export function lookup(method, endpoint, callback, data) {
  let jsonData;
  if (data) {
    jsonData = JSON.stringify(data);
  }
  const url = `http://127.0.0.1:8000/api/${endpoint}`;
  const xhr = new XMLHttpRequest();
  xhr.responseType = 'json';
  xhr.open(method, url);
  xhr.setRequestHeader("content-type", "application/json");
  if (!SAFE_HTTP_METHODS.includes(method)) {
    const csrftoken = getCookie('csrftoken');
    if (csrftoken) {
      //xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest");
      xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
      xhr.setRequestHeader("X-CSRFToken", csrftoken);  
    } 
  }
  xhr.onload = function () {
    if (xhr.status === 403) {
      const detail = xhr.response.detail;
      const error_message = "Authentication credentials were not provided.";
      if (detail === error_message || xhr.response === error_message) {
        window.location.href = '/login?showLoginRequired=true';
      }
    }
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = function () {
    callback({"message":"An error ocurred!"}, xhr.status);
  };
  xhr.send(jsonData);
}