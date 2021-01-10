import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, NavLink } from "react-router-dom";
import Navbar from "./components/Navbar";
import VenueCard from "./components/VenueCard";
import Cards from "./components/Cards";
import Venue from "./components/Venue";

function App() {
  return (
    <div>
      <Navbar/>
      <div className="container">
        <Router basename="/">
          <Route path="/" exact component={Cards}/>
          <Route path="/venue/:venueName" exact render={(props) => <Venue {...props} />}/>
        </Router>
      </div>
    </div>
  );
}

export default App;
