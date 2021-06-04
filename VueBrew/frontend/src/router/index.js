import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import calculator from  "../views/calculator.vue";
import login from  "../views/login.vue";

import recipes from  "../views/recipes.vue";
import register from  "../views/register.vue";

const routes = [
  {
    path: "/",
    name: "calculator",
    component: calculator
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
      path:"/Home",
      name:"Home",
      component: Home
  },
  {
    path:"/login",
    name:"login",
    component: login
},
{
    path:"/register",
    name:"register",
    component: register
},

{
    path:"/recipes",
    name:"recipes",
    component: recipes
},
{
    path:"/recipe",
    name:"recipe",
    component: () => import("../views/recipe.vue")
}

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
