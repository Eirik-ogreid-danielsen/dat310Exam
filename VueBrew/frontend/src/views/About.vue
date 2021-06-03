<template>
<div id ="container">
  <FermentablesCalc />
  <HopsCalc />
  <YeastCalc />
</div>
</template>

<script>

import FermentablesCalc from '../components/FermentablesCalc.vue'
import HopsCalc from '../components/HopsCalc.vue'
import YeastCalc from '../components/YeastCalc.vue'
export default {
    Name:"componentTest",
    components: {

        FermentablesCalc,
        HopsCalc,
        YeastCalc
    },

    methods: {
        created() {
        //this.getFermentables()
            console.log("fetchingdata");
            this.$store.dispatch("fetchFermentables")
            this.$store.dispatch("fetchHops")
            this.$store.dispatch("fetchYeasts")
        }
    }

}
</script>

<style>

</style>
