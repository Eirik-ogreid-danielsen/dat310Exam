<template>
  <div id=CalcContainer>
      <h3> Yeast </h3>
      
      <select v-model="selectedYeast">
            <option value="">Select a Yeast</option>
            <option v-for="yeast in yeasts "  v-bind:key="yeast.id" :value="yeast.name">{{yeast.name}}</option>
        </select>
        <button class="add" @click="AddYeast()"> Add </button>
        <p>Yeast</p>
        {{currentRecipeYeast}}
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
    data() {
        return{
            selectedYeast:''
        }
    },
    computed:{
        ...mapGetters({yeasts:"getYeasts"}),
        ...mapGetters({currentRecipeYeast:"getCurrentRecipeYeast"})
    },

    methods:{

        AddYeast() {
            this.$store.dispatch("addYeast",this.selectedYeast)
        },

        async created() {
            console.log("fetching yeasts");
           this.$store.dispatch("fetchYeasts") 
        }
    },

}
</script>

<style>

</style>