import React from "react";

const VenueCard = (props) => {
    return (
        <div className="card" style={{width: "18rem"}}>
            <img className="card-img-top" src=""/>
            <div className="card-body">
                <h5 className="card-title">Venue 1</h5>
                <p className="card-text">123 Address Ave</p>
                <span>Fun! Meter</span>
                <div className="progress mb-3">
                    <div className="progress-bar bg-success" style={{width: "78%"}} role="progressbar" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100">78%</div>
                </div>
                <a href="#" className="btn btn-primary">Go somewhere</a>
            </div>
        </div>
    )
}

export default VenueCard;