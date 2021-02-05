import React from 'react';

import Bullet from '../Bullet';
import Track from '../icons/Track';
import Visit from '../icons/Visit';
import Insights from '../icons/Insights';
import Comment from '../icons/Comment';
import Collaborate from '../icons/Collaborate';

const About = () => {
  return (
    <div className="container 2xl mx-auto py-10 m-20">
      <h1 className="text-gray-700 text-5xl font-bold px-5 py-3 mb-10">
        About <span className="text-green-600">ParMe</span>
      </h1>
      <div className="container px-5 py-5 flex flex-col">
        <div className="container rounded-lg shadow-2xl mb-20 w-100 h-48 px-10 flex flex-row-reverse justify-evenly items-center">
          <p className="px-2">
            ParMe helps you track all the games and rounds of golf that you play
          </p>
          <Track />
        </div>
        <div className="container rounded-lg shadow-2xl mb-20 w-100 h-48 px-10  flex mt-5 justify-evenly items-center">
          <p className="px-3">
            Show the world your scores and the courses you visit!
          </p>
          <Visit />
        </div>
        <div className="container rounded-lg shadow-2xl mb-20 w-100 h-48 px-10  flex mt-5 flex-row-reverse justify-evenly items-center">
          <p className="px-3">
            Key insights into your performance at your fingertips
          </p>
          <Insights />
        </div>
        <div className="container rounded-lg shadow-2xl mb-20 w-100 h-48 px-10  flex mt-5 justify-evenly items-center">
          <p className="px-3">
            Want to comment on someones game or post about their trip? You can!
          </p>
          <Comment />
        </div>
        <div className="container rounded-lg shadow-2xl w-100 h-48 px-10  flex mt-5 flex-row-reverse justify-evenly items-center">
          <p className="px-3">
            Collaborative sessions with friends coming soon!
          </p>
          <Collaborate />
        </div>
      </div>
    </div>
  );
};

export default About;
