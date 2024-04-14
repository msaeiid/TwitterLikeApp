import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { ProfileBadgeComponent } from './profiles';
import {
  TweetComponent,
  TweetDetailComponent,
  FeedComponent,
} from './tweets';

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
  const root = ReactDOM.createRoot(tweetEl);
  root.render(e(TweetComponent, tweetEl.dataset)); 
}


const tweetFeedEl=document.getElementById('tweetme2-feed')
if (tweetFeedEl) {  
  const root = ReactDOM.createRoot(tweetFeedEl);
  root.render(e(FeedComponent, tweetFeedEl.dataset)); 
}


const tweetDetailElements = document.getElementById("tweetme-2-detail");
if (tweetDetailElements) {
  const root = ReactDOM.createRoot(tweetDetailElements);
  root.render(e(TweetDetailComponent, tweetDetailElements.dataset)); 
}


const userProfileBadgeElements = document.getElementById("tweetme-2-profile-badge");
if (userProfileBadgeElements) {
  const root = ReactDOM.createRoot(userProfileBadgeElements);
  root.render(e(ProfileBadgeComponent, userProfileBadgeElements.dataset)); 
}




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
