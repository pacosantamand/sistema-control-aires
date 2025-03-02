<template>
    <div class="container">
      <h2 class="text-center my-4">Registro de edificios</h2>
      <div class="row">
        <div class="col-md-4 offset-md-1">
          <button class="btn btn-primary" @click="router.push('/edificios/nuevo')">Crear edificio</button>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-md-10 offset-md-1">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Edificios registrados</h5>
            </div>
            <table class="table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nombre</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="edificio in edificios" :key="edificio.id">
                  <td>{{ edificio.id }}</td>
                  <td>{{ edificio.nombre }}</td>
                  <td>
                    <button class="btn btn-sm btn-warning mx-1" @click="actualizarEdificio(edificio.id)">Actualizar</button>
                    <button class="btn btn-sm btn-danger mx-1" @click="eliminarEdificio(edificio.id)">Eliminar</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import api from "../../services/api";
  import { useRouter } from 'vue-router'
  
  export default {
    data() {
      return {
        router: useRouter(),
        edificios: [],
        nuevoEdificio: { nombre: "" },
      };
    },
    methods: {
      async obtenerEdificios() {
        const response = await api.get("/edificios/");
        this.edificios = response.data;
      },
      async eliminarEdificio(id) {
        await api.delete(`/edificios/${id}`);
        this.obtenerEdificios();
      },
      actualizarEdificio(id){
        this.router.push(`/edificios/editar/${id}`);
      }
    },
    mounted() {
      this.obtenerEdificios();
    },
  };
  </script>