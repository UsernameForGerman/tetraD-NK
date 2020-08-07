import React, {useState} from "react";
import '../styles/main.scss';

import Header from "./header";
import SEO from "./seo";
import Footer from "./footer";
import {message, Modal} from "antd";
import {CMS_URL} from "../getBaseUrl";

const formUrl = CMS_URL + "contact/";

const Layout = ({ children, title }) => {
    const [isOpen, setOpen] = useState(false);
    let contactsRef = React.createRef();
    let handleCancel = () => {
        setOpen(false);
    }

    const openModal = () => {
        setOpen(true);
    }

    let handleSubmit = (ref) => {
        let val = ref.current.value;
        if (val){
            handleCancel();
            let req = new XMLHttpRequest();
            req.open("POST", formUrl);
            req.send(JSON.stringify({
                contact : ref.current.value,
            }));
            req.setRequestHeader('Content-Type', 'application/json');
            message
                .loading('Отправка контактов..', 1.5)
                .then(() => message.success('Контакты отправлены', 1.5))
        } else {
            message.error("Введите контакты", 3)
        }
    }
  return (
    <>
      <SEO title={title}/>
      <Header openModal={openModal}/>
      <div>
        <main>
            {React.cloneElement(children, { openModal, handleSubmit })}</main>
        <Footer/>
          <Modal
              title="Обсудить проект"
              visible={isOpen}
              onCancel={handleCancel}
              footer={[
                  <button onClick={(e) => {
                      handleSubmit(contactsRef)
                  }}>Отправить</button>
              ]}
          >
              <h2>Оставьте ваши контакты и мы свяжемся с вами</h2>
              <input ref={contactsRef} type="text" required placeholder="Email/телефон"/>
          </Modal>
      </div>
    </>
  )
}
export default Layout;
