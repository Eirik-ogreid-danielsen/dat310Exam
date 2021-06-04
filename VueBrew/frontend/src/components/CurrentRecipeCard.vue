<template>
  <div class="recipeContainer">
      <label>Recipe Name: </label>
      <input v-model="name"/>
      {{currentRecipe}}
      <button class="save" @click="SaveRecipe()">Save</button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {

    data() {
        return{
            name:'', 
        }
    },

 computed:{
    ...mapGetters({currentRecipe:"getCurrentRecipe"}),
     ...mapGetters({ user: "getUser" }),
 },
 methods:{
     async SaveRecipe() {
         this.$store.dispatch("addRecipeAuthor",this.user)
         let currentRecipe = this.currentRecipe
         let baseURL = "http://127.0.0.1:5000/";
         let response = await fetch(baseURL+"saveRecipe", {
                method: "POST",
                credentials:"include",
                headers: {
                 'Content-Type': "application/json",
                 },
                body: JSON.stringify({
                    name:this.name,
                    user:currentRecipe.user,
                    fermentables:currentRecipe.fermentables,
                    hops:currentRecipe.hops,
                    yeast:currentRecipe.yeast,
                    mashtemp:currentRecipe.mashtemp,
                    mashtime:currentRecipe.mashtime,
                    mashwater:currentRecipe.mashwater,
                    strikewater:currentRecipe.strikewater,
                    boiltime:currentRecipe.boiltime,
                    postboilvolume:currentRecipe.postboilvolume,
                    preboilvolume:currentRecipe.preboilvolume,
                }),
             });
             console.log(response);
     }
            
 },
}
</script>
    
<style>

</style>