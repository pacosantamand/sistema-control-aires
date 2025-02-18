<template>
    <div class="container mx-auto  dark:bg-gray-800 p-4 rounded-2xl">
      <h2 class="text-2xl font-bold m-b">Salones</h2>
      <div class="p-4 rounded-lg shadow-md ">
        <form @submit.prevent="crearSalon">
          <div class="pb-4" >
            <label>Nombre </label>
            <input 
              v-model="nuevoSalon.nombre" 
              placeholder="Nombre" 
              class="w-1/2 mb-2 p-2 block border rounded-md dark:bg-gray-600"
              required 
            />
          </div>
          <div class="pb-4" >
            <label>Edificio </label>
            <select 
               v-model="nuevoSalon.edificio_id"
               class="w-1/2 mb-2 p-2 block border rounded-md dark:bg-gray-600" >
                <option v-for="edificio in edificios" :value="edificio.id">{{ edificio.nombre }}</option>
            </select>
          </div>
          <button 
            type="submit"
            class="flex-none rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
            >Agregar salon</button>
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
          <tr v-for="salon in salones" :key="salon.id">
            <td class="border p-2">{{ salon.id }}</td>
            <td class="border p-2">{{ salon.nombre }}</td>
            <td class="border p-2">
              <button class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700" @click="eliminarSalon(salon.id)">Eliminar</button>
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
        salones: [],
        edificios: [],
        nuevoSalon: { nombre: "", edificio_id: null },
      };
    },
    methods: {

      async obtenerEdificios(){
        const response = await api.get("/edificios/");
        this.edificios = response.data;
      },
      async obtenerSalones() {
        const response = await api.get("/salones/");
        this.salones = response.data;
      },
      async crearSalon() {
        console.log(this.nuevoSalon);
        await api.post("/salones/", this.nuevoSalon);
        this.nuevoSalon = { nombre: "", edificio_id: null};
        this.obtenerSalones();
      },
      async eliminarSalon(id) {
        await api.delete(`/salones/${id}`);
        this.obtenerSalones();
      },
    },
    mounted() {
      this.obtenerEdificios();    
      this.obtenerSalones();
    },
  };
  </script>