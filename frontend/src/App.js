import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, NavLink } from "react-router-dom";
import Navbar from "./components/Navbar";
import VenueCard from "./components/VenueCard";

function App() {
  return (
    <div>
      <Navbar/>
      <div className="container">
        <Router basename="/">
          <Route path="/"/>
        </Router>
        <VenueCard/>
      </div>
    </div>
  );
}

export default App;
