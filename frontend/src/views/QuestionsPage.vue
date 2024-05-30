<script setup>
	import { useRoute } from 'vue-router'
	import { ref } from 'vue'
	import axios from 'axios'
	// import { ref, computed } from 'vue'

	const route = useRoute()
	const id = route.params.id

	const question = ref("")
	const answer = ref("")

	const addQuestion = async (event) => {
	  event.preventDefault();

	  const formData = new FormData();
	  formData.append('theme_id', id);
	  formData.append('question', question.value);
	  formData.append('answer', answer.value);
	  console.log(formData)

	  try {
	    const response = await axios.post("http://localhost:8001/api/add_question/", formData, {
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
</script>

<template>
	<main>
	    <form @submit="addQuestion" enctype="multipart/form-data">
	        <input type="text" v-model="question" name="question" id="question" placeholder="Question" required><br>
		    <textarea v-model="answer" name="answer" id="answer" placeholder="Answer" required></textarea><br>
	        <button type="submit">Add question</button>
	    </form>
	</main>
</template>

<style scoped>

</style>