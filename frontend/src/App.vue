<template>
  <div
    id="app"
    class="flex flex-col min-h-screen font-sans relative"
    :class="{ dark: isDarkMode }"
  >
    <div class="content-wrapper relative z-10 flex flex-col min-h-screen">
      <nav v-if="session" class="bg-white dark:bg-gray-800 shadow-md">
        <div
          class="container mx-auto px-6 py-3 flex justify-between items-center"
        >
          <router-link
            to="/home"
            class="text-2xl font-bold text-gray-800 dark:text-white"
          >
            CreatiVision
          </router-link>
          <div class="flex items-center">
            <router-link to="/banner" class="nav-link mx-2"
              >Banner Generator</router-link
            >
            <router-link to="/video" class="nav-link mx-2"
              >Video Generator</router-link
            >
            <button @click="handleSignOut" class="nav-link mx-2">
              Sign Out
            </button>
            <button
              @click="toggleDarkMode"
              class="ml-4 p-2 rounded-full bg-gray-200 dark:bg-gray-700"
            >
              <span v-if="isDarkMode">🌞</span>
              <span v-else>🌙</span>
            </button>
          </div>
        </div>
      </nav>
      <router-view></router-view>
      <footer v-if="session" class="bg-gray-100 dark:bg-gray-800 py-4 mt-auto">
        <div
          class="container mx-auto text-center text-gray-600 dark:text-gray-300"
        >
          &copy; 2024 CreatiVision. All rights reserved.
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { supabase } from "./lib/supabase";
import { useRouter } from "vue-router";

export default {
  name: "App",
  setup() {
    const router = useRouter();
    const session = ref(null);
    const isDarkMode = ref(false);

    onMounted(async () => {
      // Get initial session
      const {
        data: { session: currentSession },
      } = await supabase.auth.getSession();
      session.value = currentSession;

      // Listen for auth changes
      supabase.auth.onAuthStateChange((_event, currentSession) => {
        session.value = currentSession;
        if (!currentSession) {
          router.push("/auth");
        }
      });

      // Set dark mode from localStorage
      isDarkMode.value = localStorage.getItem("darkMode") === "true";
      document.documentElement.classList.toggle("dark", isDarkMode.value);
    });

    const handleSignOut = async () => {
      try {
        await supabase.auth.signOut();
        router.push("/auth");
      } catch (error) {
        console.error("Error signing out:", error);
      }
    };

    const toggleDarkMode = () => {
      isDarkMode.value = !isDarkMode.value;
      localStorage.setItem("darkMode", isDarkMode.value);
      document.documentElement.classList.toggle("dark", isDarkMode.value);
    };

    return {
      session,
      isDarkMode,
      handleSignOut,
      toggleDarkMode,
    };
  },
};
</script>
