import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
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
            <Link to="/about">About</Link>
          </li>
          <li className="text-sm text-white tracking-wide p-2 mr-4">
            <Link to="/feed">Feed</Link>
          </li>
          <li className="text-sm text-white tracking-wide p-2 mr-4">
            <Link to="/login">Login</Link>
          </li>
          <li className="text-sm text-white tracking-wide p-2 mr-4">
            <Link to="/register">Sign Up</Link>
          </li>
        </div>
      </ul>
    </nav>
  );
};

export default Navbar;
