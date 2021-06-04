<template>
<div class="login">
  <form @submit.prevent="Login()" method="POST">
      <input
        type="text"
        name="Username"
        placeholder="Username"
        v-model="newUser.username"
      />
      <br />
      <input
        type="text"
        name="password"
        placeholder="Password"
        v-model="newUser.password"
      />
      <br />
      <button type="submit">Log In</button>
    </form>
</div>
</template>

<script>
import {mapGetters} from "vuex";
export default {

  name: "Signup",
  data() {
    return {
      newUser: {
        username: "",
        password: "",
      },
    }
  },
  computed: {
    ...mapGetters({ user: "getUser" }),
  },
  methods: {
    Login() {
      this.$store.dispatch("Login", this.newUser);
    },

    
  },

};

</script>

<style>

</style>