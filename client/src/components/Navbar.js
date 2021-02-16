import React from 'react';
import { useDispatch, useSelector } from 'react-redux'; // to bring in state and to fire actions
import { Link } from 'react-router-dom';

// Actions imports
import { logout } from '../actions/userActions';

const Navbar = () => {
  const dispatch = useDispatch();

  const userLogin = useSelector((state) => state.userLogin); // bring in the userLogin state from out store

  const { userInfo } = userLogin; // pull the logged in users information out of the state we got above

  // Logout the user (removes the user info from state for auth related purposes)
  const logoutHandler = () => {
    dispatch(logout());
  };

  return (
    <nav className="flex items-center bg-green-600 p-5 flex-wrap">
      <ul className="top-nav w-full lg:inline-flex lg:flex-grow lg:w-auto">
        <li className="text-xl text-white font-bold tracking-wide p-2 mr-4">
          <Link to="/">ParMe</Link>
        </li>
        <div className="top-nav w-full lg:inline-flex lg:flex-grow lg:w-auto justify-end">
          <li className="text-sm text-white tracking-wide p-2 mr-4">
            <Link to="/">Home</Link>
          </li>
          <li className="text-sm text-white tracking-wide p-2 mr-4">
            <Link to="/feed">Feed</Link>
          </li>
          {userInfo ? (
            <>
              <li className="text-sm text-white tracking-wide p-2 mr-4">
                <Link to="/profile">{userInfo.name}</Link>
              </li>
              <li
                className="text-sm text-white tracking-wide p-2 mr-4"
                onClick={logoutHandler}
              >
                <Link to="/">Logout</Link>
              </li>
            </>
          ) : (
            <>
              <li className="text-sm text-white tracking-wide p-2 mr-4">
                <Link to="/about">About</Link>
              </li>{' '}
              <li className="text-sm text-white tracking-wide p-2 mr-4">
                <Link to="/login">Login</Link>
              </li>
              <li className="text-sm text-white tracking-wide p-2 mr-4">
                <Link to="/register">Sign Up</Link>
              </li>
            </>
          )}
        </div>
      </ul>
    </nav>
  );
};

export default Navbar;
