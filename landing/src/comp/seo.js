import React from "react"
import { Helmet } from "react-helmet"

function SEO({ description, lang, meta, title }) {

  return (
    <Helmet
      htmlAttributes={{
        lang,
      }}
      title={title}
      titleTemplate={`TetraD-NK`}
    />
  )
}

export default SEO
