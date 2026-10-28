import axios from "axios";

const api = axios.create({
  baseURL: "https://disasterconnectai-1.onrender.com/api",
});

export default api;
