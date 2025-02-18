import { createRouter, createWebHistory } from "vue-router";
import Edificios from "./components/Edificios.vue";
import Salones from "./components/Salones.vue";
import Aires from "./components/Aires.vue"

const routes = [
  { path: "/edificios", component: Edificios },
  { path: "/salones", component: Salones },
  { path: "/aires", component: Aires}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;