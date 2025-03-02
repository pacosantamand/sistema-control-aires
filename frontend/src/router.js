import { createRouter, createWebHistory } from "vue-router";
import Edificios from "./components/Edificios.vue";
import Salones from "./components/Salones.vue";
import Aires from "./components/Aires.vue"
import Bitacora from "./components/Bitacora.vue";
import ListaUsuarios from "./components/usuarios/ListaUsuarios.vue";
import FormUsuario from "./components/usuarios/FormUsuario.vue";

const routes = [
  { path: "/edificios", component: Edificios },
  { path: "/salones", component: Salones },
  { path: "/aires", component: Aires},
  { path: "/bitacora",component: Bitacora},
  { path: "/usuarios",component: ListaUsuarios},
  { path: "/usuarios/nuevo",component: FormUsuario},
  { path: '/usuarios/editar/:id', component: FormUsuario, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;