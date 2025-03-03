<template>
  <div class="container">
    <h2 class="text-center my-4">Registro de Salones</h2>
    <div class="row">
        <div class="col-md-4 offset-md-1">
        <button class="btn btn-primary" @click="router.push('/salones/nuevo')">Crear salon</button>
        </div>
    </div>
    <div class="row mt-4">
      <div class="col-md-10 offset-md-1">
        <div class="card">
          <div class="card-header">
            <h5 class="card-title">Salones registrados</h5>
          </div>
          <table class="table table-hover">
            <thead>
              <tr class>
                <th>ID</th>
                <th>Nombre</th>
                <th>Edificio</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="salon in salones" :key="salon.id">
                <td>{{ salon.id }}</td>
                <td>{{ salon.nombre }}</td>
                <td>{{ salon.edificio_id }}</td>
                <td>
                  <button class="mx-1 btn btn-sm btn-warning" @click="actualizarSalon(salon.id)">Actualizar</button>
                  <button class="mx-1 btn btn-sm btn-danger" @click="eliminarSalon(salon.id)">Eliminar</button>
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
        salones: [],
        edificios: [],
      };
    },
    methods: {
      async obtenerSalones() {
        const response = await api.get("/salones/");
        this.salones = response.data;
      },
      actualizarSalon(id){
        this.router.push(`/salones/editar/${id}`);
      },
      async eliminarSalon(id) {
        await api.delete(`/salones/${id}`);
        this.obtenerSalones();
      },
    },
    mounted() {
      this.obtenerSalones();
    },
  };
  </script>