import React from "react";
import logo from "../images/fav.png"
export default function Footer() {
    return(
        <footer>
            <img src={logo} alt={"Footer logo"} className="footer-logo"/>
            <div className="footer-email">
                <a href="mailto:hello@tetradnk.ru">hello@tetradnk.ru</a>
            </div>
            <div className="footer-info">
                <div className="footer-info-item">ИП Поляк Олег Борисович</div>
                <div className="footer-info-item">ИНН: 165111276533</div>
                <div className="footer-info-item">ОГРНИП: 318169000088152</div>
            </div>
            <div className="footer-social-btns">

            </div>
        </footer>
    )
}
