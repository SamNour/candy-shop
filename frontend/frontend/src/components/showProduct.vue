<template>
  <div class="container mt-5">
    <h1 class="display-3 mb-4">Here is your Product</h1>
    <div class="card">
      <div class="card-body">
        <h2 class="card-title">Product Title: {{ products.title }}</h2>
        <p class="card-text">{{ products.body }}</p>
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
      products: {},
    };
  },
  created() {
    const id = this.$route.params.id;
    console.log("the fetches prodcut id is ==> " + id);
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
