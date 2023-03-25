import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';
import Regiser from './components/Register';
import Login from './components/Login';
import Logout from './components/Logout'
import {BrowserRouter as Router, Route, Routes as Switch} from 'react-router-dom';  //routes = switch


const routing = (
              <Router>
                <React.StrictMode>
                  <Header />
                  <Switch> 
                    <Route exact path="/" element={<App/>}/>
                    <Route exact path="/register" element={<Regiser/>}/>
                    <Route exact path="/login" element={<Login/>}/>
                  </Switch>
                  <Footer />
                </React.StrictMode>
              </Router>
);

ReactDOM.render(routing, document.getElementById('root'))

