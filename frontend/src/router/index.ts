import {createRouter, createWebHistory} from "vue-router";
import {store} from "@/store";

import HomeView from "@/views/HomeView.vue";
import LoginView from "@/views/LoginView.vue";
import AddBookView from "@/views/AddBookView.vue";
import BookDetailViewVue from "@/views/BookDetailView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/book/:id",
      name: "detail",
      component: BookDetailViewVue,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/add-book",
      name: "add-book",
      component: AddBookView,
    },
  ],
});

export default router;
