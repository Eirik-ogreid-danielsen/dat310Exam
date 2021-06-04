<template>
<div id ="mainview">
  <div id="nav">
    <div id="currentUser"> User : {{user}} </div>|
    <router-link to="/">Calculator</router-link> |
    <router-link to="/login">login</router-link> |
    <router-link to="/recipes">Recipes</router-link> |
    <router-link to="register">Register</router-link>|
    <button @click="LogOut()">Log Out</button>
    
  </div>
    <div id="content">
    <router-view />
    </div>
</div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
    computed: {
        ...mapGetters({ user: "getUser" })
    },
    methods:{
        LogOut() {
            this.$store.dispatch("LogOut")
        }
            
    }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  justify-content: center;
  color: #2c3e50;
}
.content{
    display:flex;
    flex-direction: row;
    justify-content: center;
    padding-top: 25px;
    
}

#nav {
  padding: 5px;
  display: inline;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#CalcContainer {
    border: solid;
    border-color:  #2c3e50;
    font-size: 12px
    ;
    
}
.recipeContainer{
    border: solid;
    border-color:  #2c3e50;
    max-width: 100%;
    font-size: 12px;
    height: 100%;
    
}
</style>
