import React from "react";
import { Link } from "react-router-dom";

const VenueCard = (props) => {
    return (
        <div className="card mr-2 ml-2" style={{width: "18rem"}}>
            <img className="card-img-top" src="https://i.ticketweb.com//i/venue/83154_Venue.jpg?v=30" alt=""/>
            <div className="card-body">
                <h5 className="card-title">{props.venueName}</h5>
                <p className="card-text">{props.venueAddress}</p>
                <span>Fun! Meter</span>
                <div className="progress mb-3">
                    <div className="progress-bar bg-success" style={{width: props.funPercent+"%"}} role="progressbar" aria-valuenow={props.funPercent} aria-valuemin="0" aria-valuemax="100">{props.funPercent}%</div>
                </div>
                <Link to={`/venue/${props.venueName}`} className="btn btn-primary">Check out {props.venueName}!</Link>
            </div>
        </div>
    )
}

export default VenueCard;