<template>
  <div id=CalcContainer>
      <h3> Yeast </h3>
      
      <select>
            <option value="">Select a Yeast</option>
            <option v-for="yeast in yeasts "  v-bind:key="yeast.id" :value="yeast.name">{{yeast.name}}</option>
        </select>
        <button class="add"> Add </button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
    computed:{
        ...mapGetters({yeasts:"getYeasts"})
    },

    methods:{
        async created() {
            console.log("fetching yeasts");
           this.$store.dispatch("fetchYeasts") 
        }
    },

}
</script>

<style>

</style>