<template>
<div id="recipesContainer">
 <h3> Recipes </h3>
 
 <ul id="allRecipes" @load="FetchRecipes">
            <li v-for="recipe in recipes" :key="recipe.id">
                <router-link :to="{ name:  'recipe' , params: {id:recipe.id}}">{{recipe.name}}  {{recipe.author}} </router-link>
                        
            </li>
        </ul>
</div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
    computed:{
        ...mapGetters({recipes:"getRecipes"})
    },
    
        mounted (){
            this.$store.dispatch("fetchRecipes")
        }
    
}
</script>

<style>

</style>