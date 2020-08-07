import React from 'react';
import './App.css';
import IndexPage from "./pages";
import {BrowserRouter, Route} from "react-router-dom";
import Case from "./pages/case/case";

function App() {
  return (
    <div className="App">
        <BrowserRouter basename={process.env.public_url}>
            <Route path={`/`} exact>
                <IndexPage/>
            </Route>
            <Route path={`/case/:elem`} exact>
                <Case/>
            </Route>
        </BrowserRouter>
    </div>
  );
}

export default App;
