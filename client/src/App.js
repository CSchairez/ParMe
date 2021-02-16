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
            <Route exact path="/" component={Home} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
            <Route path="/about" component={About} />
            <Route path="/feed" component={Feed} />
          </Switch>
        </div>
      </Router>
    </>
  );
};

export default App;
