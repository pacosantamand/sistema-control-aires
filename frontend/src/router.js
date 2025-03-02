import { createRouter, createWebHistory } from "vue-router";
import ListaEdificios from "./components/edificios/ListaEdificios.vue";
import ListaSalones from "./components/salones/ListaSalones.vue";
import ListaAires from "./components/aires/ListaAires.vue"
import Bitacora from "./components/Bitacora.vue";
import ListaUsuarios from "./components/usuarios/ListaUsuarios.vue";
import FormUsuario from "./components/usuarios/FormUsuario.vue";
import FormEdificios from "./components/edificios/FormEdificios.vue";
import FormSalones  from "./components/salones/FormSalones.vue";
import FormAires from "./components/aires/FormAires.vue";

const routes = [
  { path: "/edificios", component: ListaEdificios },
  { path: "/edificios/nuevo", component: FormEdificios },
  { path: "/edificios/editar/:id", component: FormEdificios, props: true },
  { path: "/salones", component: ListaSalones },
  { path: "/salones/nuevo", component: FormSalones },
  { path: "/salones/editar/:id", component: FormSalones, props: true },
  { path: "/aires", component: ListaAires},
  { path: "/aires/nuevo", component: FormAires },
  { path: "/aires/editar/:id", component: FormAires, props: true },
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