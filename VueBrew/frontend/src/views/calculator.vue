<template>
  <h2>hello {{ user }}</h2>
</template>

<script>
import {mapGetters} from "vuex";
export default {
    computed: {
        ...mapGetters({user: "getUser"})
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
    }

}
</script>


<style>

</style>