import React from "react";

export default function CTA({handleSubmit}) {
    let contactsRef = React.createRef();
    return(
        <div className="cta">
            <div className="cta-title">Оставьте свои контакты и получите скидку</div>
            <div className="cta-input-wrapper">
                <input type="text" name="email" ref={contactsRef} placeholder="Введите контакты"/>
                <button className="offer-callback-btn" onClick={(e) => handleSubmit(contactsRef)}>Получить скидку</button>
            </div>
        </div>
    )
}
