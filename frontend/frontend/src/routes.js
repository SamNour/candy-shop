import mainPage from "./components/mainPage.vue";
import addProduct from "./components/addProduct.vue";
import products from "./components/productsSearch.vue";
import showProduct from "./components/showProduct.vue";
import loginUser from "./components/loginUser.vue";
import signupUser from "./components/signupUser.vue";

export default [
  { path: "/", component: mainPage },
  { path: "/add", component: addProduct },
  { path: "/products", component: products },
  { path: "/products/:id", component: showProduct },
  { path: "/login", component: loginUser },
  { path: "/signup", component: signupUser },
];
