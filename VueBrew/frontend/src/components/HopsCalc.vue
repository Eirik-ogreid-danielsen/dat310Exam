<template>
  <div id=CalcContainer>
      <h3> Hops </h3>
      <select v-model="selected">
            <option value="">Select a Hop</option>
            <option v-for="hop in hops "  v-bind:key="hop.id" :value="hop.name">{{hop.name}}</option>
        </select>
        <input v-model="amount"/>|g
        <input v-model="time"/>|min
        <button class="add" @click="AddHop"> Add </button>
        <p>Hops</p>
        <ul id ="selectedHops">
            <li v-for="(hop, index) in currentRecipeHops"  :key="`hop-${index}`">
                {{hop.name}} {{hop.amount}} g {{hop.time}}
            </li>
        </ul>

  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
     data() {
        return{
            selected:'',
            amount:0.00,
            time:0
        }
    },

     computed:{
        ...mapGetters({hops:"getHops"}),
        ...mapGetters({selectedHop:"getSelectedHop"}),
        ...mapGetters({currentRecipeHops:"getCurrentRecipeHops"}),
    },

    methods:{
        AddHop(){
            this.$store.dispatch("selectHopName",this.selected)
            this.$store.dispatch("selectHopAmount",this.amount)
            this.$store.dispatch("selectHopTime",this.time)
           let  hop={
                name: this.selected,
                amount:this.amount,
                time:this.time
            }
            this.$store.dispatch("addHop",hop)
        },

       async created() {
            console.log("fetchinghops");
           this.$store.dispatch("fetchHops") 
        }
    },
}
</script>

<style>

</style>