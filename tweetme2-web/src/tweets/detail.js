import React, { useState } from 'react';
import { ActionBtn } from './buttons';
import {
  UserDisplay,
  UserPicture
} from '../profiles';

export function ParentTweet(props) {
  const { tweet } = props;
  return tweet.parent ? <Tweet isRetweet reTweeter={props.reTweeter} hideAction className={''} tweet={tweet.parent} /> : null;
}
export function Tweet(props) {
  const { tweet, didRetweet, hideAction, isRetweet, reTweeter } = props;
  const [actionTweet, setActionTweet] = useState(props.tweet ? props.tweet : null);
  let className = props.className ? props.className : 'col-10 mx-auto col-md-6';
  className = isRetweet === true ? `${className} p-2 border rounded` : className;
  var path = window.location.pathname;
  var match = path.match(/(?<tweetid>\d+)/);
  var urlTweetId = match ? match.groups.tweetid : -1;
  const isDetail = `${tweet.id}`===`${urlTweetId}`;
  const handleLink = (event) => {
    event.preventDefault();
    window.location.href = `/${tweet.id}`
  }
  const handlePerformAction = (newActionTweet, status) => {
    if (status === 200) {
      setActionTweet(newActionTweet);
    }
    else if (status === 201) {
      if (didRetweet) {
        didRetweet(newActionTweet);
      }
    }
  }
  return <div className={className}>
    {isRetweet === true && <div className='mb-2'>
      <span className='small text-muted'>Retweet via <UserDisplay author={reTweeter} /></span>
    </div>}
    <div className='d-flex'>
      <div className=''>
        <UserPicture author={tweet.author} />
      </div>
      <div className='col-11'>
        <div>
          <p>
            <UserDisplay author={tweet.author} includeFullName />
          </p>
          <p>
            {tweet.content}
          </p>
          <ParentTweet tweet={tweet} reTweeter={tweet.author} />
          <div className='btn btn-group px-0'>
            {(actionTweet && hideAction !== true) && <React.Fragment>
              <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "like", display: "like" }} />
              <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "unlike", display: "unlike" }} />
              <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "retweet", display: "retweet" }} />
            </React.Fragment>
        }
        {isDetail ===true ? null: <button className='btn btn-outline-primary' onClick={handleLink}>View</button>}
        </div>
      
      </div>
      </div>
      </div>
  </div>
}