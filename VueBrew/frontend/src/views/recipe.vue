<template>
<div>
   
  <div class="recipeContainer">
      <h1>{{recipe.name}}</h1>
      <h3>By {{recipe.author}}</h3>
      <h3>Fermentables</h3>
      <ul class="recipeList" id="recipeFermentables">
        <li v-for="(fermentable,index) in recipe.fermentables" :key="`fermentable-${index}`">
        
              {{fermentable.name}}:  {{fermentable.amount}} kg
        </li>
      </ul>
        <h3>Hops</h3>
        <ul class="recipeList" id="recipeHops">
            <li v-for="(hop,index) in recipe.hops" :key="`hop-${index}`">
                {{hop.name}}: {{hop.amount}} g, at {{hop.time}} min
            </li>
        </ul>
        <h3>Mash</h3>
       <p>Mashwater: {{recipe.mashwater}} liters, at {{recipe.mashtemp}} degrees for {{recipe.mashtime}} min</p>
        <h3>Boil info </h3>
        <p>BoilVolume: {{recipe.preboilvolume}} Liter for {{recipe.boiltime}} min</p>
        <p>Volume for fermentor: {{recipe.postboilvolume}}Liters</p>
        

      
      
  </div>
</div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
   data() {
        return{
            id:-1,
            recipe:''
        }
    },
    methods:{
        GetID(){
            this.id = this.$route.params.id
        },
        GetRecipe(){
            this.recipe = this.recipes[this.id-1]
        }
            
    },

computed:{
        ...mapGetters({recipes:"getRecipes"}),
        

    },
    mounted (){
        this.GetID()
        this.GetRecipe()
        
    }
}
</script>

<style>

</style>