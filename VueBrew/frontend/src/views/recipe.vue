<template>
<div>
  
  <p>{{recipe}}</p>
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