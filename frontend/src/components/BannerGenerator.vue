<template>
  <div class="banner-generator max-w-3xl mx-auto bg-gray-900 shadow-lg rounded-lg overflow-hidden my-8">
    <div class="bg-gradient-to-r from-blue-500 to-purple-600 p-8 text-white">
      <h2 class="text-4xl font-bold mb-2">AI Banner Generator</h2>
      <p class="text-xl">Create stunning banners with the power of AI</p>
    </div>
    <form @submit.prevent="generateBanner" class="p-10 space-y-6">
      <div class="form-group">
        <label for="productImages" class="block text-lg font-medium text-blue-200 mb-2">Product Images:</label>
        <input type="file" id="productImages" @change="onFileChange" accept="image/*" multiple required
               class="w-full px-4 py-3 text-gray-200 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="offer" class="block text-lg font-medium text-blue-200 mb-2">Promotional Offer:</label>
        <input v-model="offer" type="text" id="offer" required
               class="w-full px-4 py-3 text-gray-200 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="theme" class="block text-lg font-medium text-blue-200 mb-2">Theme:</label>
        <input v-model="theme" type="text" id="theme" required
               class="w-full px-4 py-3 text-gray-200 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="colorPalette" class="block text-lg font-medium text-blue-200 mb-2">Color Palette (comma-separated):</label>
        <input v-model="colorPalette" type="text" id="colorPalette" required
               class="w-full px-4 py-3 text-gray-200 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
      </div>
      <div class="form-group">
        <label for="generatorType" class="block text-lg font-medium text-blue-200 mb-2">Image Generation Model:</label>
        <select v-model="generatorType" id="generatorType" required
                class="w-full px-4 py-3 text-gray-200 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
          <option value="huggingface">Hugging Face</option>
          <option value="imagen">Google Imagen</option>
        </select>
      </div>
      <div class="form-group">
        <label for="size" class="block text-lg font-medium text-blue-200 mb-2">Size (optional, e.g., 1200x628):</label>
        <input v-model="size" type="text" id="size" placeholder="1200x628"
               class="w-full px-4 py-3 text-gray-200 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300">
      </div>
      <button type="submit" :disabled="isLoading"
              class="w-full bg-blue-600 text-white rounded-lg py-3 px-4 font-bold text-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300">
        {{ isLoading ? 'Generating...' : 'Generate Banner' }}
      </button>
    </form>
    <div v-if="isLoading" class="flex justify-center items-center p-8">
      <div class="loader"></div>
    </div>
    <div v-if="result" class="p-6">
      <img :src="result.image_path" alt="Generated Banner" class="w-full rounded-lg shadow-lg">
      <!-- <p class="mt-4 text-blue-200"><strong>Generated Prompt:</strong> {{ result.prompt }}</p> -->
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

.flex {
  display: flex;
}

.justify-center {
  justify-content: center;
}

.items-center {
  align-items: center;
}
</style>