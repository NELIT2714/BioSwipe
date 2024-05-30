import { createRouter, createWebHistory } from 'vue-router'

import Main from "@/views/MainPage.vue"
import About from "@/views/AboutPage.vue"
import ThemePage from "@/views/ThemePage.vue"
import AddTheme from "@/views/AddTheme.vue"
import QuestionsPage from "@/views/QuestionsPage.vue"

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
        path: "/theme/:id",
        name: "Theme",
        component: ThemePage,
        props: true
    },
    {
        path: "/theme/:id/questions",
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