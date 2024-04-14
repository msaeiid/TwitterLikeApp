import React from 'react';

export function UserPicture(props) {
    const { author, hideLink } = props;
    const userIdSpan = <span className='mx-1 px-3 py-2 rounded-circle bg-dark text-white'>{author.username[0]}</span>
    return hideLink === true ?  userIdSpan  : <UserLink username={author.username}>{userIdSpan}</UserLink>;
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
    const { author, includeFullName,hideLink } = props;
    const nameDisplay = includeFullName === true ? `${author.first_name} ${author.last_name} ` : null;
    return <React.Fragment>
        {nameDisplay}
        {hideLink === true ? `@${author.username}` :<UserLink username={author.username}>@{author.username}</UserLink>}
    </React.Fragment>
}