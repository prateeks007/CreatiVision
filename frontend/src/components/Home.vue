<template>
  <div class="home">
    <section
      class="hero bg-gradient-to-r from-blue-500 to-purple-600 text-white py-24 rounded-lg mb-16 relative overflow-hidden"
    >
      <canvas
        id="hero-canvas"
        class="absolute top-0 left-0 w-full h-full"
      ></canvas>
      <div class="container mx-auto text-center px-4 relative z-10">
        <h1 class="text-5xl md:text-6xl font-bold mb-6 animate-fade-in">
          Welcome to CreatiVision
        </h1>
        <p
          class="text-xl md:text-2xl mb-10 animate-fade-in-delay max-w-2xl mx-auto"
        >
          Create stunning banners and videos with the power of AI.
        </p>
        <a
          href="#features"
          class="bg-white text-blue-600 px-8 py-3 rounded-full font-bold text-lg hover:bg-blue-100 transition duration-300 shadow-md"
          >Get Started</a
        >
      </div>
    </section>

    <section
      id="features"
      data-aos="fade-up"
      data-aos-duration="1000"
      class="mb-16 bg-white bg-opacity-90 dark:bg-gray-800 dark:bg-opacity-90 rounded-lg p-8"
    >
      <div class="container mx-auto px-4">
        <h2
          class="text-3xl md:text-4xl font-bold text-center mb-12 text-gray-800 dark:text-white"
        >
          Our Features
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
          <div
            class="feature-card bg-white dark:bg-gray-800 rounded-lg shadow-md p-8 transition duration-300 hover:shadow-xl transform hover:-translate-y-2"
          >
            <div class="text-4xl mb-6 text-blue-500 animate-bounce">🎨</div>
            <h3
              class="text-2xl font-semibold mb-4 text-gray-800 dark:text-white"
            >
              Banner Generator
            </h3>
            <p class="text-gray-600 dark:text-gray-300 mb-6">
              Create eye-catching banners for your marketing campaigns with
              ease.
            </p>
            <router-link
              to="/banner"
              class="btn-primary bg-blue-500 text-white font-bold py-2 px-4 rounded"
            >
              Try Now
            </router-link>
          </div>
          <div
            class="feature-card bg-white dark:bg-gray-800 rounded-lg shadow-md p-8 transition duration-300 hover:shadow-xl transform hover:-translate-y-2"
          >
            <div class="text-4xl mb-6 text-purple-500 animate-pulse">🎥</div>
            <h3
              class="text-2xl font-semibold mb-4 text-gray-800 dark:text-white"
            >
              Video Generator
            </h3>
            <p class="text-gray-600 dark:text-gray-300 mb-6">
              Generate engaging videos to promote your products or services
              effortlessly.
            </p>
            <router-link
              to="/video"
              class="btn-primary bg-purple-500 text-white font-bold py-2 px-4 rounded"
            >
              Try Now
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <section
      class="bg-gray-100 dark:bg-gray-700 bg-opacity-90 dark:bg-opacity-90 py-16 rounded-lg"
    >
      <div class="container mx-auto px-4">
        <h2
          class="text-3xl md:text-4xl font-bold text-center mb-12 text-gray-800 dark:text-white"
        >
          What Our Users Say
        </h2>
        <div class="relative">
          <div class="testimonials-container">
            <div ref="testimonialsWrapper" class="testimonials-wrapper">
              <div
                v-for="testimonial in testimonials"
                :key="testimonial.id"
                class="testimonial-card bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm transition-all duration-300 hover:shadow-lg transform hover:-translate-y-1"
              >
                <p class="text-gray-600 dark:text-gray-300 mb-4">
                  {{ testimonial.comment }}
                </p>
                <div class="flex items-center">
                  <img
                    :src="testimonial.avatar"
                    :alt="testimonial.name"
                    class="w-12 h-12 rounded-full mr-4"
                  />
                  <div>
                    <p class="font-semibold text-gray-800 dark:text-white">
                      {{ testimonial.name }}
                    </p>
                    <p class="text-sm text-gray-600 dark:text-gray-400">
                      {{ testimonial.title }}
                    </p>
                  </div>
                </div>
                <div class="flex mt-2">
                  <span
                    v-for="star in 5"
                    :key="star"
                    class="text-yellow-400 text-xl"
                  >
                    {{ star <= testimonial.rating ? "★" : "☆" }}
                  </span>
                </div>
              </div>
            </div>
          </div>
          <button
            @click="scrollTestimonials('left')"
            class="testimonial-arrow left-arrow"
            aria-label="Previous testimonial"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 19l-7-7 7-7"
              />
            </svg>
          </button>
          <button
            @click="scrollTestimonials('right')"
            class="testimonial-arrow right-arrow"
            aria-label="Next testimonial"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";

export default {
  name: "HomePage",
  setup() {
    const testimonials = ref([
      {
        id: 1,
        name: "Aman kumar",
        title: "Marketing Manager",
        comment:
          "With CreatiVision, we've seen a significant improvement in our ad performance. The videos it creates are vibrant, attention-grabbing, and perfectly tailored for our target audience. Highly recommend!",
        rating: 4,
        avatar: "/static/images/avatars/aman-avatar.png",
      },
      {
        id: 2,
        name: "Mohammed Zaid Sikander",
        title: "Small Business Owner",
        comment:
          "I can't believe how easy it is to create professional-looking banners and videos. Highly recommended!",
        rating: 4,
        avatar: "/static/images/avatars/zaid-avatar.png",
      },
      {
        id: 3,
        name: "KS Sohan",
        title: "Freelance Designer",
        comment:
          "The time we save using CreatiVision is incredible. It's like having a design team at your fingertips.",
        rating: 5,
        avatar: "/static/images/avatars/sohan-avatar.png",
      },
      {
        id: 4,
        name: "Arun Patil",
        title: "E-commerce Entrepreneur",
        comment:
          "CreatiVision has revolutionized our product marketing. The AI-generated content is decent and saves a lot of time.",
        rating: 4.5,
        avatar: "/static/images/avatars/arun-avatar.png",
      },
      {
        id: 5,
        name: "Dheeraj Sudarshan",
        title: "Social Media Influencer",
        comment:
          "As an influencer, I need to create content quickly. CreatiVision is my secret weapon for eye-catching visuals for my collabs with brands",
        rating: 4,
        avatar: "/static/images/avatars/dheeraj-avatar.png",
      },
    ]);

    const testimonialsWrapper = ref(null);

    const scrollTestimonials = (direction) => {
      const wrapper = testimonialsWrapper.value;
      const scrollAmount = wrapper.offsetWidth;
      const maxScroll = wrapper.scrollWidth - wrapper.offsetWidth;

      if (direction === "left") {
        wrapper.scrollLeft = Math.max(0, wrapper.scrollLeft - scrollAmount);
      } else {
        wrapper.scrollLeft = Math.min(
          maxScroll,
          wrapper.scrollLeft + scrollAmount
        );
      }
    };

    onMounted(() => {
      initHeroAnimation();
    });

    const initHeroAnimation = () => {
      const canvas = document.getElementById("hero-canvas");
      const ctx = canvas.getContext("2d");
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;

      const particles = [];
      const particleCount = 100;
      const colors = ["#ffffff", "#88ccff", "#ff88cc"];

      for (let i = 0; i < particleCount; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          radius: Math.random() * 3 + 1,
          color: colors[Math.floor(Math.random() * colors.length)],
          speedX: Math.random() * 3 - 1.5,
          speedY: Math.random() * 3 - 1.5,
        });
      }

      function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach((particle) => {
          particle.x += particle.speedX;
          particle.y += particle.speedY;

          if (particle.x < 0 || particle.x > canvas.width)
            particle.speedX *= -1;
          if (particle.y < 0 || particle.y > canvas.height)
            particle.speedY *= -1;

          ctx.beginPath();
          ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
          ctx.fillStyle = particle.color;
          ctx.fill();
        });
      }

      animate();

      window.addEventListener("resize", () => {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
      });
    };

    return {
      testimonials,
      testimonialsWrapper,
      scrollTestimonials,
    };
  },
};
</script>

<style scoped>
@keyframes bounce {
  0%,
  100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}

@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.feature-card {
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-10px);
}

.btn-primary {
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: rgba(59, 130, 246, 0.8);
}

.testimonial-carousel {
  /* Add styles for the carousel container */
}

.testimonial-item {
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.testimonial-item.active {
  opacity: 1;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.testimonial-item {
  animation: fadeIn 1s ease-in-out;
}

.hero {
  position: relative;
}

#hero-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.hero .container {
  position: relative;
  z-index: 2;
}

.testimonials-container {
  position: relative;
  overflow: hidden;
  padding: 0 40px;
}

.testimonials-wrapper {
  display: flex;
  transition: transform 0.5s ease;
  scroll-behavior: smooth;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.testimonials-wrapper::-webkit-scrollbar {
  display: none;
}

.testimonial-card {
  flex: 0 0 calc(33.333% - 20px);
  margin: 0 10px;
  scroll-snap-align: start;
}

.testimonial-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  z-index: 10;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.testimonial-arrow:hover {
  background-color: rgba(255, 255, 255, 1);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.testimonial-arrow:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5);
}

.testimonial-arrow svg {
  width: 24px;
  height: 24px;
  color: #4a5568;
  transition: color 0.3s ease;
}

.testimonial-arrow:hover svg {
  color: #2d3748;
}

.left-arrow {
  left: -24px;
}

.right-arrow {
  right: -24px;
}

/* Dark mode styles */
.dark .testimonial-arrow {
  background-color: rgba(45, 55, 72, 0.9);
}

.dark .testimonial-arrow:hover {
  background-color: rgba(45, 55, 72, 1);
}

.dark .testimonial-arrow svg {
  color: #a0aec0;
}

.dark .testimonial-arrow:hover svg {
  color: #e2e8f0;
}

@media (prefers-color-scheme: dark) {
  .testimonial-arrow {
    background-color: rgba(45, 55, 72, 0.9);
  }

  .testimonial-arrow:hover {
    background-color: rgba(45, 55, 72, 1);
  }

  .testimonial-arrow svg {
    color: #a0aec0;
  }

  .testimonial-arrow:hover svg {
    color: #e2e8f0;
  }
}

@media (max-width: 768px) {
  .testimonial-card {
    flex: 0 0 calc(100% - 20px);
  }

  .left-arrow {
    left: 0;
  }

  .right-arrow {
    right: 0;
  }
}
</style>
