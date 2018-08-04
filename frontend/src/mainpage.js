import React, { Component } from 'react';
import './App.css';
import { Button } from 'reactstrap';

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
        <Button color="dark-blue" to="/login" size="lg">Log in</Button>{' '}
      </div>
    )
  }
}