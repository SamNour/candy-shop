<template>
  <section class="vh-100 gradient-custom">
    <particles-bg type="thick" :bg="true" />

    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div
            id="loginPage"
            class="card bg-dark text-white"
            style="border-radius: 1rem"
          >
            <div class="card-body p-5 text-center">
              <h2 class="fw-bold mb-5 text-uppercase">SIGNUP &#128540;</h2>

              <div role="group">
                <b-row class="my-1">
                  <b-col sm="3">
                    <label for="input-live" class="col-form-label">Name:</label>
                  </b-col>
                  <b-col sm="9">
                    <b-form-input
                      id="input-live"
                      v-model="userName"
                      :state="nameState"
                      aria-describedby="input-live-help input-live-feedback"
                      placeholder="Enter your name"
                      trim
                    ></b-form-input>

                    <!-- This will only be shown if the preceding input has an invalid state -->
                    <b-form-invalid-feedback id="input-live-feedback">
                      Enter at least 3 letters
                    </b-form-invalid-feedback>

                    <!-- This is a form text block (formerly known as help block) -->
                    <b-form-text id="input-live-help"
                      >Your full name.</b-form-text
                    >
                  </b-col>
                </b-row>
                <b-row class="my-2">
                  <b-col sm="3">
                    <label for="input2-live" class="col-form-label"
                      >Password:</label
                    >
                  </b-col>
                  <b-col sm="9">
                    <b-form-input
                      id="input2-live"
                      v-model="password"
                      :state="passwordState"
                      aria-describedby="input2-live-help input-live-feedback"
                      placeholder="Enter your password"
                      trim
                    ></b-form-input>

                    <!-- This will only be shown if the preceding input has an invalid state -->
                    <b-form-invalid-feedback id="input2-live-feedback">
                      Enter atleast 8 charecter and Only [a-zA-Z0-9]
                    </b-form-invalid-feedback>

                    <!-- This is a form text block (formerly known as help block) -->
                    <b-form-text id="input2-live-help"
                      >Your Password.</b-form-text
                    >
                  </b-col>
                </b-row>
                <b-row class="my-1">
                  <b-col sm="3">
                    <label for="input-live" class="col-form-label"
                      >Location:</label
                    >
                  </b-col>
                  <b-col sm="9">
                    <b-form-input
                      id="input-live"
                      v-model="location"
                      :state="LocationState"
                      aria-describedby="input-live-help input-live-feedback"
                      placeholder="Enter your Location"
                      trim
                    ></b-form-input>

                    <!-- This will only be shown if the preceding input has an invalid state -->
                    <b-form-invalid-feedback id="input-live-feedback">
                      Enter at least 3 letters
                    </b-form-invalid-feedback>

                    <!-- This is a form text block (formerly known as help block) -->
                    <b-form-text id="input-live-help"
                      >Your full name.</b-form-text
                    >
                  </b-col>
                </b-row>
                <b-row class="my-1">
                  <b-col sm="3">
                    <label for="input-live" class="col-form-label"
                      >Email:</label
                    >
                  </b-col>
                  <b-col sm="9">
                    <b-form-input
                      id="input-live"
                      v-model="email"
                      :state="emailState"
                      aria-describedby="input-live-help input-live-feedback"
                      placeholder="Enter your email"
                      trim
                    ></b-form-input>

                    <!-- This will only be shown if the preceding input has an invalid state -->
                    <b-form-invalid-feedback id="input-live-feedback">
                      Invalid email
                    </b-form-invalid-feedback>

                    <!-- This is a form text block (formerly known as help block) -->
                    <b-form-text id="input-live-help"
                      >Your full name.</b-form-text
                    >
                  </b-col>
                  <!-- <a class="btn btn-secondary" href="">Log in</a> -->
                  <router-link
                    :to="success ? '/add' : '/signup'"
                    exact
                    class="btn btn-primary btn-md px-5"
                    type="submit"
                    @click.native="verifyAndSignup"
                  >
                    {{ success ? "Want to add a product? " : "Sign up" }}
                    <!-- Sign up {{ success ? "success" : "failed" }}
                    {{ success ? "Press me" : "Sign up" }} -->
                  </router-link>
                </b-row>
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
      location: "",
      email: "",
      success: false,
    };
  },
  methods: {
    verifed() {
      console.log("verifed() says true");
      const emailRegex =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (
        this.userName.length > 2 &&
        this.password.length > 8 &&
        this.location.length > 2 &&
        emailRegex.test(this.email)
      ) {
        this.success = true;
        console.log("verifed() says true");
      } else {
        console.log("verifed() says false");

        this.success = false;
      }
    },

    submitUser() {
      console.log("submitUser");
      console.log(this.userName + " " + this.password);
      axios
        .post("http://localhost:5000/signup", {
          userName: this.userName,
          password: this.password,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },

    verifyAndSignup() {
      this.verifed();
      console.log("verifyAndSignup");
      this.submitUser();
    },
  },
  computed: {
    nameState() {
      return this.userName.length > 2 ? true : false;
    },
    LocationState() {
      return this.location.length > 2 ? true : false;
    },
    passwordState() {
      return this.password.length > 7 ? true : false;
    },
    emailState() {
      return this.email
        .toLowerCase()
        .match(
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        )
        ? true
        : false;
      // return this.email.length > 2 ? true : false;
    },
  },
};
</script>

<style scoped>
.gradient-custom {
  /* fallback for old browsers */
  /* background: #6a11cb; */

  /* Chrome 10-25, Safari 5.1-6 */
  /* background: -webkit-linear-gradient(
    to right,
    rgb(255, 210, 180),
    rgba(37, 117, 252, 1)
  ); */

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  /* background: linear-gradient(to right, rgb(255, 255, 255), #ffcbfc); */
}
</style>
