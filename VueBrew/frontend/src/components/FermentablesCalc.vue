<template>
  <div id=CalcContainer>
      <h3> Fermentables </h3>
        <select v-model="selected">
            <option value="">Select a Fermentable</option>
            <option v-for="fermentable in fermentables "  v-bind:key="fermentable.id" :value="fermentable.name">{{fermentable.name}}</option>
        </select>
        <input v-model="amount"/>|kg
        <button class="add" @click="AddFermentable()"> Add </button>
        <p>Fermentables</p>
        <ul id="selectedFermentables">
            <li v-for="(fermentable, index) in currentRecipeFermentables" :key="`fermentable-${index}`">
            {{fermentable.name}}  {{fermentable.amount}} kg
            </li>
        </ul>

  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
    data() {
        return{
            amount:'0',
            selected:''
        }
    },

     computed:{
        ...mapGetters({fermentables:"getFermentables"}),
        ...mapGetters({selectedFermentable:"getSelectedFermentable"}),
        ...mapGetters({currentRecipeFermentables:"getCurrentRecipeFermentables"})
    },

    methods:{
        AddFermentable(){
            this.$store.dispatch("selectFermentableName",this.selected)
            this.$store.dispatch("selectFermentableAmount",this.amount)
            console.log(this.currentRecipeFermentables);
            let fermentable = {
                name: this.selected,
                amount: this.amount
            }
            this.$store.dispatch("addFermentable",fermentable)
        },

       created() {
            console.log("fetching fermentables");
           this.$store.dispatch("fetchFermentables") 
        }
    },

}
</script>

<style>
#selectedFermentables{
    list-style-type: none;
}
</style>