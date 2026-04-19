import { createRouter, createWebHistory } from "vue-router";
import Shark from "../components/Shark.vue";
import ToDoList from "../components/ToDoList.vue";

const routes = [
  {
    path: "/",
    name: "ToDoList",
    component: ToDoList,
  },
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
