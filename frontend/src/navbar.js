import React from 'react';
import { Link } from "react-router-dom";
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem } from 'reactstrap';

export default class TopNav extends React.Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false,
      loggedIn: true
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  logIn() {
    this.setState({
      loggedIn: !this.state.loggedIn
    })
  }

  render() {
    return (
      <div>
        <Navbar color="dark-blue" light expand="md">
          <NavbarBrand href="/" color="white">Hira</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar>
              { this.state.loggedIn && 
              <div>
              <NavItem style={{display:'inline-block'}}>
                <NavLink>Welcome Doctor/Nurse</NavLink>
              </NavItem>
              <NavItem style={{display:'inline-block'}}>
                <NavLink href="/components/">Settings</NavLink>
              </NavItem>
              <NavItem style={{display:'inline-block'}}>
                <NavLink href="#">Log Out</NavLink>
              </NavItem> 
              </div> }
              { !this.state.loggedIn &&
              <div>
                <NavItem style={{display:'inline-block'}}>
                  <NavLink href="#">Log In</NavLink>
                </NavItem>
              </div>} 
            </Nav>
          </Collapse>
        </Navbar>
      </div>
    );
  }
}