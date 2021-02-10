import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const onHandleSubmit = (e) => {
    e.preventDefault();
    console.log(email, password);

    // dispath the login action here
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
      <main class="bg-white max-w-lg mx-auto p-8 md:p-12 my-20 rounded-lg shadow-2xl">
        <section>
          <h3 class="font-bold text-2xl">Login</h3>
        </section>

        <section class="mt-10">
          <form class="flex flex-col" onSubmit={onHandleSubmit}>
            <div class="mb-6 pt-3 rounded">
              <label
                class="block text-gray-700 text-sm font-bold mb-2 ml-3"
                for="email"
              >
                Email
              </label>
              <input
                type="text"
                id="email"
                name="email"
                value={email}
                onChange={onHandleChange}
                class="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
              />
            </div>
            <div class="mb-6 pt-3 rounded">
              <label
                class="block text-gray-700 text-sm font-bold mb-2 ml-3"
                for="password"
              >
                Password
              </label>
              <input
                type="password"
                id="password"
                name="password"
                value={password}
                onChange={onHandleChange}
                class="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
              />
            </div>
            <div class="flex justify-end">
              <Link
                to="/update_password"
                class="text-sm text-green-600 hover:text-green-700 hover:underline mb-6"
              >
                Forgot your password?
              </Link>
            </div>
            <button
              class="bg-green-600 hover:bg-green-500 text-white font-bold py-2 rounded shadow-lg hover:shadow-xl transition duration-200"
              type="submit"
              onSubmit={onHandleSubmit}
            >
              Sign In
            </button>
          </form>
        </section>
      </main>

      <div class="max-w-lg mx-auto text-center mt-12 mb-6">
        <p class="text-green-600">
          Don't have an account?{' '}
          <Link to="/register" class="font-bold hover:underline">
            Sign up
          </Link>
          .
        </p>
      </div>
    </div>
  );
};

export default Login;
