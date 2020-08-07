import React from "react"

import Layout from "../comp/layout"
import Offer from "../comp/offer";
import Cases from "../comp/cases";
import CTA from "../comp/cta";
import 'antd/dist/antd.css';
const Index = ({handleSubmit, openModal}) => {
    return (
        <main>
            <Offer handleSubmit={handleSubmit} openModal={openModal}/>
            <Cases/>
            <CTA handleSubmit={handleSubmit}/>
        </main>
    )
}
const IndexPage = () => {
    return(
        <Layout title="Главная">
            <Index/>
        </Layout>
    )
}

export default IndexPage
