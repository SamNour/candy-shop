<template>
  <section class="h-100 h-custom" style="background-color: #eee">
    <!-- <h1>{{ userNameUpdate }}</h1>
    <h5>{{ filteredBlogs }}</h5> -->

    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col">
          <div class="card">
            <div class="card-body p-4">
              <div class="row">
                <div class="col-lg-7">
                  <h5 class="mb-3">
                    <router-link
                      class="fas fa-long-arrow-alt-left me-2 continue-shopping-link"
                      to="/products"
                      exact
                      >Continue shopping</router-link
                    >
                  </h5>
                  <hr />

                  <div
                    class="d-flex justify-content-between align-items-center mb-4"
                  >
                    <div>
                      <p class="mb-1">Shopping cart</p>
                      <p class="mb-0">You have {{ items }}items in your cart</p>
                    </div>
                    <div>
                      <p class="mb-0">
                        <span class="text-muted">Sort by:</span>
                        <a href="#!" class="text-body"
                          >price <i class="fas fa-angle-down mt-1"></i
                        ></a>
                      </p>
                    </div>
                  </div>

                  <div
                    class="card mb-3"
                    v-for="(product, index) in filteredBlogs"
                    :key="index"
                  >
                    <div class="card-body">
                      <div class="d-flex justify-content-between">
                        <div class="d-flex flex-row align-items-center">
                          <div>
                            <img
                              :src="'/' + (index % 4) + '.jpg'"
                              class="img-fluid rounded-3"
                              alt="Shopping item"
                              style="width: 65px"
                            />
                          </div>
                          <div class="ms-3">
                            <h5>{{ product.name }}</h5>
                            <p class="small mb-0">{{ product.description }}</p>
                          </div>
                        </div>
                        <div class="d-flex flex-row align-items-center">
                          <div style="width: 50px">
                            <h5 class="fw-normal mb-0">
                              {{ product.quantity }}
                            </h5>
                          </div>
                          <div style="width: 80px">
                            <h5 class="mb-0">
                              {{ product.price * product.quantity }}
                            </h5>
                          </div>
                          <a
                            class="btn btn-primary"
                            role="button"
                            style="
                              margin-right: 10px;
                              width: 30px;
                              height: 30px;
                              text-align: center;
                              line-height: 30px;
                            "
                            v-on:click="incrementQuantity(index)"
                          >
                            +
                          </a>

                          <a
                            class="btn btn-primary"
                            role="button"
                            style="
                              width: 30px;
                              height: 30px;
                              text-align: center;
                              line-height: 30px;
                              padding: 0;
                            "
                            v-on:click="decrementQuantity(index)"
                          >
                            -
                          </a>
                          <a
                            href="#!"
                            style="color: #cecece"
                            @click="deleteProduct(index)"
                          >
                            <i class="fas fa-trash-alt"></i>
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-lg-5">
                  <div class="card bg-primary text-white rounded-3">
                    <div class="card-body">
                      <div
                        class="d-flex justify-content-between align-items-center mb-4"
                      >
                        <h5 class="mb-0">Card details</h5>
                      </div>

                      <p class="small mb-2">Card type</p>
                      <a href="#!" type="submit" class="text-white"
                        ><i class="fab fa-cc-mastercard fa-2x me-2"></i
                      ></a>
                      <a href="#!" type="submit" class="text-white"
                        ><i class="fab fa-cc-visa fa-2x me-2"></i
                      ></a>
                      <a href="#!" type="submit" class="text-white"
                        ><i class="fab fa-cc-amex fa-2x me-2"></i
                      ></a>
                      <a href="#!" type="submit" class="text-white"
                        ><i class="fab fa-cc-paypal fa-2x"></i
                      ></a>

                      <form class="mt-4">
                        <div class="form-outline form-white mb-4">
                          <input
                            type="text"
                            id="typeName"
                            class="form-control form-control-lg"
                            siez="17"
                            placeholder="Cardholder's Name"
                          />
                          <label class="form-label" for="typeName"
                            >Cardholder's Name</label
                          >
                        </div>

                        <div class="form-outline form-white mb-4">
                          <input
                            type="text"
                            id="typeText"
                            class="form-control form-control-lg"
                            siez="17"
                            placeholder="1234 5678 9012 3457"
                            minlength="19"
                            maxlength="19"
                          />
                          <label class="form-label" for="typeText"
                            >Card Number</label
                          >
                        </div>

                        <div class="row mb-4">
                          <div class="col-md-6">
                            <div class="form-outline form-white">
                              <input
                                type="text"
                                id="typeExp"
                                class="form-control form-control-lg"
                                placeholder="MM/YYYY"
                                size="7"
                                minlength="7"
                                maxlength="7"
                              />
                              <label class="form-label" for="typeExp"
                                >Expiration</label
                              >
                            </div>
                          </div>
                          <div class="col-md-6">
                            <div class="form-outline form-white">
                              <input
                                type="password"
                                id="typeText"
                                class="form-control form-control-lg"
                                placeholder="&#9679;"
                                size="1"
                                minlength="3"
                                maxlength="3"
                              />
                              <label class="form-label" for="typeText"
                                >Cvv</label
                              >
                            </div>
                          </div>
                        </div>
                      </form>

                      <hr class="my-4" />

                      <div class="d-flex justify-content-between">
                        <p class="mb-2">Subtotal</p>
                        <p class="mb-2">{{ subtotal }}</p>
                      </div>

                      <div class="d-flex justify-content-between">
                        <p class="mb-2">Shipping</p>
                        <p class="mb-2">{{ shipping }}</p>
                      </div>

                      <div class="d-flex justify-content-between mb-4">
                        <p class="mb-2">Total(Incl. taxes)</p>
                        <p class="mb-2">{{ total }}</p>
                      </div>

                      <button
                        type="button"
                        class="btn btn-info btn-block btn-lg"
                      >
                        <div class="d-flex justify-content-between">
                          <span>{{ total }} </span>
                          <span>
                            Checkout
                            <i class="fas fa-long-arrow-alt-right ms-2"></i
                          ></span>
                        </div>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
export default {
  components: {},
  data() {
    return {
      product: [],
      shipping: random(10, 20),

      items_count: 0,
    };
  },
  methods: {
    incrementQuantity(index) {
      this.product[index].quantity += 1;
    },
    decrementQuantity(index) {
      this.product[index].quantity -= 1;
    },
  },

  created() {
    axios
      .get("http://localhost:5000/products")
      .then((response) => {
        this.product = response.data.slice(0, 10);
      })
      .catch((error) => {
        console.error(error);
      });
  },
  computed: {
    total() {
      return this.shipping + this.subtotal;
    },
    userNameUpdate() {
      return localStorage.getItem("userName");
    },
    filteredBlogs: function () {
      return this.product.filter((product) => {
        return product.user
          .toLowerCase()
          .match(this.userNameUpdate.toLowerCase());
      });
    },
    subtotal() {
      return this.product.reduce((total, product) => {
        return total + product.price * product.quantity;
      }, 0);
    },
  },
};
</script>

<style scoped>
@media (min-width: 1025px) {
  .h-custom {
    height: 100vh !important;
  }
}
.continue-shopping-link {
  color: inherit; /* or any other color you prefer */
  text-decoration: none;
}
</style>
