<template>
  <div
    id="app"
    class="flex flex-col min-h-screen font-sans relative"
    :class="{ dark: isDarkMode }"
  >
    <div class="content-wrapper relative z-10 flex flex-col min-h-screen">
      <nav class="bg-white dark:bg-gray-800 shadow-md">
        <div
          class="container mx-auto px-6 py-3 flex justify-between items-center"
        >
          <router-link
            to="/"
            class="text-2xl font-bold text-gray-800 dark:text-white"
            >CreatiVision</router-link
          >
          <div class="flex items-center">
            <router-link to="/banner" class="nav-link mx-2"
              >Banner Generator</router-link
            >
            <router-link to="/video" class="nav-link mx-2"
              >Video Generator</router-link
            >
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
      <footer class="bg-gray-100 dark:bg-gray-800 py-4 mt-auto">
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
export default {
  name: "App",
  data() {
    return {
      isDarkMode: false,
    };
  },
  methods: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
      localStorage.setItem("darkMode", this.isDarkMode);
      document.documentElement.classList.toggle("dark", this.isDarkMode);

      // Add transition to body
      document.body.style.transition = "background-color 0.5s ease";
    },
  },
  mounted() {
    this.isDarkMode = localStorage.getItem("darkMode") === "true";
    document.documentElement.classList.toggle("dark", this.isDarkMode);
  },
};
</script>
