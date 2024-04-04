<template>
  <div class="container mt-5">
    <h1 class="display-3 mb-4">Here is your Product</h1>
    <div class="card">
      <div class="card-body">
        <h2 class="card-title">Product Title: {{ products.name }}</h2>
        <p class="card-text">{{ products.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      id: this.$route.params.id,
      products: [],
    };
  },
  created() {
    const id = this.$route.params.id;
    console.log("the fetches product id is ==> " + id);
    console.log(this.products);
    axios
      .get("http://localhost:5000/products/" + this.id)
      .then((response) => {
        console.log("here is your response");
        console.log(response);
        this.products = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>
