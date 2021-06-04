<template>
  <div class="recipeContainer">
      <h2>Recipe overvieew </h2>
      <label>Recipe Name: </label>
      <input v-model="name"/>
      <h3>Fermentables</h3>
      <ul class="recipeList" id="recipeFermentables">
        <li v-for="(fermentable,index) in currentRecipe.fermentables" :key="`fermentable-${index}`">
        
              {{fermentable.name}}:  {{fermentable.amount}} kg
        </li>
      </ul>
        <h3>Hops</h3>
        <ul class="recipeList" id="recipeHops">
            <li v-for="(hop,index) in currentRecipe.hops" :key="`hop-${index}`">
                {{hop.name}}: {{hop.amount}} g, at {{hop.time}} min
            </li>
        </ul>
        <h3>Yeast</h3>
        <p>{{currentRecipe.yeast}}</p>
        <h3>Mash</h3>
       <p>Mashwater: {{currentRecipe.mashwater}} liters, at {{currentRecipe.mashtemp}} degrees for {{currentRecipe.mashtime}} min</p>
        <h3>Boil info </h3>
        <p>BoilVolume: {{currentRecipe.preboilvolume}} Liter for {{currentRecipe.boiltime}} min</p>
        <p>Volume for fermentor: {{currentRecipe.postboilvolume}}Liters</p>
        

      
      <button class="save" @click="SaveRecipe()">Save</button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {

    data() {
        return{
            name:'', 
            abv:""
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
.recipeList{
    list-style-type: none;
    justify-content: center;
}
</style>