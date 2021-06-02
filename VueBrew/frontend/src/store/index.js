import { createStore } from "vuex";

export default createStore({
  state: {
      currentUser: " "
    },
  mutations: {
      logInUser(state,user) {
          state.currentUser = user
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
       
    }
  },
  getters: {
    getUser:  (state) => state.currentUser
  },
  modules: {},
});
