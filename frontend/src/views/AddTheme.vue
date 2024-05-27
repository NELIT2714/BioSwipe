<script setup>
import { ref } from 'vue';
import axios from 'axios';

const name = ref('');
const description = ref('');
const file = ref(null);

const addTheme = async (event) => {
  event.preventDefault();

  const formData = new FormData();
  formData.append('name', name.value);
  formData.append('description', description.value);
  formData.append('picture', file.value);
  console.log(formData)

  try {
    const response = await axios.post("http://localhost:8001/api/add_theme/", formData, {
    // const response = await axios.post("http://localhost:8001/uploadfile/", formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    if (response.status === 200) {
      console.log("Theme added successfully");
      // name.value = "";
      // description.value = "";
      // file.value = null;
    } else {
      console.error('Error adding theme');
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

const handleFileChange = (event) => {
  file.value = event.target.files[0];
};
</script>

<template>
  <main>
    <form @submit="addTheme" enctype="multipart/form-data">
      <input type="text" v-model="name" name="name" id="name" placeholder="Theme name" required><br>
      <input type="text" v-model="description" name="description" id="description" placeholder="Theme description" required><br>
      <input type="file" @change="handleFileChange" name="picture" id="picture">
      <button type="submit" id="addTheme">Add theme</button>
    </form>
  </main>
</template>

<style scoped>

</style>