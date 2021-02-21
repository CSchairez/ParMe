import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { Link } from 'react-router-dom';

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

  // Get users information in state - if it exists
  const userDetails = useSelector((state) => state.userDetails);
  const { loading, error, user } = userDetails;

  console.log(user);

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
        dispatch(getUserDetails());
      } else {
        setName(user.name);
        setEmail(user.email);
      }
    }
  }, []);

  const onHandleSubmit = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setMessage('Passwords do not match');
    } else {
      dispatch(updateUserProfile({ id: user._id, name, email, password }));
    }
  };

  const onHandleChange = (e) => {
    switch (e.target.name) {
      case 'email':
        setEmail(e.target.value);
        break;
      case 'password':
        setPassword(e.target.value);
        break;
      case 'password-confirm':
        setConfirmPassword(e.target.value);
        break;
      case 'text':
        setName(e.target.value);
        break;
      default:
        break;
    }
  };

  return (
    <div className="container 2xl mx-auto py-4 m-20">
      {name ? (
        <h1 className="text-gray-700 text-5xl font-bold px-5 py-3 mb-10">
          {name.split(' ')[0]}{' '}
          <span className="text-green-600">{name.split(' ')[1]}</span>
        </h1>
      ) : (
        <h1 className="text-green-600">Profile</h1>
      )}
      <section className="mt-15 max-w-lg">
        <form className="flex flex-col" onSubmit={onHandleSubmit}>
          <div className="mb-6 pt-3 rounded">
            <label
              className="block text-gray-700 text-sm font-bold mb-2 ml-3"
              htmlFor="email"
            >
              Email
            </label>
            <input
              type="text"
              id="email"
              name="email"
              value={email}
              onChange={onHandleChange}
              className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
            />
          </div>
          <div className="mb-6 pt-3 rounded">
            <label
              className="block text-gray-700 text-sm font-bold mb-2 ml-3"
              htmlFor="password"
            >
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={password}
              onChange={onHandleChange}
              className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
            />
          </div>
          <div className="mb-6 pt-3 rounded">
            <label
              className="block text-gray-700 text-sm font-bold mb-2 ml-3"
              htmlFor="password"
            >
              Confirm Password
            </label>
            <input
              type="password"
              id="password-confirm"
              name="password-confirm"
              value={confirmPassword}
              onChange={onHandleChange}
              className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
            />
          </div>
          <button
            className="bg-green-600 hover:bg-green-500 text-white font-bold py-2 rounded shadow-lg hover:shadow-xl transition duration-200"
            type="submit"
            onSubmit={onHandleSubmit}
          >
            Update Profile
          </button>
        </form>
      </section>
    </div>
  );
};

export default Profile;
