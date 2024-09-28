<template>
  <div id="app" class="min-h-screen flex flex-col" :class="{ 'dark': isDarkMode }">
    <div class="animated-bg"></div>
    <header class="bg-opacity-90 bg-surface text-on-surface p-4 shadow-md z-10">
      <div class="container mx-auto flex items-center justify-between">
        <h1 class="text-2xl font-bold text-primary flex-shrink-0">CreatiVision</h1>
        <nav class="flex-grow flex justify-center -ml-[120px]">
          <ul class="flex space-x-6">
            <li><router-link to="/" class="nav-link text-lg">Home</router-link></li>
            <li><router-link to="/banner" class="nav-link text-lg">Banner</router-link></li>
            <li><router-link to="/video" class="nav-link text-lg">Video</router-link></li>
          </ul>
        </nav>
        <div class="flex items-center flex-shrink-0">
          <button @click="toggleDarkMode" class="text-2xl transition-transform transform hover:scale-110">
            {{ isDarkMode ? '☀️' : '🌙' }}
          </button>
          <button class="md:hidden ml-4" @click="toggleMobileMenu">
            ☰
          </button>
        </div>
      </div>
      <nav v-if="isMobileMenuOpen" class="md:hidden mt-4">
        <ul class="flex flex-col space-y-2">
          <li><router-link to="/" class="nav-link text-lg block" @click="closeMobileMenu">Home</router-link></li>
          <li><router-link to="/banner" class="nav-link text-lg block" @click="closeMobileMenu">Banner</router-link></li>
          <li><router-link to="/video" class="nav-link text-lg block" @click="closeMobileMenu">Video</router-link></li>
        </ul>
      </nav>
    </header>
    <main class="flex-grow container mx-auto p-4 z-10">
      <router-view></router-view>
    </main>
    <!-- <footer class="bg-opacity-90 bg-surface text-on-surface text-center p-4 z-10">
      <p>&copy; Gemini AI Hackathon</p>
    </footer> -->
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isDarkMode: true,
      isMobileMenuOpen: false
    }
  },
  methods: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode
      localStorage.setItem('darkMode', this.isDarkMode)
    },
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen
    },
    closeMobileMenu() {
      this.isMobileMenuOpen = false
    }
  },
  mounted() {
    this.isDarkMode = localStorage.getItem('darkMode') === 'true'
  }
}
</script>

<style>
:root {
  --color-primary: #4f46e5;
  --color-secondary: #818cf8;
  --color-background: #f3f4f6;
  --color-surface: #ffffff;
  --color-text: #1f2937;
  --color-text-light: #6b7280;
}

.dark {
  --color-primary: #818cf8;
  --color-secondary: #4f46e5;
  --color-background: #111827;
  --color-surface: #1f2937;
  --color-text: #f3f4f6;
  --color-text-light: #9ca3af;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: var(--color-background);
  color: var(--color-text);
  transition: background-color 0.3s, color 0.3s;
}

.animated-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(-45deg, var(--color-primary), var(--color-secondary), var(--color-background), var(--color-surface));
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  z-index: -1;
}

@keyframes gradientBG {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  width: 100%;
}

.nav-link {
  color: var(--color-text-light);
  transition: color 0.3s;
  position: relative;
  padding-bottom: 2px;
}

.nav-link:hover, .nav-link.router-link-active {
  color: var(--color-primary);
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: var(--color-primary);
  transform: scaleX(0);
  transition: transform 0.3s;
}

.nav-link:hover::after, .nav-link.router-link-active::after {
  transform: scaleX(1);
}
</style>