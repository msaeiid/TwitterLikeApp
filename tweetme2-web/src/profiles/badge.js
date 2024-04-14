import { useState, useEffect } from 'react';
import { apiProfileDetail } from './lookup';
export function ProfileBadgeComponent(props) {
    const { username } = props;

    const [didLookup, setDidLookup] = useState(false);
    const [profile, setProfile] = useState(null);
  
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

  return didLookup === false ? "Loading ..." : profile ? <span>{profile.first_name}</span> : null
}