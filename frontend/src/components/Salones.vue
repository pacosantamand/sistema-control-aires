<template>
  <div class="container">
    <h2 class="text-center my-4">Registro de Aires acondicionados</h2>
    <div class="row">
      <div class="col-md-8 offset-md-2">
        <div class="card">
          <div class="card-header">
            <h5 class="card-title">Datos del Aire acondicionado</h5>
          </div>
          <div class="card-body">
            <form @submit.prevent="crearSalon">
              <div class="mb-3" >
                <label class="form-label">Nombre </label>
                <input 
                  v-model="nuevoSalon.nombre" 
                  placeholder="Nombre" 
                  class="form-control"
                  required 
                />
              </div>
              <div class="mb-3" >
                <label class="form-label">Edificio </label>
                <select 
                  v-model="nuevoSalon.edificio_id"
                  class="form-control" >
                    <option v-for="edificio in edificios" :value="edificio.id">{{ edificio.nombre }}</option>
                </select>
              </div>
              <button 
                type="submit"
                class="btn btn-primary"
                >Agregar salon</button>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-4">
      <div class="col-md-10 offset-md-1">
        <div class="card">
          <div class="card-header">
            <h5 class="card-title">Aires acondicionados registrados</h5>
          </div>
          <table class="table table-hover">
            <thead>
              <tr class>
                <th>ID</th>
                <th>Nombre</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="salon in salones" :key="salon.id">
                <td>{{ salon.id }}</td>
                <td>{{ salon.nombre }}</td>
                <td>
                  <button class="mx-1 btn btn-sm btn-warning" @click="eliminarSalon(salon.id)">Actualizar</button>
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