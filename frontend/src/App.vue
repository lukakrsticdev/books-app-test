<script lang="ts">
import {RouterView} from "vue-router";

import Header from "@/components/Header.vue";

export default {
  components: {
    RouterView,
    Header,
  },
};
</script>

<template>
  <Header />
  <RouterView />
</template>
