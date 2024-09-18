<template>
  <div id="app" :class="{ 'dark-mode': isDarkMode }">
    <header>
      <div class="header-content">
        <h1>AI Content Generator</h1>
        <nav>
          <router-link to="/" exact>Home</router-link>
          <router-link to="/banner">Banner</router-link>
          <router-link to="/video">Video</router-link>
        </nav>
        <button @click="toggleDarkMode" class="dark-mode-toggle">
          {{ isDarkMode ? '☀️' : '🌙' }}
        </button>
      </div>
    </header>
    <main>
      <router-view></router-view>
    </main>
    <footer>
      <p>&copy; Gemini AI Hackathon</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isDarkMode: false
    }
  },
  methods: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
      localStorage.setItem('darkMode', this.isDarkMode);
    }
  },
  mounted() {
    this.isDarkMode = localStorage.getItem('darkMode') === 'true';
  }
}
</script>

<style>
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --background-color: #f5f5f5;
  --text-color: #333;
  --header-color: #fff;
  --container-bg: #ffffff;
}

.dark-mode {
  --primary-color: #2980b9;
  --secondary-color: #27ae60;
  --background-color: #121212;
  --text-color: #f5f5f5;
  --header-color: #ecf0f1;
  --container-bg: #1e1e1e;
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: 'Roboto', Arial, sans-serif;
}

body {
  background-color: var(--background-color);
  color: var(--text-color);
  transition: background-color 0.3s, color 0.3s;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--background-color);
}

header {
  background-color: var(--primary-color);
  color: var(--header-color);
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

h1 {
  margin: 0;
  font-size: 1.5rem;
}

nav {
  display: flex;
  gap: 1rem;
}

nav a {
  color: var(--header-color);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s, color 0.3s;
}

nav a:hover, nav a.router-link-active {
  background-color: rgba(255, 255, 255, 0.2);
}

main {
  flex-grow: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  box-sizing: border-box;
}

.container {
  background-color: var(--container-bg);
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.dark-mode-toggle {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--header-color);
}

footer {
  background-color: var(--primary-color);
  color: var(--header-color);
  text-align: center;
  padding: 1rem;
  margin-top: auto;
}

button {
  background-color: var(--secondary-color);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #27ae60;
}

input[type="text"],
input[type="file"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 1rem;
}

.dark-mode input[type="text"],
.dark-mode input[type="file"] {
  background-color: #34495e;
  color: #ecf0f1;
  border-color: #7f8c8d;
}
</style>
