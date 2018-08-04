import React from 'react';
import './App.css';
import { Button } from 'reactstrap';

export default class MainPage extends React.Component {
  render() {
    return (
      <div class="parent">
        <div class="main-logo">
          <h1>HIRA</h1>
          <div>Make Appointments and hospital life easier, Hospitals don't need to be scary.</div>
        </div>
        <Button color="dark-blue">primary</Button>{' '}
      </div>
    )
  }
}