<template>
  <div id=CalcContainer>
      <h3> Hops </h3>
      <select>
            <option value="">Select a Hop</option>
            <option v-for="hop in hops "  v-bind:key="hop.id" :value="hop.name">{{hop.name}}</option>
        </select>
        <input v-model="amount"/>|g
        <input v-model="time"/>|min
        <button class="add"> Add </button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
     data() {
        return{
            amount:0.00,
            time:0
        }
    },

     computed:{
        ...mapGetters({hops:"getHops"})
    },

    methods:{
       async created() {
            console.log("fetchinghops");
           this.$store.dispatch("fetchHops") 
        }
    },
}
</script>

<style>

</style>