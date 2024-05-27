<script setup>
	import { useRoute } from 'vue-router'
	import { ref, computed } from 'vue'

	const route = useRoute()
	const id = route.params.id
	const fiszki = ref([
		{
			question: "Budowa układu hormonalnego",
			answer: "Układ hormonalny składa się z gruczołow dokrewnych i komórek wydzielniczych (komórek gruczołowych)" +
					"występujących w innych narządach. Zarówno gruczoły, jak i komórki wydzielają substancje nazywane " +
					"hormonami, które stymulują lub hamują czynności wybranych komórek organizmu."
		},
		{
			question: "хер",
			answer: "пшёл нах"
		}
	])

    const currentIndex = ref(0);
    const isFlipped = ref(false);

    const currentCard = computed(() => fiszki.value[currentIndex.value]);

    const flipCard = () => {
      isFlipped.value = !isFlipped.value;
    };

    const nextCard = () => {
      if (currentIndex.value < fiszki.value.length - 1) {
        currentIndex.value++;
        isFlipped.value = false;
      }
    };

    const prevCard = () => {
      if (currentIndex.value > 0) {
        currentIndex.value--;
        isFlipped.value = false;
      }
    };

</script>

<template>
	<main>
		<h1>Questions Page</h1>
		<p>Question ID: {{ id }}</p>

	    <div class="flashcard" :class="{flipped: isFlipped}" @click="flipCard">
	      <div class="flashcard-inner">
	        <div class="flashcard-front">{{ currentCard.question }}</div>
	        <div class="flashcard-back">{{ currentCard.answer }}</div>
	      </div>
	    </div>
	    <button @click="prevCard" :disabled="currentIndex === 0">Вернуться</button>
	    <button @click="nextCard" :disabled="currentIndex === fiszki.length - 1">Дальше</button>
	</main>
</template>

<style scoped>
    .flashcard {
      width: 300px;
      height: 200px;
      border: 1px solid #ccc;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      cursor: pointer;
      perspective: 1000px;
      margin-bottom: 20px;
    }
    .flashcard-inner {
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
      position: relative;
    }
    .flashcard.flipped .flashcard-inner {
      transform: rotateY(180deg);
    }
    .flashcard-front, .flashcard-back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
    }
    .flashcard-back {
      transform: rotateY(180deg);
    }
    button {
      margin: 5px;
      padding: 10px 20px;
      font-size: 16px;
    }
</style>