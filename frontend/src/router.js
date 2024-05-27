import { createRouter, createWebHistory } from 'vue-router'

import Main from "@/views/MainPage.vue"
import About from "@/views/AboutPage.vue"
import QuestionsPage from "@/views/QuestionsPage.vue"
import AddTheme from "@/views/AddTheme.vue"

const routes = [
    {
        path: "/",
        name: "Main",
        component: Main
    },
    {
        path: "/about/",
        name: "About",
        component: About
    },
    {
        path: "/questions/:id",
        name: "Questions",
        component: QuestionsPage,
        props: true
    },
    {
        path: "/add/theme/",
        name: "AddTheme",
        component: AddTheme
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router