import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import Home from "./components/Home.vue";
import BannerGenerator from "./components/BannerGenerator.vue";
import VideoGenerator from "./components/VideoGenerator.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/banner", component: BannerGenerator },
    { path: "/video", component: VideoGenerator },
  ],
});

createApp(App).use(router).mount("#app");
