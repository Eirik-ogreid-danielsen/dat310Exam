<template>
<div>
    <h2>hello {{ user }}</h2>
    <FermentablesCalc />
    <HopsCalc />
    <YeastCalc />
    
</div>  
</template>

<script>
import {mapGetters} from "vuex";
import FermentablesCalc from '../components/FermentablesCalc.vue'
import HopsCalc from '../components/HopsCalc.vue'
import YeastCalc from '../components/YeastCalc.vue'



export default {
    
    name:"Calculator",

    components: {

        FermentablesCalc,
        HopsCalc,
        YeastCalc
    },
    
    
    computed: {
        ...mapGetters({user: "getUser"}),
        ...mapGetters({fermentables:"getFermentables"})
    },

    methods: {
        getFermentables() {
            fetch('http://127.0.0.1:5000/fermentables', {
                method:"GET",
                headers: {
                    "content-type":"application/json"
                }
             })
             .then(resp => resp.json())
             .then(data => {
                 console.log(data);
             })
             .catch(error => {
                 console.log(error);
             })
        }
    },
    created() {
        //this.getFermentables()
        console.log("fetchingFermentables");
        this.$store.dispatch("fetchFermentables")
        this.$store.dispatch("fetchHops")
        this.$store.dispatch("fetchYeasts")
    }

}
</script>


<style>

</style>