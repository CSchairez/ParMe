import React from 'react';
import { Provider } from 'react-redux';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

// import our store which does all the combine reducers, init state, etc.
import store from './store';

// Wrap our app in our provider to provide store data
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.querySelector('#root'),
);
