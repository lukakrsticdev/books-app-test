import axios from "axios";
import {store} from "./store";

export const api = axios.create({
  baseURL: "http://localhost:8000/api/",
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use((config) => {
  const token = store.state.token;
  if (token) {
    config.headers.Authorization = "Token " + token;
  }
  return config;
});
