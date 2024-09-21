import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import BannerGenerator from "../components/BannerGenerator.vue";
import VideoGenerator from "../components/VideoGenerator.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/banner", component: BannerGenerator },
  { path: "/video", component: VideoGenerator },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
