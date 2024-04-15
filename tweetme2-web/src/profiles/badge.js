import React, { useState, useEffect } from 'react';
import {
  apiProfileDetail,
  apiProfileFollowToggle
} from './lookup';

import {
  UserDisplay,
  UserPicture
} from './components';

import { DisplayCount } from './utils';

function ProfileBadge(props) {
  const { user, didFollowToggle, profileLoading } = props;
  let currentVerb = (user && user.is_following) ? "Unfollow" : "Follow";
  currentVerb = profileLoading ? "Loading..." : currentVerb;
  const handleFollowToggle = (event) => {
    event.preventDefault();
    if (didFollowToggle && ! profileLoading) {
      didFollowToggle(currentVerb);
    }
  }
  return user ? <div className='mx-2 my-2'>
    <UserPicture author={user} hideLink></UserPicture>
    <p>
      <DisplayCount>{ user.follower_count}</DisplayCount> {user.follower_count === 1 || user.follower_count === 0 ? "Follower":"Followers"}
    </p>
    <p>
    <DisplayCount>{ user.following_count}</DisplayCount> Following
    </p>
    <p>
      {user.location}
    </p>
    <p>
      {user.bio}
    </p>
    <p><UserDisplay author={user} includeFullName hideLink /></p>
    <button className='btn btn-primary' onClick={handleFollowToggle}>{currentVerb}</button>
  </div> : null
}


export function ProfileBadgeComponent(props) {
  const { username } = props;
  const [didLookup, setDidLookup] = useState(false);
  const [profile, setProfile] = useState(null);
  const [profileLoading, setProfileLoading] = useState(false);
  const handleBackendLookup = (response, status) => {
    if (status === 200) {
      setProfile(response);
    }
  }
  useEffect(() => {
    if (didLookup === false) {
      apiProfileDetail(username,handleBackendLookup);
      setDidLookup(true);
    }
    
  }, [didLookup, setDidLookup, username]);
  const handleNewFollow = (actionVerb) => {
    apiProfileFollowToggle(username, actionVerb, (response, status) => {
      if (status === 200) {
        setProfile(response);
      }
      setProfileLoading(false);
    })
    setProfileLoading(true);
  }  

  return didLookup === false ? "Loading ..." : profile ? <ProfileBadge user={profile} didFollowToggle={handleNewFollow} profileLoading={profileLoading} /> : null
}