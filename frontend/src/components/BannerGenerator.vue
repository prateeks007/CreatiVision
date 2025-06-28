<template>
  <div class="banner-page-container min-h-screen relative">
    <div class="banner-generator max-w-4xl mx-auto my-12 p-8 bg-white dark:bg-gray-800 rounded-xl shadow-2xl relative z-10">
      <div class="text-center mb-8">
        <h2 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
          AI Banner Generator
        </h2>
        <p class="text-xl text-gray-300 mt-2">Create stunning banners with the power of AI</p>
      </div>

      <!-- Upload error message -->
      <p v-if="uploadError" class="text-center text-red-500 font-semibold mb-4">
        ❌ {{ uploadError }}
      </p>

      <form @submit.prevent="generateBanner" class="space-y-6">
        <!-- File Upload -->
        <div class="form-group">
          <label for="productImages" class="block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-images mr-2"></i>Product Images:
          </label>
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
          <label for="offer" class="block text-lg text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-tag mr-2"></i>Promotional Offer:
          </label>
          <input
            v-model="offer"
            type="text"
            id="offer"
            required
            class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2"
          />
        </div>

        <!-- Theme -->
        <div class="form-group">
          <label for="theme" class="block text-lg text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-paint-brush mr-2"></i>Theme:
          </label>
          <input
            v-model="theme"
            type="text"
            id="theme"
            required
            class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2"
          />
        </div>

        <!-- Color Palette -->
        <div class="form-group">
          <label for="colorPalette" class="block text-lg text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-palette mr-2"></i>Color Palette:
          </label>
          <input
            v-model="colorPalette"
            type="text"
            id="colorPalette"
            required
            class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2"
          />
        </div>

        <!-- Generator Type -->
        <div class="form-group">
          <label for="generatorType" class="block text-lg text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-cog mr-2"></i>Image Generation Model:
          </label>
          <select
            v-model="generatorType"
            id="generatorType"
            required
            class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2"
          >
            <option value="imagen">Google Imagen</option>
            <option value="huggingface">Hugging Face</option>
          </select>
        </div>

        <!-- Size -->
        <div class="form-group">
          <label for="size" class="block text-lg text-gray-700 dark:text-gray-300 mb-2">
            <i class="fas fa-expand-arrows-alt mr-2"></i>Size (optional):
          </label>
          <input
            v-model="size"
            type="text"
            id="size"
            placeholder="1200x628"
            class="w-full px-4 py-3 bg-gray-100 dark:bg-gray-700 border rounded-lg focus:ring-2"
          />
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="isLoading"
          class="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white py-3 rounded-lg font-bold hover:scale-105 transition"
        >
          <i class="fas fa-magic mr-2"></i>
          <span>{{ isLoading ? "Generating..." : "Generate Banner" }}</span>
        </button>
      </form>

      <!-- Result Display -->
      <div v-if="result" class="mt-8 space-y-4">
        <!-- Main Error -->
        <div v-if="result.error" class="bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-100 p-4 rounded border border-red-400">
          <p class="font-bold text-lg">❌ Banner Generation Failed</p>
          <p class="mt-1 text-sm">{{ result.error }}</p>
        </div>

        <!-- Prompt -->
        <div v-if="result.prompt" class="bg-gray-800 text-gray-300 p-3 rounded">
          <p class="text-sm italic text-center">📝 Prompt Used: "{{ result.prompt }}"</p>
        </div>

        <!-- Fallback Used -->
        <div v-if="result.fallback_used" class="text-yellow-400 font-semibold text-center">
          ⚠️ Fallback was used due to failures in all image providers.
        </div>

        <!-- Warnings -->
        <div v-if="result.warnings?.length" class="bg-yellow-100 dark:bg-yellow-800 text-yellow-900 dark:text-yellow-100 p-4 rounded border border-yellow-400">
          <p class="font-bold mb-2">⚠️ Warnings</p>
          <ul class="list-disc list-inside space-y-1 text-sm">
            <li v-for="(warn, i) in result.warnings" :key="i">{{ warn }}</li>
          </ul>
        </div>

        <!-- Raw Debug Info -->
        <pre v-if="result.details" class="text-xs bg-black text-red-400 p-3 rounded overflow-auto whitespace-pre-wrap">
{{ result.details }}
        </pre>

        <!-- Image Display -->
        <div v-if="result.image_path">
          <img :src="result.image_path" alt="Generated Banner" class="w-full rounded-lg shadow-lg mb-4" />
          <div class="text-center">
            <a
              :href="result.image_path"
              download="generated_banner.png"
              class="bg-gradient-to-r from-blue-500 to-purple-600 text-white py-3 px-6 rounded-lg font-bold hover:scale-105 transition"
            >
              <i class="fas fa-download mr-2"></i>Download Banner
            </a>
          </div>
        </div>

        <p v-else-if="!result.image_path && !result.error" class="text-center text-gray-400 italic">
          (No image was generated.)
        </p>
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
      uploadError: null,
    };
  },
  methods: {
    onFileChange(e) {
      const files = Array.from(e.target.files);
      const valid = files.filter(f => ["image/png", "image/jpeg"].includes(f.type));
      if (valid.length !== files.length) {
        this.uploadError = "Only PNG or JPG files are allowed.";
        e.target.value = "";
        this.files = [];
      } else {
        this.uploadError = null;
        this.files = valid;
      }
    },
    async generateBanner() {
      this.isLoading = true;
      this.result = null;

      const form = new FormData();
      this.files.forEach(f => form.append("productImages", f));
      form.append("offer", this.offer);
      form.append("theme", this.theme);
      form.append("colorPalette", this.colorPalette);
      form.append("generatorType", this.generatorType);
      if (this.size) form.append("size", this.size);
      form.append("format", this.format);

      try {
        const res = await fetch("/generate_banner", { method: "POST", body: form });
        let data;
        try {
          data = await res.json();
        } catch (e) {
          data = { error: "Server returned invalid JSON." };
        }
        this.result = data;
      } catch (err) {
        console.error("Request failed", err);
        this.result = { error: "Network error — please check your connection." };
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
</style>
