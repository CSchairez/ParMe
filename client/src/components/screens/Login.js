import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

import { login } from '../../actions/userActions';

const Login = ({ location, history }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const dispatch = useDispatch();

  // get the userLogin state (this specifically points to the userlogin reducer so we can fire actions off into this)
  const userLogin = useSelector((state) => state.userLogin);
  const { loading, error, userInfo } = userLogin;
  const redirect = location.search ? location.search.split('=')[1] : '/feed';

  // If we are already logged in (the user would exist in the userLogin state in our store), redirect
  useEffect(() => {
    if (userInfo) {
      history.push(redirect);
    }
  }, [history, redirect, userInfo]);

  const onHandleSubmit = (e) => {
    e.preventDefault();
    // dispath the login action here
    dispatch(login(email, password)); // dispatch the login action to the store
  };

  const onHandleChange = (e) => {
    switch (e.target.name) {
      case 'email':
        setEmail(e.target.value);
        break;
      case 'password':
        setPassword(e.target.value);
        break;
      default:
        break;
    }
  };

  return (
    <div className="login">
      <main className="bg-white max-w-lg mx-auto p-8 md:p-12 my-20 rounded-lg shadow-2xl">
        <section>
          <h3 className="font-bold text-2xl">Login</h3>
        </section>

        <section className="mt-10">
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
            <div className="flex justify-end">
              <Link
                to="/update_password"
                className="text-sm text-green-600 hover:text-green-700 hover:underline mb-6"
              >
                Forgot your password?
              </Link>
            </div>
            <button
              className="bg-green-600 hover:bg-green-500 text-white font-bold py-2 rounded shadow-lg hover:shadow-xl transition duration-200"
              type="submit"
              onSubmit={onHandleSubmit}
            >
              Sign In
            </button>
          </form>
        </section>
      </main>

      <div className="max-w-lg mx-auto text-center mt-12 mb-6">
        <p className="text-green-600">
          Don't have an account?{' '}
          <Link to="/register" className="font-bold hover:underline">
            Sign up
          </Link>
          .
        </p>
      </div>
    </div>
  );
};

export default Login;
