import React, {useEffect, useState} from "react";
import 'antd/dist/antd.css';
import {Link} from 'react-router-dom'
import fetchCases from "../fetchCases";
import {Carousel} from "antd";
import {LeftOutlined, RightOutlined} from '@ant-design/icons';

export default function Cases() {
    const [cases, setCases] = useState([]);
    const [fetching, setFetching] = useState(false);
    let carousel = React.createRef();
    useEffect(() => {
        if (cases.length === 0 && !fetching){
            fetchCases(
                setFetching, setCases
            )
        }
    })
    return (
        <>{
            cases
                ? <>
                <div className="nav-icons">
                    <LeftOutlined onClick={() => carousel.prev()} />
                    <RightOutlined onClick={() => carousel.next()} />
                </div>
                <Carousel autoplay arrows accessibility ref={node => (carousel = node)}>
                    {cases.map(elem => {
                        let img = elem.image;
                        return (
                            <Link to={`/case/${elem.title.toString().toLowerCase()}`} style={{width: "100%"}}>
                                <div className="offer-case">
                                    <img src={img} className="offer-case-img" alt={"Offer img"}/>
                                    <div className="offer-case-main">
                                        <h2 className="offer-case-main-title">{elem.title}</h2>
                                        <div className="offer-case-main-desc">{elem.description}</div>
                                        <button className="offer-case-main-btn">Читать подробнее</button>
                                    </div>
                                </div>
                            </Link>
                        )
                    })}
                </Carousel>
                </>
                : <></>
        }
        </>
    )
}
