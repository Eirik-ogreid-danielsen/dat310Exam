import { createStore } from "vuex";

export default createStore({
  state: {
      currentUser: " ",
      fermentables:[],
      hops:[],
      yeasts:[],
      recipes:[],
      selectedFermentable: {
             name:"",
             amount: 0,
         },
    selectedYeast:'',
    selectedHop:{
        name:"",
        amount:0,
        time:0,
    },
    recipe: {
            id:'',
            user:'',
            fermentables:[],
            hops:[],
            yeast:'',
            mashtemp:'',
            mashtime:'',
            mashwater:'',
            strikewater:'',
            boiltime:'',
            postBoilVolume:'',
         },
    currentRecipe: {
            name:'',
            user:'',
            fermentables:[],
            hops:[],
            yeast:'',
            mashtemp:'',
            mashtime:'',
            mashwater:'',
            strikewater:'',
            boiltime:'',
            postboilvolume:'',
         },
    },
  mutations: {
    logInUser(state,user) {
          state.currentUser = user
      },
    setFermentables(state,fermentables) {
            state.fermentables = fermentables
        }, 
    setHops(state,hops) {
            state.hops = hops
         },
    setYeasts(state,yeasts) {
            state.yeasts = yeasts
        },
    setSelectedFermentableName(state,name){
        state.selectedFermentable.name =name
    },
    setSelectedFermentableAmount(state,amount){
        state.selectedFermentable.amount = amount
    },
    setCurrentRecipeFermentables(state,fermentable) {
        console.log(state.currentRecipe.fermentables);
        console.log(fermentable);
        state.currentRecipe.fermentables.push(fermentable)
        console.log(state.currentRecipe.fermentables);
    },
    setSelecteHopName(state,name){
        state.selectedHop.name=name
    },
    setSelecteHopAmount(state,amount){
        state.selectedHop.amount=amount
    },
    setSelecteHopTime(state,time){
        state.selectedHop.time=time
    },
    setCurrentRecipeHops(state,selectedHop){
        state.currentRecipe.hops.push(selectedHop)
    },
    setCurrentRecipeYeast(state,selectedYeast){
        state.currentRecipe.yeast=selectedYeast
    },
    setCurrentRecipeUser(state,user){
        state.currentRecipe.user=user
    },
    setCurrentRecipeMashTemp(state,mashtemp){
        state.currentRecipe.mashtemp=mashtemp
    },
    setCurrentRecipeMashTime(state,mashtime){
        state.currentRecipe.mashtemp=mashtime
    },
    setCurrentRecipeMashWater(state,mashwater){
        state.currentRecipe.mashwater=mashwater
    },
    setCurrentRecipeStrikeWater(state,strikewater){
        state.currentRecipe.strikewater=strikewater
    },
    setCurrentRecipePreBoilVolume(state,preboilvolume){
        state.currentRecipe.preboilvolume=preboilvolume
    },
    setCurrentRecipePostBoilVolume(state,postboilvolume){
        state.currentRecipe.postboilvolume=postboilvolume
    },
    setCurrentRecipeBoilTime(state,boiltime){
        state.currentRecipe.boiltime=boiltime
    },
    setRecipes(state,recipes){
        state.recipes=recipes
    }
    
  },
  actions: {

    async Login({ commit }, user) {
        let baseURL = "http://127.0.0.1:5000/";
        let response = await fetch(baseURL+"login", {
          method: "POST",
          credentials:"include",

          headers: {

            'Content-Type': "application/json",
          },
          body: JSON.stringify({
            username: user.username,
            password: user.password,
          }),
        });
        console.log(response);
        let verifiedUser = await response.json();
        commit("logInUser",verifiedUser.username)
     },

     async  fetchFermentables({ commit }) {
        fetch('http://127.0.0.1:5000/fermentables', {
            method:"GET",
            headers: {
                "content-type":"application/json"
            }
         })
         .then(resp => resp.json())
         .then(data => {
             let fermentables=data;
             commit("setFermentables",fermentables)
         })
         .catch(error => {
             console.log(error);
         })
     },

     async   fetchHops({ commit }) {
        fetch('http://127.0.0.1:5000/hops', {
            method:"GET",
            headers: {
                "content-type":"application/json"
            }
         })
         .then(resp => resp.json())
         .then(data => {
             let hops=data;
             commit("setHops",hops)
         })
         .catch(error => {
             console.log(error);
         })
    },

     async   fetchRecipes({ commit }) {
        fetch('http://127.0.0.1:5000/recipes', {
            method:"GET",
            headers: {
                "content-type":"application/json"
            }
         })
         .then(resp => resp.json())
         .then(data => {
             let recipes=data;
             commit("setRecipes",recipes)
         })
         .catch(error => {
             console.log(error);
         })
    },
    async   fetchYeasts({ commit }) {
        fetch('http://127.0.0.1:5000/yeasts', {
            method:"GET",
            headers: {
                "content-type":"application/json"
            }
         })
         .then(resp => resp.json())
         .then(data => {
             let yeasts=data;
             commit("setYeasts",yeasts)
         })
         .catch(error => {
             console.log(error);
         })
    },
    selectFermentableName({commit}, fermentable){
        commit("setSelectedFermentableName",fermentable) 
    },
    selectFermentableAmount({commit}, amount) {
        commit("setSelectedFermentableAmount",amount)
    },
    addFermentable({commit},selectedFermentable){
        
        commit("setCurrentRecipeFermentables",selectedFermentable)
    },
    selectHopName({commit},hop){
        commit("setSelecteHopName",hop)
    },
    selectHopAmount({commit},amount){
        commit("setSelecteHopAmount",amount)
    },
    selectHopTime({commit},time){
        commit("setSelecteHopTime",time)
    },
    addHop({commit},hop){
        commit("setCurrentRecipeHops",hop)
    },
    addYeast({commit},yeast){
        commit("setCurrentRecipeYeast",yeast)
    },
    addRecipeAuthor({commit},user){
        commit("setCurrentRecipeUser",user)
    },
    addRecipeMashTemp({commit},mashtemp){
        commit("setCurrentRecipeMashTemp",mashtemp)
    },
    addRecipeMashTime({commit},mashtime){
        commit("setCurrentRecipeMashTime",mashtime)
    },
    addRecipeMashWater({commit},mashwater){
        commit("setCurrentRecipeMashWater",mashwater)
    }, 
    addRecipeStrikeWater({commit},strikewater){
        commit("setCurrentRecipeStrikeWater",strikewater)
    }, 
    addRecipePreBoilVolume({commit},preboilvolume){
        commit("setCurrentRecipePreBoilVolume",preboilvolume)
    }, 
    addRecipePostBoilVolume({commit},postboilvolume){
        console.log(postboilvolume);
        commit("setCurrentRecipePostBoilVolume",postboilvolume)
    }, 
    addRecipeBoilTime({commit},boiltime){
        console.log(boiltime);
        commit("setCurrentRecipeBoilTime",boiltime)
    }, 
        
  },
  getters: {
    getUser:  (state) => state.currentUser,
    getFermentables: (state) => state.fermentables,
    getHops: (state) => state.hops,
    getYeasts: (state) => state.yeasts,
    getSelectedFermentable:(state) => state.selectedFermentable,
    getCurrentRecipe:(state) => state.currentRecipe,
    getCurrentRecipeFermentables:(state) => state.currentRecipe.fermentables,
    getCurrentRecipeHops:(state) => state.currentRecipe.hops,
    getSelectedHop:(state)=> state.selectedHop,
    getCurrentRecipeYeast:(state) => state.currentRecipe.yeast,
    getRecipes:(state) => state.recipes,
   
  },
  modules: {},
});