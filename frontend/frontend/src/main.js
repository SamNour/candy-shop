import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import Routes from "./routes";
import "bootstrap-icons/font/bootstrap-icons.css";
import "bootstrap/dist/js/bootstrap.bundle";
import VueParticlesBg from "particles-bg-vue";

export const bus = new Vue();

//register our routes
const router = new VueRouter({
  routes: Routes,
  mode: "history",
});

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueParticlesBg);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  router: router,
}).$mount("#app");
