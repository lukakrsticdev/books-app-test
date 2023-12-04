<script lang="ts">
export default {
  props: {
    name: String,
    description: String,
    image: String,
  },
};
</script>

<template>
  <div class="book-item">
    <div class="book-item-image">
      <img :src="image" alt="Book" />
    </div>

    <div class="book-item-title">{{ name }}</div>

    <div class="book-item-description">
      {{ description }}
    </div>
  </div>
</template>

<style scoped lang="scss">
.book-item {
  background-color: var(--color-white);
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.12);
  border: 1px solid transparent;
  cursor: pointer;

  &:hover {
    border: 1px solid var(--color-medium-gray);
  }

  &-image {
    border-bottom: 1px solid var(--color-light-gray);
    padding-bottom: 10px;

    img {
      border-top-left-radius: 8px;
      border-top-right-radius: 8px;
      width: 100%;
    }
  }

  &-title {
    font-weight: 600;
    padding: 10px;
    padding-bottom: 0px;
  }

  &-description {
    font-size: var(--text-normal);
    padding: 10px;
  }
}
</style>
