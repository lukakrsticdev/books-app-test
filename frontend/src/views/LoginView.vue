<script lang="ts">
import {store} from "@/store";
import {api} from "@/api";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    onsubmit: async function (e: Event) {
      e.preventDefault();
      const res = await api.post("auth/login/", {
        username: this.username,
        password: this.password,
      });
      if (res.data) {
        localStorage.setItem("auth/token", res.data.token);
        store.commit("setToken", res.data.token);
        this.$router.push("/");
      }
    },
  },
};
</script>

<template>
  <div class="login-form wrapper">
    <form v-on:submit="onsubmit">
      <fieldset>
        <label for="username">Username</label>
        <input id="username" type="text" name="username" v-model="username" />
      </fieldset>

      <fieldset>
        <label for="password">Password</label>
        <input
          id="password"
          type="password"
          name="password"
          v-model="password"
        />
      </fieldset>

      <button class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<style scoped lang="scss">
.login-form {
  background-color: var(--color-white);
  padding: 20px;
  border-radius: 4px;
  width: 540px;
}
</style>
