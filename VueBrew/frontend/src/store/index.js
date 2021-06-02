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
             ammount: '',
         },
    selectedYeast:'',
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
     

  },
  getters: {
    getUser:  (state) => state.currentUser,
    getFermentables: (state) => state.fermentables,
    getHops: (state) => state.hops,
    getYeasts: (state) => state.yeasts
  },
  modules: {},
});