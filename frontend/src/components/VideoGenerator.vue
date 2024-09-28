<template>
  <div class="video-generator p-8 backdrop-filter backdrop-blur-sm rounded-xl">
    <h2 class="text-3xl font-bold text-blue-300 mb-8 text-center">AI Video Generator</h2>
    <form @submit.prevent="generateVideo" class="space-y-6 max-w-md mx-auto">
      <div class="form-group">
        <label for="productImage" class="block text-lg font-medium text-blue-200 mb-2">Product Image:</label>
        <input type="file" id="productImage" @change="onFileChange" accept="image/*" required
               class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="offer" class="block text-lg font-medium text-blue-200 mb-2">Promotional Offer:</label>
        <input v-model="offer" type="text" id="offer" required
               class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="theme" class="block text-lg font-medium text-blue-200 mb-2">Theme:</label>
        <input v-model="theme" type="text" id="theme" required
               class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="colorPalette" class="block text-lg font-medium text-blue-200 mb-2">Color Palette (comma-separated):</label>
        <input v-model="colorPalette" type="text" id="colorPalette" required
               class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="size" class="block text-lg font-medium text-blue-200 mb-2">Size (e.g., 1200x628):</label>
        <input v-model="size" type="text" id="size" required
               class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="duration" class="block text-lg font-medium text-blue-200 mb-2">Duration (seconds):</label>
        <input v-model="duration" type="number" id="duration" required
               class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <button type="submit" :disabled="isLoading"
              class="w-full bg-blue-600 text-white rounded-full py-3 px-6 font-bold text-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300 transform hover:scale-105">
        {{ isLoading ? 'Generating...' : 'Generate Video' }}
      </button>
    </form>
    <div v-if="isLoading" class="mt-8">
      <div class="loader"></div>
    </div>
    <div v-if="result" class="result mt-8 animate-fade-in">
      <video :src="result.video_path" controls class="w-full rounded-lg shadow-lg"></video>
      <p class="mt-4 text-blue-200"><strong>Generated Prompt:</strong> {{ result.prompt }}</p>
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
  max-width: 600px;
  margin: 0 auto;
  background: var(--color-surface);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 2rem;
}

.loader {
  border: 4px solid rgba(59, 130, 246, 0.3);
  border-radius: 50%;
  border-top: 4px solid #3b82f6;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 0 auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.form-group {
  transition: all 0.3s ease;
}

.form-group:focus-within {
  transform: translateY(-2px);
}

input[type="file"] {
  cursor: pointer;
}

input[type="file"]::-webkit-file-upload-button {
  visibility: hidden;
}

input[type="file"]::before {
  content: 'Select file';
  display: inline-block;
  background: var(--color-primary);
  color: var(--color-on-primary);
  padding: 8px 12px;
  border-radius: 20px;
  cursor: pointer;
}

input[type="file"]:hover::before {
  background: var(--color-secondary);
}

input[type="file"]:active::before {
  background: var(--color-primary);
}
</style>