<template>
<div>
    <div class="content">
        <div id=ContentContainer>
        <FermentablesCalc />
        <HopsCalc />
        <YeastCalc />
        <WaterCalc />
        </div>
        <div class=RecipeContainer>
        <CurrentRecipeCard />
        </div>
        </div>
</div>  
</template>

<script>
import {mapGetters} from "vuex";
import FermentablesCalc from '../components/FermentablesCalc.vue'
import HopsCalc from '../components/HopsCalc.vue'
import YeastCalc from '../components/YeastCalc.vue'
import WaterCalc from '../components/WaterCalc.vue'
import CurrentRecipeCard from '../components/CurrentRecipeCard.vue'



export default {
    
    name:"Calculator",

    components: {

        FermentablesCalc,
        HopsCalc,
        YeastCalc,
        WaterCalc,
        CurrentRecipeCard
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
        this.$store.dispatch("fetchRecipes")
    }

}
</script>


<style>
.content{
     display: grid;
    place-items: center;
    grid-template-columns: auto auto;
}
#ContentContainer{
    display: flex;
    flex-direction: column;
    justify-content: center;
}

</style>