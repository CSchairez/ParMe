import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

// Import our Actions + Action types
import { getUserDetails, updateUserProfile } from '../../actions/userActions';
import { USER_UPDATE_PROFILE_RESET } from '../../reducers/actionTypes';

const Profile = ({ history, location }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [message, setMessage] = useState(null);

  const dispatch = useDispatch();

  // Get users information in state
  const userDetails = useSelector((state) => state.userDetails);
  const { loading, error, user } = userDetails;

  // Checking if the user is authenticated
  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  // To update user profile
  const userUpdateProfile = useSelector((state) => state.userUpdateProfile);
  const { success } = userUpdateProfile;

  // If user is not logged in, kick them off this page immediately (which is why it is in useEffffect)
  useEffect(() => {
    // if userinfo state is empty (user is not logged in and stored in state), redirect
    if (!userInfo) {
      history.push('/login');
    } else {
      if (!user || !user.name || success) {
        dispatch(getUserDetails(userInfo._id));
      } else {
        setName(userInfo.name);
        setEmail(userInfo.email);
      }
    }
  }, [
    dispatch,
    history,
    success,
    user,
    userInfo.email,
    userInfo.name,
    userInfo,
  ]);

  const submitHandler = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setMessage('Passwords do not match');
    } else {
      dispatch(updateUserProfile({ id: user._id, name, email, password }));
    }
  };

  const onHandleChange = (e) => {
    // determine if this was the email or password field being updated
    switch (e.target.type) {
      case 'email':
        setEmail(e.target.value);
        break;
      case 'password':
        setPassword(e.target.value);
        break;
      case 'text':
        setName(e.target.value);
        break;
      default:
        break;
    }
  };

  return <div>Profile</div>;
};

export default Profile;
