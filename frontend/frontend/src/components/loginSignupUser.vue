<template>
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
                <p class="text-white-0 mb-5 font-weight-bold display-1">
                  Please enter your user name and password!
                </p>

                <div class="form-outline form-white mb-4">
                  <input
                    type="email"
                    id="typeEmailX"
                    class="form-control form-control-lg"
                    v-model="userName"
                  />
                  <label> {{ userName }}</label>
                  <label class="form-label" for="typeEmailX">User Name</label>
                </div>

                <div class="form-outline form-white mb-4">
                  <input
                    type="password"
                    id="typePasswordX"
                    class="form-control form-control-lg"
                    v-model="password"
                  />
                  <label> {{ password }}</label>

                  <label class="form-label" for="typePasswordX">Password</label>
                </div>

                <button
                  class="btn btn-primary btn-lg px-5"
                  type="submit"
                  @click="submitUser"
                >
                  Login
                </button>

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
                  <a href="#!" class="text-white-50 fw-bold">Sign Up</a>
                </p>
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

export default {
  data() {
    return {
      userName: "",
      password: "",
    };
  },
  methods: {
    submitUser() {
      console.log("submitUser");
      console.log(this.userName + " " + this.password);
      axios
        .post("http://localhost:5000/login", {
          userName: this.userName,
          password: this.password,
        })
        .then((response) => {
          console.log("here is your response");
          console.log(response);
          this.blog = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
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
  background: linear-gradient(to right, rgb(118, 253, 253), rgb(255, 166, 251));
}
</style>
