import React from "react";
import logo from "../images/fav.png"
export default function Footer() {
    return(
        <footer>
            <img src={logo} alt={"Footer logo"} className="footer-logo"/>
            <div className="footer-email">
                <a href="mailto:polyakgerman@gmail.com">polyakgerman@gmail.com</a>
            </div>
            <div className="footer-social-btns">

            </div>
        </footer>
    )
}
