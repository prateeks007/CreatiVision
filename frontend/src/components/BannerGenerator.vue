<template>
  <div class="banner-page-container min-h-screen relative">
    <div class="banner-generator max-w-4xl mx-auto my-12 p-8 bg-white dark:bg-gray-800 rounded-xl shadow-2xl relative z-10">
      <div class="text-center mb-8">
        <h2 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">AI Banner Generator</h2>
        <p class="text-xl text-gray-300 mt-2">Create stunning banners with the power of AI</p>
      </div>
      <form @submit.prevent="generateBanner" class="space-y-6">
        <div class="form-group">
          <label for="productImages" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-images mr-2"></i>Product Images:
          </label>
          <input type="file" id="productImages" @change="onFileChange" accept="image/*" multiple required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="offer" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-tag mr-2"></i>Promotional Offer:
          </label>
          <input v-model="offer" type="text" id="offer" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="theme" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-paint-brush mr-2"></i>Theme:
          </label>
          <input v-model="theme" type="text" id="theme" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="colorPalette" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-palette mr-2"></i>Color Palette (comma-separated):
          </label>
          <input v-model="colorPalette" type="text" id="colorPalette" required
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <div class="form-group">
          <label for="generatorType" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-cog mr-2"></i>Image Generation Model:
          </label>
          <select v-model="generatorType" id="generatorType" required
                  class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
            <option value="imagen">Google Imagen</option>
            <option value="huggingface">Hugging Face</option>
          </select>
        </div>
        <div class="form-group">
          <label for="size" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-expand-arrows-alt mr-2"></i>Size (optional, e.g., 1200x628):
          </label>
          <input v-model="size" type="text" id="size" placeholder="1200x628"
                 class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
        </div>
        <button type="submit" :disabled="isLoading"
                class="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg py-3 px-4 font-bold text-lg hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300 transform hover:scale-105 flex items-center justify-center">
          <i class="fas fa-magic mr-2"></i>
          <span>{{ isLoading ? 'Generating...' : 'Generate Banner' }}</span>
          <div v-if="isLoading" class="loader ml-2"></div>
        </button>
      </form>
      <div v-if="result" class="mt-8 animate-fade-in">
        <img :src="result.image_path" alt="Generated Banner" class="w-full rounded-lg shadow-lg">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BannerGenerator',
  data() {
    return {
      files: [],
      offer: '',
      theme: '',
      colorPalette: '',
      generatorType: 'huggingface',
      size: '',
      format: 'PNG',
      result: null,
      isLoading: false
    }
  },
  methods: {
    onFileChange(e) {
      this.files = Array.from(e.target.files);
    },
    async generateBanner() {
      this.isLoading = true;
      const formData = new FormData();
      if (this.files.length === 0) {
        alert('Please select at least one product image.');
        this.isLoading = false;
        return;
      }
      this.files.forEach(file => {
        formData.append('productImages', file);
      });
      formData.append('offer', this.offer);
      formData.append('theme', this.theme);
      formData.append('colorPalette', this.colorPalette);
      formData.append('generatorType', this.generatorType);
      if (this.size) {
        formData.append('size', this.size);
      }
      formData.append('format', this.format);

      try {
        const response = await fetch('/generate_banner', {
          method: 'POST',
          body: formData
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        this.result = await response.json();
      } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while generating the banner.');
      } finally {
        this.isLoading = false;
      }
    }
  }
}
</script>

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
.banner-page-container {
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