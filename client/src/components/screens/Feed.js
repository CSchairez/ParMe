import React, { useState } from 'react';

const Feed = () => {
  const [showing, setIsShowing] = useState(false);

  window.onscroll = () => goToTop();

  const goToTop = (e) => {
    if (
      document.body.scrollTop > 20 ||
      document.documentElement.scrollTop > 20
    ) {
      setIsShowing(true);
    } else {
      setIsShowing(false);
    }
  };

  const dummyData = [
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img: 'img_url',
    },
    {
      location: 'Silver Creek',
      score: 94,
      img_url: 'img_url',
    },
  ];

  return (
    <>
      <div className="container 2xl mx-auto py-4 m-20">
        <h3 className="text-gray-700 text-5xl font-bold px-5 py-3 mb-10">
          Feed
        </h3>
        <section>
          {dummyData &&
            dummyData.map((data) => (
              <div className="round container mx-auto py-4 m-10">
                <h3>{data.location}</h3>
                <h5>{data.score}</h5>
                <p>{data.img_url}</p>
              </div>
            ))}
        </section>
      </div>
      <div
        className="add_round_2 shadow-2xl"
        style={showing ? { display: 'flex' } : { display: 'none' }}
        onClick={() => {
          document.body.scrollTop = 0;
          document.documentElement.scrollTop = 0;
        }}
      >
        <i className="fas fa-chevron-up adder_2"></i>
      </div>
      {/* Make top icon show up dynamically */}
      <div className="add_round shadow-2xl" onClick={(e) => alert('Add Round')}>
        <i className="fas fa-plus adder"></i>
      </div>
    </>
  );
};

export default Feed;
