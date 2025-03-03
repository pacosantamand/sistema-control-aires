<template>
    <div class="container">
      <h2 class="text-center my-4">Bitacora de operaciones</h2>
      <div class="row">
        <div class="col-md-8 offset-md-2">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Datos de la busqueda</h5>
            </div>
            <div class="card-body">
                <div class="mb-3" >
                  <label for="tipoBusqueda" class="form-label">Tipo de busqueda </label>
                  <select
                    v-model="tipoBusqueda" 
                    class="form-control"
                    @change="cambiaOpcion"
                    id="tipoBusqueda">
                        <option v-for="(opcion, index) in opciones" :value="opciones[index]">{{ opcion }}</option>
                  </select>
                </div>
                <div v-if="tipoBusqueda==opciones[1]" class="row mb-3">
                    <div class="col-md-6">
                        <input 
                            v-model="fecha"
                            placeholder="dd/mm/aaaa" 
                            class="form-control"
                            required 
                        />
                    </div>
                    <div class="col-md-6 d-grid">
                        <button class="btn btn-secondary" @click="obtenerBitacoraPorDia">Buscar</button>
                    </div>
                </div>
                <div v-if="tipoBusqueda==opciones[2]" class="row mb-3">
                    <div class="row">
                        <div class="col-md-4">
                            <label for="desde" class="form-label">Desde </label>
                        </div>
                        <div class="col-md-4">
                            <label for="desde" class="form-label">Hasta </label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-4">
                            <input 
                                v-model="fecha_inicio"
                                placeholder="dd/mm/aaaa" 
                                class="form-control col-md-4"
                                id="desde"
                                required 
                            />
                        </div>
                        <div class="col-md-4">
                            <input 
                                v-model="fecha_fin"
                                placeholder="dd/mm/aaa" 
                                class="form-control"
                                id="hasta"
                                required 
                            />
                        </div>
                        <div class="col-md-4 d-grid">
                            <button class="btn btn-secondary" @click="obtenerBitacoraRango">Buscar</button>
                        </div>
                    </div>
                </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-md-10 offset-md-1">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Eventos ocurridos en el periodo</h5>
            </div>
            <table class="table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th></th>
                  <th>Salon</th>
                  <th>Razón</th>
                  <th>Usuario</th>
                  <th>Fecha</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="bita in bitacora" :key="bitacora.id">
                  <td>{{ bita.id }}</td>
                  <td v-if="bita.accion=='encender'"><span class="badge text-bg-success">Encendido</span></td>
                  <td v-else><span class="badge text-bg-danger">Apagado</span></td>
                  <td>{{ bita.aire.salon_id }}</td>
                  <td>{{ bita.razon }}</td>
                  <td>{{ bita.usuario.nombre }}</td>
                  <td>{{ bita.fecha }}</td>
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
        bitacora: [],
        tipoBusqueda: "",
        opciones: ["Todos","Por día", "Por rango de fecha"],
        fecha: "",
        fecha_inicio: "",
        fecha_fin: ""
      };
    },
    methods: {
      async obtenerBitacora() {
        const response = await api.get("/bitacora/");
        this.bitacora = response.data;
      },
      async obtenerBitacoraPorDia(){
        const response = await api.get(`/bitacora/dia/${this.fecha}`);
        this.bitacora = response.data;
      },
      async obtenerBitacoraRango(){
        const response = await api.get(`/bitacora/desde/${this.fecha_inicio}/hasta/${this.fecha_fin}`);
        this.bitacora = response.data;
      },
      cambiaOpcion(event) {
        if(this.tipoBusqueda==this.opciones[0]){
          this.fecha="";
          this.fecha_inicio="";
          this.ficha_fin="";
          this.obtenerBitacora();
        }
      }
    },
    mounted() {
      this.obtenerBitacora();
    },
  };
  </script>