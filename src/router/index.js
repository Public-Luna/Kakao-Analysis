import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      component: () => import("@/views/Home"),
      children: []
    },
    {
      path: "/upload",
      component: () => import("@/views/Upload"),
      children: []
    },
    {
      path: "/analysis",
      component: () => import("@/views/Analysis"),
      // children: [
      //   {
      //     path: "",
      //     name: "home",
      //     component: () => import("@/views/HomeGlobal")
      //   },
      // ]
    },
    {
      path: "/project",
      component: () => import("@/views/Project"),
      children: []
    },
  ]
});
