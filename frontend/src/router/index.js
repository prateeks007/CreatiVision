import { createRouter, createWebHashHistory } from "vue-router";
import { supabase } from "../lib/supabase";
import Home from "../components/Home.vue";
import BannerGenerator from "../components/BannerGenerator.vue";
import VideoGenerator from "../components/VideoGenerator.vue";
import AuthForm from "../components/AuthForm.vue";

const routes = [
  {
    path: "/",
    redirect: "/auth",
  },
  {
    path: "/home",
    component: Home,
    meta: { requiresAuth: true },
  },
  {
    path: "/banner",
    component: BannerGenerator,
    meta: { requiresAuth: true },
  },
  {
    path: "/video",
    component: VideoGenerator,
    meta: { requiresAuth: true },
  },
  {
    path: "/auth",
    component: AuthForm,
    meta: { requiresUnauth: true },
  },
  // Add catch-all route
  {
    path: "/:pathMatch(.*)*",
    redirect: "/auth",
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

// Add navigation guard
router.beforeEach(async (to, from, next) => {
  // Wait for supabase to initialize
  const {
    data: { session },
  } = await supabase.auth.getSession();

  if (to.meta.requiresAuth && !session) {
    // If route requires auth and no session exists, redirect to auth page
    next("/auth");
  } else if (to.path === "/auth" && session) {
    // If trying to access auth page with active session, redirect to home
    next("/home");
  } else {
    next();
  }
});

export default router;
