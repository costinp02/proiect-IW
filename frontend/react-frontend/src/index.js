import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';
import {Route, BrowserRouter as Router, Routes} from 'react-router-dom';  //routes = switch


// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <Router>
//     <React.StrictMode>
//     <Header />
//                   <Routes>
//                   <Route exact path="/" component={App}/>
//                   </Routes>
//                   <Footer />
    
//   </React.StrictMode>
//   </Router>
  
// );

const routing = (
              <Router>
                <React.StrictMode>
                  <Header />
                  <App/>
                  <Footer />
                </React.StrictMode>
              </Router>
);

ReactDOM.render(routing, document.getElementById('root'))

