<template>
  <div class="banner-generator p-8 backdrop-filter backdrop-blur-sm rounded-xl">
    <h2 class="text-3xl font-bold text-blue-300 mb-8 text-center">AI Banner Generator</h2>
    <form @submit.prevent="generateBanner" class="space-y-6 max-w-md mx-auto">
      <div class="form-group">
        <label for="productImages" class="block text-lg font-medium text-blue-200 mb-2">Product Images:</label>
        <input type="file" id="productImages" @change="onFileChange" accept="image/*" multiple required
               class="w-full px-4 py-3 text-gray-200 bg-opacity-20 bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="offer" class="block text-lg font-medium text-blue-200 mb-2">Promotional Offer:</label>
        <input v-model="offer" type="text" id="offer" required
               class="w-full px-4 py-3 text-gray-200 bg-opacity-20 bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="theme" class="block text-lg font-medium text-blue-200 mb-2">Theme:</label>
        <input v-model="theme" type="text" id="theme" required
               class="w-full px-4 py-3 text-gray-200 bg-opacity-20 bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="colorPalette" class="block text-lg font-medium text-blue-200 mb-2">Color Palette (comma-separated):</label>
        <input v-model="colorPalette" type="text" id="colorPalette" required
               class="w-full px-4 py-3 text-gray-200 bg-opacity-20 bg-gray-700 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300">
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
      <p class="mt-4 text-lg text-blue-200"><strong>Generated Prompt:</strong> {{ result.prompt }}</p>
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
</style>