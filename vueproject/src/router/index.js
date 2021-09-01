import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home";
import Check from "../components/Check";
import Compare from "../components/Compare";
import Manage from "../components/Manage";

// 引入组件
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path:"/home",
    component: Home
  },
  {
    path: "/check",
    component: Check
  },
  {
    path: "/compare",
    component: Compare
  },
  {
    path: "/manage",
    component: Manage
  },


]

const router = new VueRouter({
  mode:"hash",
  routes
});

export default router;
