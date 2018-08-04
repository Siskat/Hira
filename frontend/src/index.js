import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import LoginPage from './loginpage';
import registerServiceWorker from './registerServiceWorker';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

ReactDOM.render(
    <BrowserRouter>
      <Switch>
      <Route path="/" component={App}/>
      <Route path="/login" component={LoginPage}/>
      </Switch>
    </BrowserRouter>,
    document.getElementById('root'));
registerServiceWorker();
