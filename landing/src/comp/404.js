import React from "react";
import Layout from "./layout";
import {NavLink} from "react-router-dom";
export default function ErrorPage() {
    debugger
    return(
        <Layout title={"Ошибка 404"}>
            <div className={"error-wrapper"}>
                <div className="error-title">
                    404
                </div>
                <div className="error-desc">
                    Такой страницы не существует
                </div>
                <div className="error-link">
                    <NavLink to={"/"}>
                        Вернуться на главную
                    </NavLink>
                </div>
            </div>
        </Layout>
    )
}
