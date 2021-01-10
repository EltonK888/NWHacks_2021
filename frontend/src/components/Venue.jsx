import React, { useState } from 'react';
import { Link } from "react-router-dom";

const Venue = (props) => {
    const [numPeople, setNumPeople] = useState(0);
    const [avgAge, setAvgAge] = useState(18);
    return (
        <div className="row mt-5 pt-5">
            <div className="col-sm-5">
                <img className="img-fluid" src={props.location.state.image} alt=""/>
            </div>
            <div className="col-sm-7">
                <h1>{props.match.params.venueName}</h1>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid quibusdam, commodi nostrum mollitia magni illum qui dolor distinctio vero deserunt quo, sed tenetur modi aspernatur magnam? Impedit doloremque architecto perferendis.</p>
                <div className="row">
                    <div className="col-sm-6">
                        <div className="row">
                            <div className="col-2">
                                <i className="fa fa-smile-o fa-3x" style={{color: "#f2500a"}}></i> 
                            </div>
                            <div className="col-10">
                                <h4>Fun factor</h4>
                                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo, voluptas.</p>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-6">
                        <div className="row">
                            <div className="col-2">
                                <i className="fa fa-music fa-3x" style={{color: "#f2500a"}}></i> 
                            </div>
                            <div className="col-10">
                                <h4>Music Genre</h4>
                                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo, voluptas.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="col-sm-6">
                        <div className="row">
                            <div className="col-2">
                                <i className="fa fa-image" style={{color: "#f2500a", fontSize: "38px"}}></i> 
                            </div>
                            <div className="col-10">
                                <h4>Theme tonight</h4>
                                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo, voluptas.</p>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-6">
                        <div className="row">
                            <div className="col-2">
                                <i className="fa fa-volume-up fa-3x" style={{color: "#f2500a"}}></i> 
                            </div>
                            <div className="col-10">
                                <h4>Sound (hype!) levels</h4>
                                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo, voluptas.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <Link to={"/"} className="btn btn-primary">Back to home</Link>
            </div>
        </div>
    )
}

export default Venue;