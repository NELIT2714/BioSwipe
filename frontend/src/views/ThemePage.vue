<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const route = useRoute()
const id = ref(route.params.id)
const cards = ref([])
const currentCardIndex = ref(0)
const showBack = ref(false)

const fetchCards = async () => {
  try {
    const response = await axios.get(`http://localhost:8001/api/get_cards/${id.value}`);
    cards.value = response.data.cards || [];
    if (cards.value.length > 0) {
      currentCard.value = cards.value[0];
    }
  } catch (error) {
    console.error('Произошла ошибка при выполнении запроса:', error);
  }
};

const toggleCard = () => {
  showBack.value = !showBack.value;
};

const goBack = () => {
  if (currentCardIndex.value > 0) {
    currentCardIndex.value--;
    showBack.value = false;
    currentCard.value = cards.value[currentCardIndex.value];
  }
};

const goForward = () => {
  if (currentCardIndex.value < cards.value.length - 1) {
    currentCardIndex.value++;
    showBack.value = false;
    currentCard.value = cards.value[currentCardIndex.value];
  }
};

const currentCard = ref({ question: '', answer: '' });

onMounted(() => {
  fetchCards();
});
</script>

<template>
  <main>
    <h1>Страница вопросов</h1>
    <p>ID вопроса: {{ id }}</p>

    <div v-if="cards && cards.length > 0">
      <div class="flashcard">
        <div class="flashcard-inner" @click="toggleCard">
          <div class="flashcard-front">{{ currentCard.question }}</div>
          <div class="flashcard-back" v-if="showBack">{{ currentCard.answer }}</div>
        </div>
      </div>
      <div>
        <button @click="goBack">Назад</button>
        <button @click="toggleCard">Перевернуть</button>
        <button @click="goForward">Дальше</button>
      </div>
    </div>
    <div v-else>
      <p>Загрузка карточек...</p>
    </div>
  </main>
</template>

<style scoped>
.flashcard {
  width: 300px; /* Ширина карточки */
  height: 200px; /* Высота карточки */
  border: 1px solid #ccc; /* Граница карточки */
  border-radius: 8px; /* Скругление углов */
  margin-bottom: 20px; /* Отступ между карточками */
  perspective: 1000px; /* Перспектива для анимации переворота */
}

.flashcard-inner {
  width: 100%;
  height: 100%;
  transition: transform 0.6s; /* Анимация переворота */
  transform-style: preserve-3d; /* Сохранение 3D-пространства */
}

.flashcard:hover .flashcard-inner {
  //transform: rotateY(180deg); /* Поворот на 180 градусов при наведении */
}

.flashcard-front, .flashcard-back {
  width: 100%;
  height: 100%;
  position: absolute;
  backface-visibility: hidden; /* Скрытие задней стороны */
}

.flashcard-front {
  background-color: #ffffff; /* Цвет передней стороны */
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
}

.flashcard-back {
  background-color: #f0f0f0; /* Цвет задней стороны */
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
}

button {
  margin-top: 10px; /* Отступ сверху кнопок */
}
</style>
