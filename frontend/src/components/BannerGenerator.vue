<template>
  <div class="banner-page-container min-h-screen relative">
    <div class="banner-generator max-w-4xl mx-auto my-12 p-8 bg-white dark:bg-gray-800 rounded-xl shadow-2xl relative z-10">
      <div class="text-center mb-8">
        <h2 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
          AI Banner Generator
        </h2>
        <p class="text-xl text-gray-300 mt-2">Create stunning banners with the power of AI</p>
      </div>

      <form @submit.prevent="generateBanner" class="space-y-6">
        <!-- File Upload -->
        <div class="form-group">
          <label for="productImages" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-images mr-2"></i>Product Images:
          </label>
          <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">
            <i class="fas fa-info-circle mr-1"></i>Only PNG or JPG files are allowed.
          </p>
          <input
            type="file"
            id="productImages"
            @change="onFileChange"
            accept=".png, .jpg, .jpeg"
            multiple
            required
            class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2"
          />
        </div>

        <!-- Offer -->
        <div class="form-group">
          <label for="offer" class="block text-lg text-gray-700 dark:text-gray-300 mb-2"><i class="fas fa-tag mr-2"></i>Promotional Offer:</label>
          <input v-model="offer" type="text" id="offer" required class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2" />
        </div>

        <!-- Theme -->
        <div class="form-group">
          <label for="theme" class="block text-lg text-gray-700 dark:text-gray-300 mb-2"><i class="fas fa-paint-brush mr-2"></i>Theme:</label>
          <input v-model="theme" type="text" id="theme" required class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2" />
        </div>

        <!-- Palette -->
        <div class="form-group">
          <label for="colorPalette" class="block text-lg text-gray-700 dark:text-gray-300 mb-2"><i class="fas fa-palette mr-2"></i>Color Palette:</label>
          <input v-model="colorPalette" type="text" id="colorPalette" required class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2" />
        </div>

        <!-- Generator -->
        <div class="form-group">
          <label for="generatorType" class="block text-lg text-gray-700 dark:text-gray-300 mb-2"><i class="fas fa-cog mr-2"></i>Image Generation Model:</label>
          <select v-model="generatorType" id="generatorType" required class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2">
            <option value="imagen">Google Imagen</option>
            <option value="huggingface">Hugging Face</option>
          </select>
        </div>

        <!-- Size -->
        <div class="form-group">
          <label for="size" class="block text-lg text-gray-700 dark:text-gray-300 mb-2"><i class="fas fa-expand-arrows-alt mr-2"></i>Size (optional):</label>
          <input v-model="size" type="text" id="size" placeholder="1200x628" class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2" />
        </div>

        <!-- Button -->
        <button type="submit" :disabled="isLoading" class="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white py-3 rounded-lg font-bold hover:scale-105 transition">
          <i class="fas fa-magic mr-2"></i><span>{{ isLoading ? "Generating..." : "Generate Banner" }}</span>
        </button>
      </form>

      <!-- Results -->
      <div v-if="result" class="mt-8 animate-fade-in">
        <img :src="result.image_path" alt="Generated Banner" class="w-full rounded-lg shadow-lg mb-4" />
        
        <!-- Warnings and fallback -->
        <div v-if="result.fallback_used || result.warnings?.length" class="text-center text-yellow-400 font-semibold mb-4">
          <div v-if="result.fallback_used">⚠️ No image analysis providers worked. A default caption was used.</div>
          <div v-for="(warn, idx) in result.warnings" :key="idx">⚠️ {{ warn }}</div>
        </div>

        <!-- Download -->
        <div class="flex justify-center">
          <a :href="result.image_path" download="generated_banner.png" class="bg-gradient-to-r from-blue-500 to-purple-600 text-white py-3 px-6 rounded-lg font-bold hover:scale-105 transition">
            <i class="fas fa-download mr-2"></i>Download Banner
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BannerGenerator",
  data() {
    return {
      files: [],
      offer: "",
      theme: "",
      colorPalette: "",
      generatorType: "imagen",
      size: "",
      format: "PNG",
      result: null,
      isLoading: false,
    };
  },
  methods: {
    onFileChange(e) {
      const files = Array.from(e.target.files);
      const validFiles = files.filter((file) =>
        ["image/png", "image/jpeg"].includes(file.type)
      );

      if (validFiles.length !== files.length) {
        alert("Only PNG or JPG files are allowed.");
        e.target.value = "";
      } else {
        this.files = validFiles;
      }
    },
    async generateBanner() {
      this.isLoading = true;
      const formData = new FormData();

      if (this.files.length === 0) {
        alert("Please select at least one image.");
        this.isLoading = false;
        return;
      }

      this.files.forEach((file) => formData.append("productImages", file));
      formData.append("offer", this.offer);
      formData.append("theme", this.theme);
      formData.append("colorPalette", this.colorPalette);
      formData.append("generatorType", this.generatorType);
      if (this.size) formData.append("size", this.size);
      formData.append("format", this.format);

      try {
        const res = await fetch("/generate_banner", {
          method: "POST",
          body: formData,
        });

        const data = await res.json();
        this.result = data;
      } catch (err) {
        console.error(err);
        alert("Error generating banner.");
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>

<style scoped>
.banner-page-container {
  background: linear-gradient(135deg, #e0f2fe, #fae8ff, #f0fdf4, #fae8ff);
  background-size: 400% 400%;
  animation: gradientAnimation 20s ease infinite;
}

@keyframes gradientAnimation {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>
