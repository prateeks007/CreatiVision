<template>
  <div class="home container mx-auto p-8 text-center">
    <h2 class="text-5xl font-bold mb-4 text-gradient">Welcome to AI Content Generator</h2>
    <p class="text-xl mb-12 text-text-light">Create stunning banners and videos with the power of AI.</p>
    <div class="features grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="feature bg-surface bg-opacity-80 rounded-lg p-8 shadow-lg backdrop-filter backdrop-blur-sm transition-all duration-300 hover:shadow-xl">
        <h3 class="text-2xl font-semibold text-primary mb-4">Banner Generator</h3>
        <p class="text-text-light mb-6">Create eye-catching banners for your marketing campaigns.</p>
        <router-link to="/banner" class="btn-primary">Get Started</router-link>
      </div>
      <div class="feature bg-surface bg-opacity-80 rounded-lg p-8 shadow-lg backdrop-filter backdrop-blur-sm transition-all duration-300 hover:shadow-xl">
        <h3 class="text-2xl font-semibold text-primary mb-4">Video Generator</h3>
        <p class="text-text-light mb-6">Generate engaging videos to promote your products or services.</p>
        <router-link to="/video" class="btn-primary">Get Started</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
.text-gradient {
  background: linear-gradient(45deg, var(--color-primary), var(--color-secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.btn-primary {
  @apply inline-block bg-primary text-white rounded-full py-2 px-6 font-semibold transition-all duration-300;
}

.btn-primary:hover {
  @apply bg-secondary shadow-lg;
}
</style>
