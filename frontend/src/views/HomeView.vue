<script lang="ts">
import BookItem from "@/components/BookItem.vue";
import {api} from "@/api";

export default {
  components: {
    BookItem,
  },
  data(): {
    books: Array<{
      id: number;
      name: string;
      description: string;
      image: string;
    }>;
  } {
    return {
      books: [],
    };
  },
  methods: {
    onNavigate: function (id: Number) {
      this.$router.push(`/book/${id}`);
    },
  },
  async mounted() {
    const res = await api.get("mybooks/");
    if (res.data) {
      this.books = res.data;
    }
  },
};
</script>

<template>
  <main class="wrapper">
    <div class="booklist">
      <BookItem
        v-for="(book, index) in books"
        :key="index"
        @click="onNavigate(book.id)"
        v-bind="book"
      />
    </div>
  </main>
</template>

<style scoped lang="scss">
.booklist {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
}
</style>
