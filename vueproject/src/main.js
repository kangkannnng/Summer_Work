import Vue from 'vue';
import App from './App.vue';
//引入路由
import router from './router/index.js';
//在这里我们引入ElementUI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
//引入axios
import axios from "axios";
// 引入序列化字符串文件
import QS from "qs";

Vue.config.productionTip = false
//注册ElementUI
Vue.use(ElementUI)
//注册axios
Vue.prototype.$axios = axios
//加入到原型链中
Vue.prototype.$qs = QS;
//将http挂在Vue的原型对象上面方便使用
//响应时间
axios.defaults.timeout = 5000;
//配置请求头
axios.defaults.headers.post["Content-Type"] ="application/x-www-form-urlencoded;charset=UTF-8";
//配置请求的地址
axios.defaults.beseURL = "";

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
