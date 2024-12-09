<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500"
  >
    <div class="auth-container max-w-md w-full mx-4">
      <div
        v-if="errorMessage"
        class="mb-4 p-4 rounded-lg bg-red-100 border border-red-400 text-red-700 relative animate-fade-in"
        role="alert"
      >
        <strong class="font-bold">Error: </strong>
        <span class="block sm:inline">{{ errorMessage }}</span>
        <button
          @click="errorMessage = ''"
          class="absolute top-0 right-0 px-4 py-3"
        >
          <span class="sr-only">Close</span>
          <i class="fas fa-times"></i>
        </button>
      </div>

      <div
        class="bg-white dark:bg-gray-800 rounded-2xl shadow-2xl p-8 transform transition-all hover:scale-[1.02]"
      >
        <div v-if="!session" class="space-y-6">
          <div class="text-center">
            <h2
              class="text-3xl font-bold bg-gradient-to-r from-blue-500 to-purple-600 bg-clip-text text-transparent"
            >
              Welcome to CreatiVision
            </h2>
            <p class="mt-2 text-gray-600 dark:text-gray-400">
              Create stunning AI-powered content
            </p>
          </div>

          <div class="space-y-4">
            <div class="relative">
              <input
                type="email"
                v-model="email"
                placeholder="Email"
                class="w-full px-4 py-3 border-2 border-gray-200 dark:border-gray-600 rounded-xl focus:border-blue-500 dark:focus:border-blue-400 focus:outline-none transition-colors dark:bg-gray-700 dark:text-white"
              />
              <i
                class="fas fa-envelope absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400"
              ></i>
            </div>

            <div class="relative">
              <input
                :type="showPassword ? 'text' : 'password'"
                v-model="password"
                placeholder="Password"
                class="w-full px-4 py-3 border-2 border-gray-200 dark:border-gray-600 rounded-xl focus:border-blue-500 dark:focus:border-blue-400 focus:outline-none transition-colors dark:bg-gray-700 dark:text-white"
              />
              <i
                :class="[
                  'fas',
                  showPassword ? 'fa-eye-slash' : 'fa-eye',
                  'absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400 cursor-pointer',
                ]"
                @click="showPassword = !showPassword"
              ></i>
            </div>
          </div>

          <div class="space-y-4">
            <button
              @click="handleSignIn"
              class="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white py-3 rounded-xl font-semibold transform transition-all hover:scale-[1.02] hover:shadow-lg"
            >
              Sign In
            </button>

            <div class="relative">
              <div class="absolute inset-0 flex items-center">
                <div
                  class="w-full border-t border-gray-300 dark:border-gray-600"
                ></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="px-2 bg-white dark:bg-gray-800 text-gray-500"
                  >or</span
                >
              </div>
            </div>

            <button
              @click="handleSignUp"
              class="w-full bg-white dark:bg-gray-700 text-gray-700 dark:text-white py-3 rounded-xl font-semibold border-2 border-gray-200 dark:border-gray-600 transform transition-all hover:scale-[1.02] hover:shadow-lg"
            >
              Create Account
            </button>
          </div>
        </div>

        <div v-else class="text-center space-y-4">
          <div class="mb-6">
            <div
              class="w-20 h-20 mx-auto bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center"
            >
              <i class="fas fa-user text-3xl text-white"></i>
            </div>
            <p class="mt-4 text-gray-800 dark:text-white font-medium">
              {{ session.user.email }}
            </p>
          </div>
          <button
            @click="handleSignOut"
            class="w-full bg-red-500 hover:bg-red-600 text-white py-3 rounded-xl font-semibold transform transition-all hover:scale-[1.02] hover:shadow-lg"
          >
            Sign Out
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { supabase } from "../lib/supabase";
import { useRouter } from "vue-router";

export default {
  name: "AuthForm",
  setup() {
    const session = ref(null);
    const email = ref("");
    const password = ref("");
    const showPassword = ref(false);
    const errorMessage = ref("");
    const router = useRouter();

    const setError = (error) => {
      const errorMessages = {
        "Invalid login credentials":
          "Invalid email or password. Please try again.",
        "Email not confirmed":
          "Please check your email to confirm your account before signing in.",
        "Password should be at least 6 characters":
          "Password must be at least 6 characters long.",
        "User already registered": "An account with this email already exists.",
        "Invalid email": "Please enter a valid email address.",
      };

      errorMessage.value = errorMessages[error.message] || error.message;

      setTimeout(() => {
        errorMessage.value = "";
      }, 5000);
    };

    const handleSignUp = async () => {
      try {
        const { error } = await supabase.auth.signUp({
          email: email.value,
          password: password.value,
        });

        if (error) throw error;

        errorMessage.value =
          "Success! Please check your email for confirmation.";
      } catch (error) {
        setError(error);
      }
    };

    const handleSignIn = async () => {
      try {
        const { error } = await supabase.auth.signInWithPassword({
          email: email.value,
          password: password.value,
        });

        if (error) throw error;

        router.push("/home");
      } catch (error) {
        setError(error);
      }
    };

    const handleSignOut = async () => {
      try {
        const { error } = await supabase.auth.signOut();
        if (error) throw error;
      } catch (error) {
        setError(error);
      }
    };

    onMounted(() => {
      supabase.auth
        .getSession()
        .then(({ data: { session: currentSession } }) => {
          session.value = currentSession;
        });

      supabase.auth.onAuthStateChange((_event, currentSession) => {
        session.value = currentSession;
      });
    });

    return {
      session,
      email,
      password,
      showPassword,
      errorMessage,
      handleSignUp,
      handleSignIn,
      handleSignOut,
    };
  },
};
</script>

<style scoped>
.auth-container {
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.3s ease-out;
}
</style>
