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

    <!-- main image & intro text -->
    <section id="intro">
      <div class="container-lg">
        <div class="row g-4 justify-content-center align-items-center">
          <div class="col-md-5 text-center text-md-start">
            <h1>
              <div class="display-2">Candy lovers</div>
              <div class="display-5 text-muted">Your haven!</div>
            </h1>
            <p class="lead my-4 text-muted">
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Laboriosam, dignissimos?
            </p>
            <a href="#pricing" class="btn btn-secondary btn-md mx-3"
              >Subscribe Now</a
            >
            <router-link class="btn btn-secondary" to="/products" exact
              >To products</router-link
            >
            <!-- open sidebar / offcanvas -->
          </div>
          <div class="col-md-5 text-center d-none d-md-block">
            <!-- tooltip -->
            <span
              class="tt"
              data-bs-placement="bottom"
              title="Net Ninja Pro book cover"
            >
              <img
                src="../assets/cotton-candy-main.jpg"
                class="img-fluid rounded shadow-lg"
                alt="ebook"
              />
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- topics at a glance -->
    <section id="topics">
      <div class="container-md">
        <div class="text-center">
          <h2>A safe place for buying and selling your favourite candy</h2>
          <p class="lead text-muted">A quick glance</p>
        </div>
        <div class="row my-5 g-5 justify-content-around align-items-center">
          <div class="col-6 col-lg-4">
            <img
              src="../assets/candy-child.jpg"
              class="img-fluid rounded"
              alt="ebook"
            />
          </div>
          <div class="col-lg-6">
            <!-- accordion -->
            <div class="accordion" id="chapters">
              <div class="accordion-item">
                <h2 class="accordion-header" id="heading-1">
                  <button
                    class="accordion-button"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#chapter-1"
                    aria-expanded="true"
                    aria-controls="chapter-1"
                  >
                    Seller Support
                  </button>
                </h2>
                <div
                  id="chapter-1"
                  class="accordion-collapse collapse show"
                  aria-labelledby="heading-1"
                  data-bs-parent="#chapters"
                >
                  <div class="accordion-body">
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header" id="heading-2">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#chapter-2"
                    aria-expanded="false"
                    aria-controls="chapter-2"
                  >
                    Trust and Credibility
                  </button>
                </h2>
                <div
                  id="chapter-2"
                  class="accordion-collapse collapse"
                  aria-labelledby="heading-2"
                  data-bs-parent="#chapters"
                >
                  <div class="accordion-body">
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header" id="heading-3">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#chapter-3"
                    aria-expanded="false"
                    aria-controls="chapter-1"
                  >
                    Large Customer Base
                  </button>
                </h2>
                <div
                  id="chapter-3"
                  class="accordion-collapse collapse"
                  aria-labelledby="heading-3"
                  data-bs-parent="#chapters"
                >
                  <div class="accordion-body">
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header" id="heading-4">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#chapter-4"
                    aria-expanded="false"
                    aria-controls="chapter-4"
                  >
                    Your safety is our priority
                  </button>
                </h2>
                <div
                  id="chapter-4"
                  class="accordion-collapse collapse"
                  aria-labelledby="heading-4"
                  data-bs-parent="#chapters"
                >
                  <div class="accordion-body">
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                  </div>
                </div>
              </div>
              <div class="accordion-item">
                <h2 class="accordion-header" id="heading-5">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#chapter-5"
                    aria-expanded="false"
                    aria-controls="chapter-5"
                  >
                    Customer Reviews
                  </button>
                </h2>
                <div
                  id="chapter-5"
                  class="accordion-collapse collapse"
                  aria-labelledby="heading-5"
                  data-bs-parent="#chapters"
                >
                  <div class="accordion-body">
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                    <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                      Quis assumenda delectus sapiente quidem consequatur odit
                      adipisci necessitatibus nemo aliquid minus modi tempore
                      quibusdam quas vitae, animi ipsam nulla sunt alias.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- reviews list -->
    <section id="reviews" class="bg-light">
      <div class="container-lg">
        <div class="text-center">
          <h2><i class="bi bi-stars"></i>Retailers Reviews</h2>
          <p class="lead">
            What are our customers have said about the blalala...
          </p>
        </div>

        <div class="row justify-content-center my-5">
          <div class="col-lg-8">
            <div class="list-group">
              <div class="list-group-item py-3">
                <div class="pb-2">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                </div>
                <h5 class="mb-1">
                  Chocoholic's Dream - Unwrapping Joy at the Candy Shop
                </h5>
                <p class="mb-1">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Tenetur error veniam sit expedita est illo maiores neque quos
                  nesciunt, reprehenderit autem odio commodi labore praesentium
                  voluptate repellat in id quisquam.
                </p>
                <small>Review by Mario</small>
              </div>
              <div class="list-group-item py-3">
                <div class="pb-2">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                </div>
                <h5 class="mb-1">
                  Gummy Galore - A Sugary Expedition through the Candy Shop's
                  Wonderland
                </h5>
                <p class="mb-1">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Tenetur error veniam sit expedita est illo maiores neque quos
                  nesciunt, reprehenderit autem odio commodi labore praesentium
                  voluptate repellat in id quisquam.
                </p>
                <small>Review by Mario</small>
              </div>
              <div class="list-group-item py-3">
                <div class="pb-2">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-half"></i>
                </div>
                <h5 class="mb-1">
                  Lollipop Love - Savoring Sweetness with the Candy Shop's
                  Delectable Finds
                </h5>
                <p class="mb-1">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Tenetur error veniam sit expedita est illo maiores neque quos
                  nesciunt, reprehenderit autem odio commodi labore praesentium
                  voluptate repellat in id quisquam.
                </p>
                <small>Review by Mario</small>
              </div>
              <div class="list-group-item py-3">
                <div class="pb-2">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                </div>
                <h5 class="mb-1">
                  Jawbreaker Jamboree - Breaking Open Fun at the Candy Shop's
                  Fiesta
                </h5>
                <p class="mb-1">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Tenetur error veniam sit expedita est illo maiores neque quos
                  nesciunt, reprehenderit autem odio commodi labore praesentium
                  voluptate repellat in id quisquam.
                </p>
                <small>Review by Mario</small>
              </div>
              <div class="list-group-item py-3">
                <div class="pb-2">
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-fill"></i>
                  <i class="bi bi-star-half"></i>
                </div>
                <h5 class="mb-1">
                  Caramel Carnival - Whirling Delight at the Candy Shop's Sweet
                  Extravaganza
                </h5>
                <p class="mb-1">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Tenetur error veniam sit expedita est illo maiores neque quos
                  nesciunt, reprehenderit autem odio commodi labore praesentium
                  voluptate repellat in id quisquam.
                </p>
                <small>Review by Mario</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "mainPage",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
    };
  },
};
</script>

<style scoped>
section {
  padding: 60px 0;
}
</style>
