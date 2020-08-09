import React from 'react';
import './App.css';
import IndexPage from "./pages";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Case from "./pages/case/case";
import ErrorPage from "./comp/404";

function App() {
  return (
    <div className="App">
        <BrowserRouter basename={process.env.public_url}>
            <Switch>
                <Route path={`/`} exact>
                    <IndexPage/>
                </Route>
                <Route path={`/case/:elem`} exact>
                    <Case/>
                </Route>
                <Route>
                    <ErrorPage/>
                </Route>
            </Switch>
        </BrowserRouter>
    </div>
  );
}

export default App;
