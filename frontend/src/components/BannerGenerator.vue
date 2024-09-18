<template>
  <div class="banner-generator container">
    <h2>AI Banner Generator</h2>
    <form @submit.prevent="generateBanner" class="generator-form">
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
      <button type="submit" :disabled="isLoading">Generate Banner</button>
    </form>
    <div v-if="isLoading" class="loader">Generating banner...</div>
    <div v-if="result" class="result">
      <img :src="result.image_path" alt="Generated Banner">
      <p><strong>Generated Prompt:</strong> {{ result.prompt }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BannerGenerator',
  data() {
    return {
      file: null,
      offer: '',
      theme: '',
      colorPalette: '',
      result: null,
      isLoading: false
    }
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0]
    },
    async generateBanner() {
      this.isLoading = true;
      const formData = new FormData()
      formData.append('productImage', this.file)
      formData.append('offer', this.offer)
      formData.append('theme', this.theme)
      formData.append('colorPalette', this.colorPalette)

      try {
        const response = await fetch('/generate_banner', {
          method: 'POST',
          body: formData
        })
        this.result = await response.json()
      } catch (error) {
        console.error('Error:', error)
        alert('An error occurred while generating the banner.')
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style scoped>
.banner-generator {
  max-width: 600px;
  margin: 0 auto;
}

h2 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
}

.generator-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

label {
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: var(--text-color);
}

input[type="text"],
input[type="file"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input[type="text"]:focus,
input[type="file"]:focus {
  border-color: var(--primary-color);
  outline: none;
}

button {
  align-self: flex-start;
  margin-top: 1rem;
}

.loader {
  margin-top: 1rem;
  font-style: italic;
  color: var(--text-color);
}

.result {
  margin-top: 2rem;
  text-align: center;
}

.result img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.result p {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: var(--text-color);
}
</style>