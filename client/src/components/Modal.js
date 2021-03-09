import React from 'react';

export default function Modal({ setShowModal }) {
  return null;

  // the below code is an outline to the tailwind classes being used. Will need to be worked off of
  // <>
  //   <div
  //     className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none"
  //     onClick={() => setShowModal(false)}
  //   >
  //     <div className="relative w-auto my-6 mx-auto max-w-3xl">
  //       {/*content*/}
  //       <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
  //         {/*header*/}
  //         <div className="flex items-start justify-between p-5 border-b border-solid border-gray-300 rounded-t">
  //           <h3 className="text-3xl font-semibold">Add Round</h3>
  //           <button
  //             className="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none"
  //             onClick={() => setShowModal(false)}
  //           >
  //             <span className="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
  //               ×
  //             </span>
  //           </button>
  //         </div>
  //         {/*body*/}
  //         <div className="relative p-6 flex-auto">
  //           <div className="my-4 text-gray-600 text-lg leading-relaxed">
  //             <label
  //               className="block text-gray-700 text-sm font-bold mb-2 ml-3"
  //               htmlFor="course"
  //             >
  //               Course
  //             </label>
  //             <input
  //               type="text"
  //               id="course"
  //               name="course"
  //               value={''}
  //               onChange={(e) => console.log(e)}
  //               className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
  //             />
  //             <label
  //               className="block text-gray-700 text-sm font-bold mb-2 ml-3"
  //               htmlFor="score"
  //             >
  //               Round Score
  //             </label>
  //             <input
  //               type="text"
  //               id="score"
  //               name="score"
  //               value={''}
  //               onChange={(e) => console.log(e)}
  //               className="rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-green-600 transition duration-500 px-3 pb-3"
  //             />
  //           </div>
  //         </div>
  //         {/*footer*/}
  //         <div className="flex items-center justify-end p-6 border-t border-solid border-gray-300 rounded-b">
  //           <button
  //             className="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1"
  //             type="button"
  //             style={{ transition: 'all .15s ease' }}
  //             onClick={() => setShowModal(false)}
  //           >
  //             Cancel
  //           </button>
  //           <button
  //             className="bg-green-500 text-white active:bg-green-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1"
  //             type="button"
  //             style={{ transition: 'all .15s ease' }}
  //             onClick={() => setShowModal(false)}
  //           >
  //             Confirm
  //           </button>
  //         </div>
  //       </div>
  //     </div>
  //   </div>
  //   <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
  // </>
}
