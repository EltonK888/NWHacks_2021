import React, { useState } from "react";
import VenueCard from "./VenueCard"


const Cards = () => {
    const [cards, setCards] = useState();
    return (
        <div>
            <h1 className="display-4 my-4" style={{textAlign: "center"}}>Vancouver, BC</h1>
            <div className="cards">
                <VenueCard venueName="Venue 1" venueAddress="123 Address Ave" funPercent="78" imageLink="https://i.ticketweb.com//i/venue/83154_Venue.jpg?v=30"/>
                <VenueCard venueName="Venue 2" venueAddress="123 Address Rd" funPercent="56" imageLink="https://www.savourychef.com/wp-content/gallery/venue-nightclub/vancouver-venue-night-club-5.jpg"/>
                <VenueCard venueName="Venue 3" venueAddress="123 Address Circle" funPercent="14" imageLink="https://pbs.twimg.com/media/DXxN_TTWkAApGG2.jpg"/>
            </div>
        </div>
    )
}

export default Cards;