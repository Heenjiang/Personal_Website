import React from 'react';
import './App.css';
import SignIn from './sign-in/SignIn';
import SignUp from './sign-up/SignUp';
import Header from './footer-and-header/Header'
import Footer from './footer-and-header/Footer'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom'

function App() {
  return (
    <Router>
      <Switch>
        <Route  path="/user/signin">
          <SignIn />
        </Route>
        <Route  path="/user/signup">
          <SignUp />
        </Route>
        <Route path="/">
          <Header />
          <Switch>
            <Route exact path="/" render={() => <h1> Home page</h1>}>
            </Route>
            <Route path="/about" render={() => <h1> About Us Page</h1>}>
            </Route>
            <Route path="/blog" render={() => <h1> Blog Page</h1>}>
            </Route>
          </Switch>
          <Footer />
        </Route>
      </Switch>
   </Router>
  );
}

export default App;
