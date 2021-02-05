import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

// Component imports
import Navbar from './components/Navbar';
import Home from './components/screens/Home';
import About from './components/screens/About';
import Feed from './components/screens/Feed';
import Login from './components/screens/Login';
import Register from './components/screens/Register';

const App = () => {
  return (
    <>
      <Router>
        <Navbar />
        <div>
          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route exact path="/about">
              <About />
            </Route>
            <Route exact path="/feed">
              <Feed />
            </Route>
            <Route exact path="/login">
              <Login />
            </Route>
            <Route exact path="/register">
              <Register />
            </Route>
          </Switch>
        </div>
      </Router>
    </>
  );
};

export default App;
