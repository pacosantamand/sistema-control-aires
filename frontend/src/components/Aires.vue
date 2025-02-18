<template>
    <div class="container mx-auto  dark:bg-gray-800 p-4 rounded-2xl">
      <h2 class="text-2xl font-bold m-b">Aires acondicionados</h2>
      <div class="p-4 rounded-lg shadow-md ">
        <form @submit.prevent="crearSalon">
          <div class="pb-4" >
            <label>Nombre</label>
            <input 
              v-model="nuevoAire.nombre" 
              placeholder="Nombre" 
              class="w-1/2 mb-2 p-2 block border rounded-md dark:bg-gray-600"
              required 
            />
          </div>
          <div class="pb-4" >
            <label>Salon</label>
            <select 
               v-model="nuevoAire.salon_id"
               class="w-1/2 mb-2 p-2 block border rounded-md dark:bg-gray-600" >
                <option v-for="salon in salones" :value="salon.id">{{ salon.nombre }}</option>
            </select>
          </div>
          <button 
            type="submit"
            class="flex-none rounded-md bg-indigo-500 px-3.5 py-2.5 text-sm font-semibold text-white shadow-xs hover:bg-indigo-400 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
            >Agregar aire</button>
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
          <tr v-for="aire in aires" :key="aire.id">
            <td class="border p-2">{{ aire.id }}</td>
            <td class="border p-2">{{ aire.nombre }}</td>
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
        aires: [],
        salones: [],
        nuevoAire: { nombre: "", salon_id: null },
      };
    },
    methods: {

      async obtenerSalones(){
        const response = await api.get("/salones/");
        this.salones = response.data;
      },
      async obtenerAires() {
        const response = await api.get("/aires/");
        this.aires = response.data;
      },
      async crearSalon() {
        console.log(this.nuevoAire);
        await api.post("/aires/", this.nuevoAire);
        this.nuevoAire = { nombre: "", salon_id: null};
        this.obtenerAires();
      },
      async eliminarAire(id) {
        await api.delete(`/aires/${id}`);
        this.obtenerAalones();
      },
    },
    mounted() {
        this.obtenerSalones();
        this.obtenerAires();    
    },
  };
  </script>