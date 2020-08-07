import React, {useEffect, useState} from "react";
import Layout from "../../comp/layout";
import 'antd/dist/antd.css';
import { Timeline } from 'antd';
import AimOutlined from "@ant-design/icons/lib/icons/AimOutlined";
import OrderedListOutlined from "@ant-design/icons/lib/icons/OrderedListOutlined";
import InfoOutlined from "@ant-design/icons/lib/icons/InfoOutlined";
import CheckOutlined from "@ant-design/icons/lib/icons/CheckOutlined";
import ClockCircleOutlined from "@ant-design/icons/lib/icons/ClockCircleOutlined";
import DollarCircleOutlined from "@ant-design/icons/lib/icons/DollarCircleOutlined";
import {withRouter} from "react-router-dom";
import fetchCases from "../../fetchCases";
function Case(props) {
    const title = props.match.params.elem;
    const [elems, setElems] = useState();
    const [fetching, setFetching] = useState(false);
    useEffect(() => {
        if (!elems && !fetching){
            fetchCases(
                setFetching, setElems
            )
        }
    })
    if (!elems) return (<></>);
    const elem = elems.filter(el => el.title.toLowerCase() === title)[0]
    const tasks = elem.tasks.map(task => task.task).filter(task => task !== null && task !== undefined);
    let document = elem.document[0] ? elem.document[0] : {};
    let renderedTasks = "";
    if (tasks.length > 0){
        renderedTasks = (
            <div className="case-tasks">
                <h2 className="case-tasks-title">
                    <OrderedListOutlined className="icon" /> Задачи
                </h2>
                <Timeline className="case-tasks-list">
                    {tasks.map(task => {
                        return (<Timeline.Item className="case-tasks-list-item">{task}</Timeline.Item>)
                    })}
                </Timeline>
            </div>
        )
    }
    return (<Layout title={elem.title}>
        <div className="case">
            <div className="case-name">
                <h1><a href={elem.link}>{elem.title}</a></h1>
                {document
                    ? <h4><a href={document.url}>Презентация проекта</a></h4>
                    : <></>
                }
            </div>
            <div className="case-row">
                <div className="case-desc">
                    <h2 className="case-desc-title">
                        <InfoOutlined className="icon"/> Описание
                    </h2>
                    {elem.desc}
                </div>
                <div className="case-target">
                    <h2 className="case-target-title">
                        <AimOutlined className="icon" spin/> Цель
                    </h2>
                    {elem.target}
                </div>
                {renderedTasks}
            </div>
            <div className="case-row">
                <div className="case-solution">
                    <h2 className="case-solution-title">
                        <CheckOutlined className="icon" /> Решение
                    </h2>
                    {elem.solution}
                </div>
                <div className="case-time">
                    <h2 className="case-time-title">
                        <ClockCircleOutlined className="icon" /> Время
                    </h2>
                    {elem.time}
                </div>
                <div className="case-price">
                    <h2 className="case-time-title">
                        <DollarCircleOutlined className="icon" /> Цена
                    </h2>
                    {elem.price}
                </div>
            </div>
        </div>
    </Layout>)
}

export default withRouter(Case)
