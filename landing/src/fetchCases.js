import axios from "axios";
import {CMS_URL} from "./getBaseUrl";

export default function fetchCases(setFetching, setCases) {
    setFetching(true);
    axios.create({
        baseURL: CMS_URL
    }).get('cases/').then(resp => {
        setCases(resp.data)
    })
}
