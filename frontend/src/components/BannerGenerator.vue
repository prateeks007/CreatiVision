<template>
  <div class="banner-generator p-8 backdrop-filter backdrop-blur-sm rounded-xl">
    <h2 class="text-3xl font-bold text-blue-300 mb-8 text-center">AI Banner Generator</h2>
    <form @submit.prevent="generateBanner" class="space-y-6 max-w-md mx-auto">
      <div class="form-group">
        <label for="productImages" class="block text-lg font-medium text-blue-200 mb-2">Product Images:</label>
        <input type="file" id="productImages" @change="onFileChange" accept="image/*" multiple required
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
        <label for="generatorType" class="block text-lg font-medium text-blue-200 mb-2">Image Generation Model:</label>
        <div class="relative">
          <select v-model="generatorType" id="generatorType" required
                  class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300 appearance-none custom-select">
            <option value="huggingface">Hugging Face</option>
            <option value="imagen">Google Imagen</option>
          </select>
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-200">
            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M7 10l5 5 5-5H7z"/></svg>
          </div>
        </div>
      </div>
      <div class="form-group">
        <label for="size" class="block text-lg font-medium text-blue-200 mb-2">Size (optional, e.g., 1200x628):</label>
        <input v-model="size" type="text" id="size" placeholder="1200x628"
               class="w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-opacity-20 dark:bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <button type="submit" :disabled="isLoading"
              class="w-full bg-blue-600 text-white rounded-full py-3 px-6 font-bold text-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300 transform hover:scale-105">
        {{ isLoading ? 'Generating...' : 'Generate Banner' }}
      </button>
    </form>
    <div v-if="isLoading" class="mt-8">
      <div class="loader"></div>
    </div>
    <div v-if="result" class="result mt-8 animate-fade-in">
      <img :src="result.image_path" alt="Generated Banner" class="w-full rounded-lg shadow-lg">
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

<style scoped>
.banner-generator {
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
  content: 'Select files';
  display: inline-block;
  background: var(--color-primary);
  color: var(--color-on-primary);
  /* ... other styles ... */
}

input[type="file"]:hover::before {
  background: var(--color-secondary);
}

input[type="file"]:active::before {
  background: var(--color-primary);
}

/* Custom styles for the dropdown */
.custom-select {
  background-color: var(--color-surface);
  color: var(--color-text);
  border-radius: 0.5rem;
  padding-right: 2.5rem;
}

.custom-select option {
  background-color: var(--color-surface);
  color: var(--color-text);
}

/* Ensure the selected option text is visible */
.custom-select:focus {
  color: var(--color-text);
}

/* Custom styles for the dropdown options */
.custom-select option {
  background-color: var(--color-surface);
  color: var(--color-text);
}

.custom-select option:hover {
  background-color: var(--color-primary);
  color: var(--color-on-primary);
}

/* Ensure the selected option text is visible */
.custom-select option:checked {
  background-color: var(--color-primary);
  color: var(--color-on-primary);
}

/* Additional styles to ensure visibility */
.custom-select option {
  background-color: var(--color-surface);
  color: var(--color-text);
}

.custom-select option:hover {
  background-color: var(--color-primary);
  color: var(--color-on-primary);
}

.custom-select option:checked {
  background-color: var(--color-primary);
  color: var(--color-on-primary);
}

/* Ensure the selected option text is visible */
.custom-select option[selected] {
  background-color: var(--color-primary);
  color: var(--color-on-primary);
}
</style>