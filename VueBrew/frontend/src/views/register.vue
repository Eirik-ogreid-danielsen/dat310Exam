<template>
  <div class="register">
      <form @submit.prevent="Register()" method="POST">
        <input  type="text"
                name="Username"
                placeholder="Username"
                v-model="registerUser.username"
            />
            <br/>
            <input
                type="text"
                name="password"
                placeholder="Password"
                v-model="registerUser.password"
            />
            <br/>
            <input
                type="text"
                name="password"
                placeholder="Password"
                v-model="registerUser.passwordcheck"
            />
      <br />
      <button type="submit">Register</button>
        <br />
        
      </form>
  </div>
</template>

<script>
export default {
    data() {
        return {
        registerUser: {
            username: "",
            password: "",
            passwordcheck:"",
        },
    }
    },
    methods:{
        async Register() {
            let registerUser=this.registerUser
            let baseURL = "http://127.0.0.1:5000/";
            let response = await fetch(baseURL+"register", {
                method: "POST",
                credentials:"include",
                headers: {
                 'Content-Type': "application/json",
                 },
                body: JSON.stringify({
                    username: registerUser.username,
                    password: registerUser.password,
                }),
             });
            console.log(response);
            }
        }
}
</script>

<style>

</style>

