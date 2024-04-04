<template>
  <div>
    <particles-bg type="lines" :bg="true" />

    <section>
      <nav
        class="navbar navbar-expand-md navbar-light pt-5 pb-4 gradient-custom"
      >
        <div class="container-xxl">
          <!-- navbar brand / title -->
          <a class="navbar-brand" href="#intro">
            <span class="text-secondary fw-bold">
              <router-link to="/" id="myLink" class="bi bi-book-half"
                >Candy shop</router-link
              >
            </span>
          </a>

          <!-- <router-link to="/signup" class="text-white-50 fw-bold"
            >Sign Up</router-link
          > -->
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

                <!-- if user is logged in route the user to /add else stay at /login -->
                <template v-if="success">
                  <router-link
                    to="/add"
                    exact
                    class="btn btn-secondary mx-3 btn-md"
                    >Add Products</router-link
                  >
                </template>

                <!-- <template v-else>
                  <router-link
                    to="/login"
                    exact
                    class="btn btn-secondary mx-3 btn-md"
                    >Add Products</router-link
                  >
                </template> -->

                <template v-else>
                  <!-- Button trigger modal -->
                  <button
                    type="button"
                    class="btn btn-secondary mx-3 btn-md"
                    data-bs-toggle="modal"
                    data-bs-target="#exampleModalCenter"
                  >
                    Add Products
                  </button>

                  <!-- Modal -->
                  <div
                    class="modal fade"
                    id="exampleModalCenter"
                    tabindex="-1"
                    role="dialog"
                    aria-labelledby="exampleModalCenterTitle"
                    aria-hidden="true"
                  >
                    <div
                      class="modal-dialog modal-dialog-centered"
                      role="document"
                    >
                      <div class="modal-content">
                        <div class="modal-header">
                          <h5 class="modal-title" id="exampleModalLongTitle">
                            Forgot to login in?
                          </h5>
                          <button
                            type="button"
                            class="close"
                            data-bs-dismiss="modal"
                            aria-label="Close"
                          >
                            <span aria-hidden="true">&times;</span>
                          </button>
                        </div>
                        <div class="modal-body">
                          Please login to access this page.
                        </div>
                        <div class="modal-footer">
                          <button
                            type="button"
                            class="btn btn-secondary"
                            data-bs-dismiss="modal"
                          >
                            Close
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </template>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </section>
    <section class="vh-100 gradient-custom">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div
              id="loginPage"
              class="card bg-dark text-white"
              style="border-radius: 1rem"
            >
              <div class="card-body p-5 text-center">
                <div class="mb-md-5 mt-md-4 pb-5">
                  <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                  <p class="text-white-0 mb-5 font-weight-bold">
                    Please enter you user name and password!
                  </p>

                  <!-- Validations -->
                  <b-form-group
                    id="fieldset-1"
                    description="Let us know your name."
                    label="User name"
                    label-for="input-1"
                    valid-feedback="Thank you!"
                    :invalid-feedback="invalidFeedbackUserName"
                    :state="stateUserName"
                  >
                    <b-form-input
                      id="input-1"
                      v-model="userName"
                      :state="stateUserName"
                      trim
                    ></b-form-input>
                    <!-- <h1>{{ userName }}</h1> -->
                  </b-form-group>

                  <b-form-group
                    id="fieldset-2"
                    description="Let us know your Password."
                    label="Password"
                    label-for="input-2"
                    valid-feedback="Thank you!"
                    :invalid-feedback="invalidFeedbackPassword"
                    :state="statePassword"
                  >
                    <b-form-input
                      id="input-2"
                      v-model="password"
                      :state="statePassword"
                      trim
                    ></b-form-input>
                    <!-- <small id="passwordHelpInline" class="text-muted">
                      Must be 8-20 characters long.
                    </small> -->
                  </b-form-group>
                  <!-- Validations -->

                  <button
                    class="btn btn-primary btn-md px-5"
                    type="submit"
                    @click="loginUser(userName)"
                  >
                    Login
                  </button>
                  <p>{{ userMsg }}</p>

                  <div
                    class="d-flex justify-content-center text-center mt-4 pt-1"
                  >
                    <a href="#!" class="text-white"
                      ><i class="fab fa-facebook-f fa-lg"></i
                    ></a>
                    <a href="#!" class="text-white"
                      ><i class="fab fa-twitter fa-lg mx-4 px-2"></i
                    ></a>
                    <a href="#!" class="text-white"
                      ><i class="fab fa-google fa-lg"></i
                    ></a>
                  </div>
                </div>

                <div>
                  <p class="mb-0">
                    Don't have an account?
                    <router-link to="/signup" class="text-white-50 fw-bold"
                      >Sign Up</router-link
                    >
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      userName: "",
      password: "",
      success: false,
      userMsg: "",
    };
  },
  methods: {
    updateUserName(userName) {
      this.$store.commit("setUserName", userName);
    },
    loginUser() {
      console.log("loginUser function called");
      console.log("user name: " + this.userName + " password:" + this.password);
      axios
        .post("http://localhost:5000/login", {
          userName: this.userName,
          password: this.password,
        })
        .then((response) => {
          console.log("here is your response");
          console.log(response);
          console.log(response.data.status);
          if (response.data.status === "success") {
            this.success = true;
            console.log("User logged in successfully " + this.success);
            this.userMsg = "User logged in successfully!!!";
            localStorage.setItem("userName", this.userName);
          } else {
            this.success = false;
            console.log("user logged in Failed " + this.success);
            this.userMsg = "Please Enter a valid user!!!";
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  computed: {
    stateUserName() {
      return this.userName.length >= 4;
    },
    invalidFeedbackUserName() {
      if (this.userName.length > 0) {
        return "Enter at least 4 characters.";
      }
      return "Enter a valid user name.";
    },
    statePassword() {
      return this.password.length >= 9;
    },
    invalidFeedbackPassword() {
      if (this.password.length > 0) {
        return "Invalid password";
      }
      return "Password must at least 8 charecter.";
    },
  },
};
</script>

<style scoped>
/* .gradient-custom {
  background: #6a11cb;

  background: -webkit-linear-gradient(
    to right,
    rgb(255, 210, 180),
    rgba(37, 117, 252, 1)
  );

  background: linear-gradient(to right, rgb(118, 253, 253), rgb(255, 166, 251));
} */
#myLink {
  color: inherit;
  text-decoration: none;
}
</style>
