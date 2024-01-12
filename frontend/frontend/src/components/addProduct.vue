<template>
  <section class="vh-100 gradient-custom">
    <div id="add-blog" class="container py-5 h-100">
      <h2 class="display-4">I need to add authentication here</h2>

      <form v-if="!submitted">
        <h1 class="display-4">and product details and pictures.</h1>
        <label>lorem Title: </label>
        <input type="text" v-model="product.name" required />
        <label>lorem Content: </label>
        <textarea v-model="product.name2"></textarea>
        <label>lorem</label>
        <!--  -->
        <div class="form-check">
          <input
            class="form-check-input"
            type="checkbox"
            value="boot1"
            id="flexCheckDefault-1"
            v-model="product.categories"
          />
          <label class="form-check-label" for="flexCheckDefault-1">
            Checkbox 1
          </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="checkbox"
            value="boot"
            id="flexCheckDefault"
            v-model="product.categories"
          />
          <label class="form-check-label" for="flexCheckDefault">
            Checkbox 2
          </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="checkbox"
            value="shoes"
            id="flexCheckChecked"
            checked
            v-model="product.categories"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Checked checkbox
          </label>
        </div>

        <select v-model="product.author">
          <option v-for="(item, index) in authors" :key="index">
            {{ item }}
          </option>
        </select>
        <button class="btn btn-primary mx-5" v-on:click.prevent="submitBlog">
          Add Product
        </button>
      </form>
      <div v-if="submitted">
        <h3 class="display-3">Thanks for adding your Product</h3>
      </div>

      <div id="preview">
        <h3>Preview Product</h3>
        <p>Product Name: {{ product.name }}</p>
        <p>Blabla content: {{ product.name2 }}</p>
        <p>Categories:</p>
        <ul>
          <li v-for="(item, index) in product.categories" :key="index">
            {{ item }}
          </li>
        </ul>
        <p>lorem: {{ product.author }}</p>
      </div>
    </div>
  </section>
</template>

<script>
import { bus } from "../main";

import axios from "axios";
export default {
  components: {},
  data() {
    return {
      product: {
        name: "",
        name2: "",
        categories: [],
        author: "",
      },
      authors: ["lorem", "lorem", "lorem"],
      submitted: false,
    };
  },
  methods: {
    submitBlog: function () {
      this.post();
    },
    post: function () {
      axios
        .post("https://jsonplaceholder.typicode.com/posts", {
          title: this.product.name,
          body: this.product.name2,
          userId: 1,
        })
        .then((data) => {
          console.log(data);
          this.submitted = true;
          console.log(this.submitted);
          bus.$emit("submitted", this.submitted);
        });
    },
  },
};
</script>

<style scoped>
#add-blog * {
  box-sizing: border-box;
}
#add-blog {
  margin: 20px auto;
  max-width: 700px;
}
label {
  display: block;
  margin: 20px 0 10px;
}
h2 {
  color: rgb(253, 7, 245);
}
input[type="text"],
textarea {
  display: block;
  width: 100%;
  padding: 8px;
}
#preview {
  padding: 10px 20px;
  border: 1px dotted #ccc;
  margin: 30px 0;
}
h3 {
  margin-top: 10px;
}
#checkboxes input {
  display: inline-block;
  margin-right: 20px;
}
#checkboxes label {
  display: inline-block;
  margin-right: 20px;
}

.gradient-custom {
  /* fallback for old browsers */
  background: #6a11cb;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgb(255, 210, 180),
    rgba(37, 117, 252, 1)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, rgb(245, 245, 245), rgb(255, 242, 254));
}
</style>
