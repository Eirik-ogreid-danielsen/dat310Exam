<template>
  <div id="CalcContainer">
        <div id="mashInstructions">
            <h3>Mash</h3>
            <label>Mashwater</label>
            <input v-model="mashwater"/> Liters
            <input v-model="mashtemp"/> C
            <input v-model="mashtime"/> min
            <label>Strikewater</label>
            <input v-model="strikewater"/> Liters
        </div>
        <div id="boilInstructions">
            <h3>Boil</h3>
            <label>Preboil</label>
            <input v-model="preboilvolume"/> Liters
            <label>Boiltime</label>
            <input v-model="boiltime"/> min
            <label>Postboil</label>
            <input v-model="postboilvolume"/> Liters
        </div>
        <button class="add" @click="addWater()"> Add </button>
  </div>
</template>

<script>
export default {

    data() {
        return{
            mashtemp:0,
            mashtime:0,
            mashwater:0,
            strikewater:0,
            boiltime:0,
            preboilvolume:0,
            postboilvolume:0,
        }
    },
    methods:{
        addWater(){
            this.$store.dispatch("addRecipeMashTemp",this.mashtemp)
            this.$store.dispatch("addRecipeMashTime",this.mashtime)
            this.$store.dispatch("addRecipeMashWater",this.mashwater)
            this.$store.dispatch("addRecipeStrikeWater",this.strikewater)
            this.$store.dispatch("addRecipePreBoilVolume",this.preboilvolume)
            this.$store.dispatch("addRecipePostBoilVolume",this.postboilvolume)
            this.$store.dispatch("addRecipeBoilTime",this.boiltime)
        }
    }

}
</script>

<style>

</style>