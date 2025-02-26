<template>
    <div class="container">
      <h2 class="text-center my-4">Registro de edificios</h2>
      <div class="row">
        <div class="col-md-8 offset-md-2">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Datos del edificio</h5>
            </div>
            <div class="card-body">
              <form @submit.prevent="crearEdificio">
                <div class="mb-3" >
                  <label for="nombre" class="form-label">Nombre </label>
                  <input 
                    v-model="nuevoEdificio.nombre" 
                    placeholder="Nombre" 
                    class="form-control"
                    id="nombre"
                    required 
                  />
                </div>
                <button 
                  type="submit"
                  class="btn btn-primary"
                  >Agregar edificio</button>
              </form>
            </div>
          </div>
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
                    <button class="btn btn-sm btn-warning mx-1" >Actualizar</button>
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