import React, { useState } from "react";
import VenueCard from "./VenueCard"


const Cards = () => {
    const [cards, setCards] = useState();
    return (
        <div>
            <h1 className="display-4 my-4" style={{textAlign: "center"}}>Vancouver, BC</h1>
            <div className="card-container">
                <VenueCard venueName="Venue 1" venueAddress="123 Address Ave" funPercent="78"/>
                <VenueCard venueName="Venue 2" venueAddress="123 Address Rd" funPercent="56"/>
                <VenueCard venueName="Venue 3" venueAddress="123 Address Circle" funPercent="14"/>
            </div>
        </div>
    )
}

export default Cards;