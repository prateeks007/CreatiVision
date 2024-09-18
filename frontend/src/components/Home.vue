<template>
  <div class="home container">
    <h2>Welcome to AI Content Generator</h2>
    <p>Create stunning banners and videos with the power of AI.</p>
    <div class="features">
      <div class="feature">
        <h3>Banner Generator</h3>
        <p>Create eye-catching banners for your marketing campaigns.</p>
        <router-link to="/banner" class="btn">Get Started</router-link>
      </div>
      <div class="feature">
        <h3>Video Generator</h3>
        <p>Generate engaging videos to promote your products or services.</p>
        <router-link to="/video" class="btn">Get Started</router-link>
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
.home {
  text-align: center;
}

h2 {
  color: var(--primary-color);
  margin-bottom: 1rem;
}

p {
  color: var(--text-color);
}

.features {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 2rem;
}

.feature {
  flex-basis: calc(50% - 1rem);
  padding: 1.5rem;
  background-color: var(--container-bg);
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  margin-bottom: 1rem;
}

.feature:hover {
  transform: translateY(-5px);
}

h3 {
  color: var(--secondary-color);
}

.feature p {
  color: var(--text-color);
}

.btn {
  display: inline-block;
  background-color: var(--secondary-color);
  color: var(--header-color);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  margin-top: 1rem;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: var(--primary-color);
}

@media (max-width: 768px) {
  .feature {
    flex-basis: 100%;
  }
}
</style>
