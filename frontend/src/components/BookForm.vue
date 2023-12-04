<script lang="ts">
import {api} from "@/api";

export default {
  data() {
    return {
      name: "",
      description: "",
      image: "",
    };
  },
  methods: {
    onsubmit: async function (e: Event) {
      e.preventDefault();

      if (this.$route.params.id) {
        await api.put(`mybooks/${this.$route.params.id}`, {
          name: this.name,
          description: this.description,
          image: this.image,
        });
        this.$router.push("/");
      } else {
        await api.post("mybooks/", {
          name: this.name,
          description: this.description,
          image: this.image,
        });
        this.$router.push("/");
      }
    },
  },
  async mounted() {
    const id = this.$route.params.id;

    if (id) {
      const res = await api.get(`mybooks/${id}`);
      const {name, description, image} = res.data;
      this.name = name;
      this.description = description;
      this.image = image;
    }
  },
};
</script>

<template>
  <div class="book-form wrapper">
    <form v-on:submit="onsubmit">
      <fieldset>
        <label for="name">Book Name</label>
        <input id="name" type="text" name="name" v-model="name" required />
      </fieldset>

      <fieldset>
        <label for="description">Description</label>
        <input
          id="description"
          type="text"
          name="description"
          v-model="description"
          required
        />
      </fieldset>

      <fieldset>
        <label for="image">Image URL</label>
        <input id="image" type="text" name="image" v-model="image" required />
      </fieldset>

      <button v-if="!$route.params.id" class="btn btn-primary">Create</button>
      <button v-else class="btn btn-primary">Update</button>
    </form>
  </div>
</template>

<style scoped lang="scss">
.book-form {
  background-color: var(--color-white);
  padding: 20px;
  border-radius: 4px;
  width: 540px;
}
</style>
