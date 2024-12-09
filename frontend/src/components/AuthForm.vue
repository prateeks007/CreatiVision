<template>
  <div
    class="auth-container p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md"
  >
    <div v-if="!session" class="space-y-4">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-white mb-4">
        Sign In / Sign Up
      </h2>

      <input
        type="email"
        v-model="email"
        placeholder="Email"
        class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
      />

      <input
        type="password"
        v-model="password"
        placeholder="Password"
        class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white"
      />

      <div class="flex space-x-4">
        <button
          @click="handleSignUp"
          class="flex-1 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition-colors"
        >
          Sign Up
        </button>
        <button
          @click="handleSignIn"
          class="flex-1 bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition-colors"
        >
          Sign In
        </button>
      </div>
    </div>

    <div v-else class="text-center">
      <p class="text-gray-800 dark:text-white mb-4">
        Signed in as {{ session.user.email }}
      </p>
      <button
        @click="handleSignOut"
        class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors"
      >
        Sign Out
      </button>
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
    const router = useRouter();

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

    const handleSignUp = async () => {
      try {
        console.log("Attempting sign up...");
        const { data, error } = await supabase.auth.signUp({
          email: email.value,
          password: password.value,
        });
        if (error) {
          console.error("Sign up error:", error);
          throw error;
        }
        console.log("Sign up successful:", data);
        alert("Check your email for the confirmation link!");
      } catch (error) {
        console.error("Sign up error:", error);
        alert(error.message);
      }
    };

    const handleSignIn = async () => {
      try {
        console.log("Attempting sign in...");
        const { data, error } = await supabase.auth.signInWithPassword({
          email: email.value,
          password: password.value,
        });
        if (error) {
          console.error("Sign in error:", error);
          throw error;
        }
        console.log("Sign in successful:", data);
        router.push("/home");
      } catch (error) {
        console.error("Sign in error:", error);
        alert(error.message);
      }
    };

    const handleSignOut = async () => {
      try {
        const { error } = await supabase.auth.signOut();
        if (error) throw error;
      } catch (error) {
        alert(error.message);
      }
    };

    return {
      session,
      email,
      password,
      handleSignUp,
      handleSignIn,
      handleSignOut,
    };
  },
};
</script>
