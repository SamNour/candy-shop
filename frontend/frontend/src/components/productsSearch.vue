<template>
  <div>
    <nav class="navbar navbar-expand-md navbar-light pt-5 pb-4">
      <div class="container-xxl">
        <!-- navbar brand / title -->
        <a class="navbar-brand" href="#intro">
          <span class="text-secondary fw-bold">
            <i class="bi bi-book-half"></i>
            Candy shop
          </span>
        </a>
        <!-- toggle button for mobile nav -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#main-nav"
          aria-controls="main-nav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- navbar links -->
        <div
          class="collapse navbar-collapse justify-content-end align-center"
          id="main-nav"
        >
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#topics">About Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#reviews">Reviews</a>
            </li>

            <li class="nav-item d-md-none">
              <a class="nav-link" href="#pricing">Pricing</a>
            </li>
            <li class="nav-item ms-2 d-none d-md-inline">
              <!-- <a class="btn btn-secondary" href="">Log in</a> -->
              <router-link
                class="btn btn-secondary mx-3 btn-md"
                to="/login"
                exact
                >Log in</router-link
              >
              <router-link class="btn btn-secondary mx-3 btn-md" to="/add" exact
                >Add Products</router-link
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <section id="show-products" class="p-5">
      <div>
        <div class="row row-cols-1 row-cols-md-2 g-4">
          <div class="col">
            <div class="card">
              <img
                src="/0.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[0].title }}</h5>
                <p class="card-text">{{ product[0].body }}</p>
                <router-link v-bind:to="'/products/' + product[0].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/1.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[1].title }}</h5>
                <p class="card-text">
                  product name: {{ product[1].title }} {{ product[1].body }}
                </p>
                <router-link v-bind:to="'/products/' + product[1].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/2.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[2].title }}</h5>
                <p class="card-text">{{ product[2].body }}</p>
                <router-link v-bind:to="'/products/' + product[2].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/3.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[3].title }}</h5>
                <p class="card-text">{{ product[3].body }}</p>
                <router-link v-bind:to="'/products/' + product[3].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/4.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[4].title }}</h5>
                <p class="card-text">
                  {{ product[4].body }}
                </p>
                <router-link v-bind:to="'/products/' + product[4].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/0.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[5].title }}</h5>
                <p class="card-text">
                  {{ product[5].body }}
                </p>
                <router-link v-bind:to="'/products/' + product[5].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/1.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[6].title }}</h5>
                <p class="card-text">
                  {{ product[6].body }}
                </p>
                <router-link v-bind:to="'/products/' + product[6].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/2.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[7].title }}</h5>
                <p class="card-text">
                  {{ product[7].body }}
                </p>
                <router-link v-bind:to="'/products/' + product[6].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>

          <div class="col">
            <div class="card">
              <img
                src="/0.jpg"
                class="card-img-top img-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[8].title }}</h5>
                <p class="card-text">
                  {{ product[8].body }}
                </p>
                <router-link v-bind:to="'/products/' + product[8].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card">
              <img
                src="/0.jpg"
                class="card-img-topimg-fluid shadow-lg"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">{{ product[9].title }}</h5>
                <p class="card-text">
                  {{ product[9].body }}
                </p>
                <router-link v-bind:to="'/products/' + product[9].id">
                  <b-button variant="primary">Go somewhere</b-button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="pagenations py-3">
      <nav aria-label="...">
        <ul class="pagination pagination-sm justify-content-center">
          <li class="page-item active" aria-current="page">
            <span class="page-link">1</span>
          </li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
        </ul>
      </nav>
    </section>
    <section class="footer">copy right &copy; 2021</section>
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
    getImageUrl(imageFileName) {
      // Assuming images are in the "public" folder
      return `/public/${imageFileName}`;
    },

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
    console.log("the fetches prodcut id is ==> " + this.path);

    this.fetchPosts();
  },
  mixins: [searchMixin],
};
</script>

<style scoped>
#show-products {
  font-family: Arial, sans-serif;
  margin: 0 auto;
  max-width: 960px;
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

.footer {
  /* background-color: #f1f1f1; */
  text-align: center;
  padding: 10px;
}
</style>
