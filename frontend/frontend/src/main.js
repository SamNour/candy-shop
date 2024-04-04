import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import App from "./App.vue";
import "bootstrap-icons/font/bootstrap-icons.css";
import VueParticlesBg from "particles-bg-vue";
import "bootstrap/dist/js/bootstrap.bundle";
import VueRouter from "vue-router";
import Routes from "./routes";

const router = new VueRouter({
  routes: Routes,
  mode: "history",
});

import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap/dist/css/bootstrap.css";

Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueParticlesBg);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  router: router,
}).$mount("#app");
