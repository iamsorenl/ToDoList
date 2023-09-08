import { createRouter, createWebHistory } from "vue-router";
import Shark from "../components/Shark.vue";

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
