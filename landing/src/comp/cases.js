import React, {useEffect, useState} from "react";
import { Carousel } from 'antd';
import 'antd/dist/antd.css';
import {Link} from 'react-router-dom'
import fetchCases from "../fetchCases";

export default function Cases() {
    const [cases, setCases] = useState([]);
    const [fetching, setFetching] = useState(false);
    useEffect(() => {
        if (cases.length === 0 && !fetching){
            fetchCases(
                setFetching, setCases
            )
        }
    })
    return (
        <Carousel autoplay>
            {cases ? cases.map(elem => {
                // let img = elem.img[0];
                let img = elem.image;
                return (
                    <Link to={`/case/${elem.title.toString().toLowerCase()}`} style={{width: "100%"}}>
                        <div className="offer-case">
                            //<img src={img.name} className="offer-case-img" alt={"Offer img"}/>
                            <img src={img} className="offer-case-img" alt={"Offer img"}/>
                            <div className="offer-case-main">
                                <h2 className="offer-case-main-title">{elem.title}</h2>
                                <div className="offer-case-main-desc">{elem.description}</div>
                                <button className="offer-case-main-btn">Читать подробнее</button>
                            </div>
                        </div>
                    </Link>
                )
            }) : <></>}
        </Carousel>
    )
}
