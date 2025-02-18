<template>
    <div class="container mx-auto  dark:bg-gray-800 p-4 rounded-2xl">
      <h2 class="text-2xl font-bold m-b">Edificios</h2>
      <div class="p-4 rounded-lg shadow-md ">
        <form @submit.prevent="crearEdificio">
          <div class="pb-4" >
            <label>Nombre </label>
            <input 
              v-model="nuevoEdificio.nombre" 
              placeholder="Nombre" 
              class="mb-2 p-2 block border rounded-md dark:bg-gray-600"
              required 
            />
          </div>
          <button 
            type="submit"
            class="flex-none rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
            >Agregar edificio</button>
        </form>
      </div>
      <table class="w-full border-collapse border border-gray-300 mt-4">
        <thead>
          <tr class="bg-blue-500 text-white">
            <th class="border p-2">ID</th>
            <th class="border p-2">Nombre</th>
            <th class="border p-2">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="edificio in edificios" :key="edificio.id">
            <td class="border p-2">{{ edificio.id }}</td>
            <td class="border p-2">{{ edificio.nombre }}</td>
            <td class="border p-2">
              <button class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700" @click="eliminarEdificio(edificio.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import api from "../services/api";
  
  export default {
    data() {
      return {
        edificios: [],
        nuevoEdificio: { nombre: "" },
      };
    },
    methods: {
      async obtenerEdificios() {
        const response = await api.get("/edificios/");
        this.edificios = response.data;
      },
      async crearEdificio() {
        await api.post("/edificios/", this.nuevoEdificio);
        this.nuevoEdificio = { nombre: "" };
        this.obtenerEdificios();
      },
      async eliminarEdificio(id) {
        await api.delete(`/edificios/${id}`);
        this.obtenerEdificios();
      },
    },
    mounted() {
      this.obtenerEdificios();
    },
  };
  </script>