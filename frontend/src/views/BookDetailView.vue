<script lang="ts">
import BookItem from "@/components/BookItem.vue";
import BookForm from "@/components/BookForm.vue";
import {api} from "@/api";

export default {
  components: {
    BookItem,
    BookForm,
  },
  data(): {
    book: {
      id: number;
      name: string;
      description: string;
      image: string;
    } | null;
  } {
    return {
      book: null,
    };
  },
  async mounted() {
    const id = this.$route.params.id;

    if (id) {
      const res = await api.get(`mybooks/${id}`);
      this.book = res.data;
    } else {
      console.error("No book found");
    }
  },
};
</script>

<template>
  <div class="book-detail-container wrapper">
    <div class="book-detail">
      <BookItem v-bind="book" />
    </div>
    <div class="book-detail-form">
      <BookForm />
    </div>
  </div>
</template>

<style scoped lang="scss">
.book-detail-container {
  display: flex;
  gap: 20px;

  .book-detail {
    width: 340px;

    &-form {
      flex: 1;

      .book-form {
        width: 100%;
      }
    }
  }
}
</style>
