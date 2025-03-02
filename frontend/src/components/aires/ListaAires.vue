<template>
    <div class="container">
      <h2 class="text-center my-4">Registro de Aires acondicionados</h2>
      <div class="row">
        <div class="col-md-4 offset-md-1">
        <button class="btn btn-primary" @click="router.push('/aires/nuevo')">Nuevo</button>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-md-10 offset-md-1">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Aires acondicionados registrados</h5>
            </div>
            <table class="table table-hover">
              <thead class="bg-success">
                <tr >
                  <th >ID</th>
                  <th >Nombre</th>
                  <th> Salon</th>
                  <th >Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="aire in aires" :key="aire.id">
                  <td >{{ aire.id }}</td>
                  <td >{{ aire.nombre }}</td>
                  <td> {{ aire.salon.nombre }}</td>
                  <td >
                    <button class="btn btn-sm btn-warning mx-1" @click="actualizarAire(aire.id)" >Actualizar</button>
                    <button class="btn btn-sm btn-danger mx-1" @click="eliminarAire(aire.id)">Eliminar</button>
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
  import { useRouter } from "vue-router"
  
  export default {
    data() {
      return {
        router: useRouter(),
        aires: [],
        salones: [],
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
      async eliminarAire(id) {
        await api.delete(`/aires/${id}`);
        this.obtenerAires();
      },
      actualizarAire(id){
        this.router.push(`/aires/editar/${id}`);
      },
    },
    mounted() {
        this.obtenerSalones();
        this.obtenerAires();    
    },
  };
  </script>