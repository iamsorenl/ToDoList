import { createRouter, createWebHistory } from "vue-router";
import Shark from "../components/Shark.vue";
import ToDoList from "../components/ToDoList.vue";

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
  {
    path: "/ToDoList",
    name: "ToDoList",
    component: ToDoList,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
