<script lang="ts">
import {store} from "@/store";

export default {
  data() {
    return {
      isAuthenticated: store.state.token !== null,
    };
  },
  methods: {
    logout: function () {
      localStorage.removeItem("auth/token");
      store.commit("removeToken");
      this.$router.push("/login");
    },
  },
};
</script>

<template>
  <div class="header-container">
    <header class="header wrapper">
      <div class="header-left">
        <img
          alt="Book logo"
          class="logo"
          src="@/assets/logo.svg"
          width="40"
          height="40"
        />

        <div class="header-title">MYBOOKS</div>
      </div>

      <nav v-if="isAuthenticated" class="nav-items">
        <RouterLink to="/">Home</RouterLink>
        <button @click="logout">Logout</button>
      </nav>
      <nav v-else class="nav-items" />

      <div class="header-actions">
        <RouterLink
          v-if="isAuthenticated"
          class="btn btn-primary login"
          to="/add-book"
        >
          Add New Book
        </RouterLink>
        <RouterLink
          v-if="!isAuthenticated"
          class="btn btn-default login"
          to="/login"
          >Login</RouterLink
        >
      </div>
    </header>
  </div>
</template>

<style scoped lang="scss">
.header-container {
  background-color: var(--color-white);
  border-bottom: 1px solid var(--color-light-gray);
  margin-bottom: 20px;
  position: sticky;
  left: 0;
  top: 0;
  width: 100%;

  .header {
    display: flex;
    align-items: center;
    padding: 20px 0;

    &-left {
      display: flex;
      align-items: center;
      cursor: pointer;

      img {
        display: block;
      }

      .header-title {
        font-weight: 800;
        font-size: var(--text-heading);
      }
    }

    .nav-items {
      margin-left: 40px;
      flex: 1;

      a {
        text-decoration: none;
        color: var(--color-medium-black);
        padding: 10px;

        &:hover {
          text-decoration: underline;
        }
      }

      button {
        border: none;
        background-color: transparent;
        font-size: var(--text-medium);
        cursor: pointer;
        color: var(--color-medium-black);
        padding: 10px;
        margin-left: 4px;

        &:hover {
          text-decoration: underline;
        }
      }
    }

    &-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
  }
}
</style>
