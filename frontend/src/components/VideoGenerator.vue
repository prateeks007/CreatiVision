<template>
  <div class="video-generator">
    <h2>AI Video Generator</h2>
    <form @submit.prevent="generateVideo" class="generator-form">
      <div class="form-group">
        <label for="productImage">Product Image:</label>
        <input type="file" id="productImage" @change="onFileChange" accept="image/*" required>
      </div>
      <div class="form-group">
        <label for="offer">Promotional Offer:</label>
        <input v-model="offer" type="text" id="offer" required>
      </div>
      <div class="form-group">
        <label for="theme">Theme:</label>
        <input v-model="theme" type="text" id="theme" required>
      </div>
      <div class="form-group">
        <label for="colorPalette">Color Palette (comma-separated):</label>
        <input v-model="colorPalette" type="text" id="colorPalette" required>
      </div>
      <div class="form-group">
        <label for="size">Size (e.g., 1200x628):</label>
        <input v-model="size" type="text" id="size" required>
      </div>
      <div class="form-group">
        <label for="duration">Duration (seconds):</label>
        <input v-model="duration" type="number" id="duration" required>
      </div>
      <button type="submit" :disabled="isLoading">Generate Video</button>
    </form>
    <div v-if="isLoading" class="loader">Generating video...</div>
    <div v-if="result" class="result">
      <video controls :src="result.video_path"></video>
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