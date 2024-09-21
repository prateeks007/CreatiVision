import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; // Import the router
import "./global.css"; // Import global CSS
// import Home from "./components/Home.vue";
import "./assets/styles.css"; // Import Tailwind CSS
// import VideoGenerator from "./components/VideoGenerator.vue";
const app = createApp(App);
app.use(router); // Use the router
app.mount("#app");
