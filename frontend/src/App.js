import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import TopNav from './navbar.js';
import MainPage from './mainpage.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'reactstrap';

class App extends Component {
  render() {
    return (
      <div className="App">
        < TopNav />
      <Container>
        <Col sm="12" md={{ size: 8, offset: 2 }}>
        <br />
        <br />
          <MainPage />
        </Col>
      </Container>
      </div>
    );
  }
}

export default App;
