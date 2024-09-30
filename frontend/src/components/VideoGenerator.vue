<template>
  <div class="video-page-container min-h-screen relative">
    <div class="video-generator max-w-4xl mx-auto my-12 p-8 bg-white dark:bg-gray-800 rounded-xl shadow-2xl relative z-10">
      <div class="text-center mb-8">
        <h2 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">AI Video Generator</h2>
        <p class="text-xl text-gray-300 mt-2">Create engaging videos with the power of AI</p>
      </div>
      <form @submit.prevent="generateVideo" class="space-y-6">
        <div class="form-group">
          <label for="productImage" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-image mr-2"></i>Product Image:
          </label>
          <input type="file" id="productImage" @change="onFileChange" accept="image/*" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="offer" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-tag mr-2"></i>Promotional Offer:
          </label>
          <input v-model="offer" type="text" id="offer" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="theme" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-paint-brush mr-2"></i>Theme:
          </label>
          <input v-model="theme" type="text" id="theme" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="colorPalette" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-palette mr-2"></i>Color Palette:
          </label>
          <input v-model="colorPalette" type="text" id="colorPalette" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="size" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-expand-arrows-alt mr-2"></i>Size:
          </label>
          <input v-model="size" type="text" id="size" placeholder="1200x628" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="duration" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-clock mr-2"></i>Duration (seconds):
          </label>
          <input v-model="duration" type="number" id="duration" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <button type="submit" :disabled="isLoading"
                class="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg py-3 px-4 font-bold text-lg hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300 transform hover:scale-105">
          <i class="fas fa-video mr-2"></i>{{ isLoading ? 'Generating...' : 'Generate Video' }}
        </button>
      </form>
      <div v-if="isLoading" class="flex justify-center items-center mt-8">
        <div class="loader"></div>
      </div>
      <div v-if="result" class="mt-8 animate-fade-in">
        <video :src="result.video_path" controls class="w-full rounded-lg shadow-lg"></video>
        <p class="mt-4 text-gray-700 dark:text-gray-300"><strong>Generated Prompt:</strong> {{ result.prompt }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoGenerator',
  data() {
    return {
      file: null,
      offer: '',
      theme: '',
      colorPalette: '',
      size: '',
      duration: null,
      result: null,
      isLoading: false
    }
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0]
    },
    async generateVideo() {
      this.isLoading = true;
      const formData = new FormData()
      formData.append('productImage', this.file)
      formData.append('offer', this.offer)
      formData.append('theme', this.theme)
      formData.append('colorPalette', this.colorPalette)
      formData.append('size', this.size)
      formData.append('duration', this.duration)

      try {
        const response = await fetch('/generate_video', {
          method: 'POST',
          body: formData
        })
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        this.result = await response.json()
      } catch (error) {
        console.error('Error:', error)
        alert('An error occurred while generating the video.')
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style scoped>
.video-generator {
  transition: all 0.3s ease-in-out;
}

.form-group {
  transition: all 0.3s ease-in-out;
}

.form-group:hover {
  transform: translateY(-2px);
}

input, select {
  transition: all 0.3s ease-in-out;
}

input:hover, select:hover {
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.5);
}

.loader {
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes gradientAnimation {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.animate-gradient {
  animation: gradientAnimation 15s ease infinite;
  background-size: 400% 400%;
}
</style>

<style>
:root {
  --bg-gradient-1: #e0f2fe;  /* Light sky blue */
  --bg-gradient-2: #fae8ff;  /* Light lavender */
  --bg-gradient-3: #f0fdf4;  /* Light mint */
}

.dark {
  --bg-gradient-1: #0f172a;  /* Deep navy */
  --bg-gradient-2: #292524;  /* Dark brown */
  --bg-gradient-3: #1e293b;  /* Dark slate blue */
}
</style>

<style scoped>
.video-page-container {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--bg-gradient-1),
    var(--bg-gradient-2),
    var(--bg-gradient-3),
    var(--bg-gradient-2));
  background-size: 400% 400%;
  animation: gradientAnimation 20s ease infinite;
  position: relative;
  overflow: hidden;
}

@keyframes gradientAnimation {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* Add any other scoped styles you need */
</style>