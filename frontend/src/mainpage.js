import React, { Component } from 'react';
import './App.css';
import { Button } from 'reactstrap';
import {Link} from 'react-router-dom';

export default class MainPage extends Component {
  render() {
    return (
      <div>
        <div class="main-logo">
          <br />
          <br />
          <h1>HIRA</h1>
          <div>Make Appointments and hospital life easier, Hospitals don't need to be scary.</div>
        </div>
        <br />
        <br />
        <Link to='/loginpage'><Button color="dark-blue" size="lg">Log in</Button>{' '}</Link>
      </div>
    )
  }
}