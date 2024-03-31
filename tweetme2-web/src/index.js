import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {TweetComponent}  from './tweets'

const appEl=document.getElementById('root')
if (appEl) {
  const root = ReactDOM.createRoot(appEl);
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  ); 
}
const e = React.createElement;

const tweetEl=document.getElementById('tweetme2')
if (tweetEl) {
  //console.log(tweetEl.dataset)
  const root = ReactDOM.createRoot(tweetEl);
  root.render(e(TweetComponent, tweetEl.dataset),tweetEl); 
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
