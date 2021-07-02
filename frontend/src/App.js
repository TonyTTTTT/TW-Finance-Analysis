import React from 'react';
import {Switch, Route, Link, BrowserRouter} from 'react-router-dom';
import TestPage from './Components/TestPage';
import HomePage from "./Components/HomePage";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
        <BrowserRouter>
          <div>
            <ul>
              <li style={{display: 'none'}}><Link to="/test">Test</Link></li>
              <li style={{display: 'none'}}><Link to="/">Home</Link></li>
            </ul>
            <Switch>
              <Route exact path="/test" component={TestPage}/>
              <Route exact path="/" component={HomePage}/>
            </Switch>
          </div>
        </BrowserRouter>
    );
  }
}
export default App;