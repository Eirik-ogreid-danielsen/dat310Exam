<template>
<div>
    <h2>hello {{ user }}</h2>
    <select>
        <option value="">Select a Fermentable</option>
        <option v-for="fermentable in fermentables "  v-bind:key="fermentable.id" :value="fermentable.name">{{fermentable.name}}</option>
    </select>
</div>  
</template>

<script>
import {mapGetters} from "vuex";
export default {
    
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
        this.getFermentables()
        this.$store.dispatch("fetchFermentables")
    }

}
</script>


<style>

</style>