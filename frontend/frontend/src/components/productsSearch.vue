<template>
  <div id="show-products">
    <h1>Add your product - Form</h1>
    <input
      id="searchBar"
      type="text"
      v-model="search"
      placeholder="Search blogs..."
    />
    <div
      v-for="(product, index) in filteredBlogs"
      :key="index"
      class="single-product"
    >
      <router-link v-bind:to="'/products/' + product.id"
        ><h2>{{ product.title }}</h2></router-link
      >
      <article>{{ product.body }}</article>
    </div>
  </div>
</template>

<script>
import searchMixin from "../mixins/searchMixin";
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      product: [],
      search: "",
    };
  },
  methods: {
    fetchPosts() {
      axios
        .get("http://localhost:5000/products")
        .then((response) => {
          this.product = response.data.slice(0, 10);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.fetchPosts();
  },
  mixins: [searchMixin],
};
</script>

<style scoped>
#show-products {
  font-family: Arial, sans-serif;
  margin: 0 auto;
  max-width: 800px;
}

#show-products h1 {
  color: #333;
  font-size: 2em;
  text-align: center;
  margin-bottom: 1em;
}

.single-product {
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-bottom: 1em;
  padding: 1em;
}

.single-product h2 {
  color: #333;
  font-size: 1.5em;
}

.single-productsingle-product article {
  color: #666;
  line-height: 1.6;
}
#searchBar {
  width: 100%;
  padding: 10px 20px;
  margin: 10px 0;
  box-sizing: border-box;
  border: none;
  border-radius: 4px;
  background-color: #f1f1f1;
  font-size: 16px;
  transition: width 0.4s ease-in-out;
}

#searchBar:focus {
  width: 100%;
  outline: none;
  background-color: #ddd;
}
</style>
