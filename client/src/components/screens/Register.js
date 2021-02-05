import React from 'react';
import { Link } from 'react-router-dom';

const Register = () => {
  return (
    <div className="login">
      <main className="bg-white max-w-lg mx-auto p-8 md:p-12 my-20 rounded-lg shadow-2xl">
        <section>
          <h3 className="font-bold text-2xl">Register</h3>
        </section>

        <section className="mt-10">
          <form className="flex flex-col">
            <div className="mb-6 pt-3 rounded">
              <label
                className="block text-gray-700 text-sm font-bold mb-2 ml-3"
                for="Name"
              >
                Name
              </label>
              <input
                type="text"
                id="name"
                className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
              />
            </div>
            <div className="mb-6 pt-3 rounded">
              <label
                className="block text-gray-700 text-sm font-bold mb-2 ml-3"
                for="email"
              >
                Email
              </label>
              <input
                type="text"
                id="email"
                className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
              />
            </div>
            <div className="mb-6 pt-3 rounded">
              <label
                className="block text-gray-700 text-sm font-bold mb-2 ml-3"
                for="password"
              >
                Password
              </label>
              <input
                type="password"
                id="password"
                className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
              />
            </div>
            <button
              className="bg-green-600 my-3 hover:bg-green-500 text-white font-bold py-2 rounded shadow-lg hover:shadow-xl transition duration-200"
              type="submit"
            >
              Register
            </button>
          </form>
        </section>
      </main>

      <div className="max-w-lg mx-auto text-center mt-12 mb-6">
        <p className="text-green-600">
          Already have an account?{' '}
          <Link to="/login" className="font-bold hover:underline">
            Sign in
          </Link>
          .
        </p>
      </div>
    </div>
  );
};

export default Register;