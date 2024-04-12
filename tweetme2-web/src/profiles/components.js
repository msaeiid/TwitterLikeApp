import React from 'react';

export function UserPicture(props) {
    const { author } = props;
    return <UserLink username={author.username}><span className='mx-1 px-3 py-2 rounded-circle bg-dark text-white'>
      {author.username[0]}
    </span></UserLink>
}
  
export function UserLink(props) {
    const { username } = props;
    const handleUserLink = (event) => {
        event.preventDefault();
        window.location.href = `/profile/${username}`;
    }
    return <span className='pointer' onClick={handleUserLink}>
        {props.children}
    </span>
}
  
export function UserDisplay(props) {
    const { author, includeFullName } = props;
    const nameDisplay = includeFullName === true ? `${author.first_name} ${author.last_name} ` : null;
    return <React.Fragment>
      {nameDisplay}
        <UserLink username={author.username}>@{author.username}</UserLink>
    </React.Fragment>
}