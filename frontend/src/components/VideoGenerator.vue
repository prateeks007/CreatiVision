<template>
  <div class="video-generator container mx-auto p-4 bg-white dark:bg-gray-800 rounded-lg shadow-md">
    <h2 class="text-xl font-bold text-blue-600 dark:text-blue-400">AI Video Generator</h2>
    <form @submit.prevent="generateVideo" class="generator-form space-y-4">
      <div class="form-group">
        <label for="productImage" class="font-semibold dark:text-gray-300">Product Image:</label>
        <input type="file" id="productImage" @change="onFileChange" accept="image/*" required class="border rounded p-2 w-full dark:bg-gray-700 dark:text-gray-300">
      </div>
      <div class="form-group">
        <label for="offer" class="font-semibold dark:text-gray-300">Promotional Offer:</label>
        <input v-model="offer" type="text" id="offer" required class="border rounded p-2 w-full dark:bg-gray-700 dark:text-gray-300">
      </div>
      <div class="form-group">
        <label for="theme" class="font-semibold dark:text-gray-300">Theme:</label>
        <input v-model="theme" type="text" id="theme" required class="border rounded p-2 w-full dark:bg-gray-700 dark:text-gray-300">
      </div>
      <div class="form-group">
        <label for="colorPalette" class="font-semibold dark:text-gray-300">Color Palette (comma-separated):</label>
        <input v-model="colorPalette" type="text" id="colorPalette" required class="border rounded p-2 w-full dark:bg-gray-700 dark:text-gray-300">
      </div>
      <div class="form-group">
        <label for="size" class="font-semibold dark:text-gray-300">Size (e.g., 1200x628):</label>
        <input v-model="size" type="text" id="size" required class="border rounded p-2 w-full dark:bg-gray-700 dark:text-gray-300">
      </div>
      <div class="form-group">
        <label for="duration" class="font-semibold dark:text-gray-300">Duration (seconds):</label>
        <input v-model="duration" type="number" id="duration" required class="border rounded p-2 w-full dark:bg-gray-700 dark:text-gray-300">
      </div>
      <button type="submit" :disabled="isLoading" class="bg-blue-600 text-white rounded p-2 hover:bg-blue-700 transition">Generate Video</button>
    </form>
    <div v-if="isLoading" class="mt-4 text-gray-600 dark:text-gray-400">Generating video...</div>
    <div v-if="result" class="result mt-4 text-center">
      <video :src="result.video_path" controls class="max-w-full rounded shadow"></video>
      <p class="mt-2 dark:text-gray-300"><strong>Generated Prompt:</strong> {{ result.prompt }}</p>
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
/* Use the same styles as in BannerGenerator.vue */
</style>