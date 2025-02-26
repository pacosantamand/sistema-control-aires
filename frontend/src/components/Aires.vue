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
                  <label class="form-label">Nombre</label>
                  <input 
                    v-model="nuevoAire.nombre" 
                    placeholder="Nombre" 
                    class="form-control"
                    required 
                  />
                </div>
                <div class="mb-3" >
                  <label class="form-label">Salon</label>
                  <select 
                    v-model="nuevoAire.salon_id"
                    class="form-control" >
                      <option v-for="salon in salones" :value="salon.id">{{ salon.nombre }}</option>
                  </select>
                </div>
                <button 
                  type="submit"
                  class="btn btn-primary">Agregar aire</button>
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
                  <td> {{ aire.salon_id }}</td>
                  <td >
                    <button class="btn btn-sm btn-warning mx-1" >Actualizar</button>
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
      async crearAire() {
        console.log(this.nuevoAire);
        await api.post("/aires/", this.nuevoAire);
        this.nuevoAire = { nombre: "", salon_id: null};
        this.obtenerAires();
      },
      async eliminarAire(id) {
        await api.delete(`/aires/${id}`);
        this.obtenerAires();
      },
    },
    mounted() {
        this.obtenerSalones();
        this.obtenerAires();    
    },
  };
  </script>