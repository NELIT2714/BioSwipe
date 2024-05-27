<script setup>
	import { onMounted, ref } from "vue"
	import axios from 'axios';

	const themes = ref([]);

	const fetchThemes = async () => {
		try {
			const response = await axios.get("http://localhost:8001/api/get_themes/");
			themes.value = response.data.themes;
			console.log(response.data.themes)
		} catch (error) {
			console.error('There has been a problem with your fetch operation:', error);
		}
	};

	onMounted(fetchThemes);
</script>

<template>
	<main>
		<section class="section">
			<div class="title">
				<h1>Tematy</h1>
			</div>
			<div class="content themes">
				<div class="themes-container">
					<div class="theme" v-for="theme in themes" :key="theme._id">
						<div class="picture">
							<img :src="`http://localhost:8001/resources/${theme.picture}`" :alt="theme.name">
						</div>
						<div class="info">
							<div class="name">{{ theme.name }}</div>
							<div class="description">{{ theme.description }}</div>
							<div class="labels">
								<div><i class="bi bi-person-fill"></i><span>{{ theme.completed }}</span></div>
								<div><i class="bi bi-eye-fill"></i><span>{{ theme.views }}</span></div>
<!--								<div><i class="bi bi-question-circle-fill"></i><span>{{ // theme.questions_count }}</span></div>-->
							</div>
						</div>
						<div class="btn-container">
							<router-link :to="{ name: 'Questions', params: { id: theme._id } }">
								<button class="primary-btn">
								Przejdź do pytań
								</button>
							</router-link>
						</div>
					</div>
				</div>
			</div>
		</section>
	</main>

	<router-view/>
</template>

<style scoped>
.themes-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;

	.theme > .picture > img {
	    width: 10rem;
        border-radius: 1rem;
		transition: .3s;
	}
	.theme > .picture > img:hover {
	    transform: translateY(-2%);
	}
}
.themes-container > .theme {
    display: flex;
    gap: 1rem;
    align-items: center;
    width: fit-content;
    padding: 1rem;
    background-color: #1919190D;
    border-radius: 1rem;
}
.themes-container > .theme > .info {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 35rem;

	.name {
	    font-size: 15pt;
	    font-weight: 600;
	}
	.labels {
	    display: flex;
        gap: 1.5rem;
        align-items: center;
	}
	.labels > div > i {
	    color: #adadad;
        font-size: 20pt;
	}
	.labels > div {
		display: flex;
	    align-items: center;
	    gap: 5px;
	}
}
</style>