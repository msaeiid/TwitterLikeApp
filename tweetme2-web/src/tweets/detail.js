import React, { useState } from 'react';
import { ActionBtn } from './buttons';

export function ParentTweet(props) {
    const { tweet } = props
    return tweet.parent ?
      <div className='row'>
        <div className='col-11 mx-auto p-3 border rounded'>
          <p className='mb-0 text-muted small'>Retweet</p>
          <Tweet hideAction className={''} tweet={tweet.parent} />
      </div>
      </div> :
      null
}
export function Tweet(props) {
  const { tweet, didRetweet, hideAction } = props;
  const [actionTweet, setActionTweet] = useState(props.tweet ? props.tweet : null);
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6';

  var path = window.location.pathname;
  var match = path.match(/(?<tweetid>\d+)/);
  var urlTweetId = match ? match.groups.tweetid : -1;
  const isDetail = `${tweet.id}`===`${urlTweetId}`;
  const handleLink = (event) => {
    event.preventDefault();
    window.location.href = `${tweet.id}/`
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
    <p>
      {tweet.id} - {tweet.content}
    </p>
    <ParentTweet tweet={tweet} />
    <div className='btn btn-group'>
      {(actionTweet && hideAction !== true) && <React.Fragment>
        <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "like", display: "like" }} />
        <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "unlike", display: "unlike" }} />
        <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} action={{ type: "retweet", display: "retweet" }} />
      </React.Fragment>
      }
      {isDetail ===true ? null: <button className='btn btn-outline-primary' onClick={handleLink}>View</button>}
    </div>
  </div>
}