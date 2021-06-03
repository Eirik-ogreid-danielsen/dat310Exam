<template>
  <div id=CalcContainer>
      <h3> Fermentables </h3>
        <select>
            <option value="">Select a Fermentable</option>
            <option v-for="fermentable in fermentables "  v-bind:key="fermentable.id" :value="fermentable.name">{{fermentable.name}}</option>
        </select>
        <input v-model="amount"/>|kg
        <button class="add"> Add </button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
    data() {
        return{
            amount:'0'
        }
    },

     computed:{
        ...mapGetters({fermentables:"getFermentables"})
    },

    methods:{
       created() {
            console.log("fetching fermentables");
           this.$store.dispatch("fetchFermentables") 
        }
    },

}
</script>

<style>

</style>