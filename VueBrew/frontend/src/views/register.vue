<template>
  <div class="register">
      <form @submit.prevent="sendRegister()" method="POST">
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
         <p v-if="errors.length">
        <b>Please correct the following error(s):</b>
            <ul>
                <li v-for="(error, index) in errors" :key="`error-${index}`">{{ error }}</li>
            </ul>
        </p>
        
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
        errors:[]
    }
    },
    //unfinished validation
    methods:{
        Register(){
            let validate=this.Validate()
            if (validate.valid) {
                this.sendRegister
            }else{
                let error = this.Validate.msg
                this.errors.push(error)
                console.log(this.errors);
            }
        },

        Validate(){
            let password= this.password
            let passwordcheck=this.passwordcheck
            let response ={
                valid:true,
                msg:"ok",
               
            }
            if (password!==passwordcheck){
                response = {
                    valid:false,
                    msg:"Passwords does not match"
                }
                return response
            }
            if (password.length >! 8) {
                response = {
                    valid:false,
                    msg:"Passwords must be longer than 8 characters"
                }
                return response
                    
            }

            return response
        },
        //registers user, all validation on server
        async sendRegister() {
            
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

