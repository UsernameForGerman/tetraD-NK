import React from "react";
import graph from "../images/graph.jpeg";
import scrap from "../images/scpars.png";
import mac from "../images/mac-2.png";
import screen from "../images/screen.png";

export default function Offer({handleSubmit}) {
    let contactsRef = React.createRef();
    return (
    <div className="offer">
        <div className="offer-main">
            <div className="offer-main-wrapper">
                <div className="offer-main-list">
                    <p>Создадим сайт от <b>3х дней</b></p>
                    <p>Напишем <b>бесплатно</b> ТЗ</p>
                    <p><b>Нешаблонные</b> решения</p>
                </div>
                <div className="offer-main-mac">
                    <img src={mac} alt={"macbook air"}/>
                    <div className="offer-main-abs">
                        <img src={screen} alt={"Screen"}/>
                    </div>
                </div>
            </div>
            <div className="offer-main-cta">
                <h6>Оставьте контакты и мы перезвоним</h6>
                <div className="offer-main-cta-input-wrapper">
                    <input type="text" name="email" ref={contactsRef} placeholder="Введите контакты"/>
                    <button className="offer-callback-btn" onClick={(e) => handleSubmit(contactsRef)}>Получить консультацию</button>
                </div>
            </div>
        </div>
        <div className="promo">
            <div className="promo-case">
                <img src={graph} className="promo-case-bck" alt="background"/>
                <div className="promo-case-title">
                    Автоматизация и оцифровка бизнес-процессов
                </div>
                <ol className="promo-case-list">
                    <li className="promo-case-list-item">Создаем <mark>для Клиента</mark></li>
                    <li className="promo-case-list-item">Поднимаем <mark>статус</mark> компании</li>
                    <li className="promo-case-list-item">Показываем сложное <mark>понятнее</mark></li>
                    <button
                        className="offer-callback-btn"
                    >Обсудить проект</button>
                </ol>
            </div>
            <div className="promo-case">
                <img src={scrap} className="promo-case-bck" alt="background"/>
                <div className="promo-case-title">
                    Корпоративный портал
                </div>
                <ol className="promo-case-list">
                    <li className="promo-case-list-item">Обрабатываем <mark>большие данные</mark></li>
                    <li className="promo-case-list-item">Переводим бизнес-процессы в <mark>онлайн</mark></li>
                    <li className="promo-case-list-item">Создаем <mark>понятные</mark> интерфейсы</li>
                    <button
                        className="offer-callback-btn"
                    >Обсудить проект</button>
                </ol>
            </div>
        </div>
    </div>
    )
}
