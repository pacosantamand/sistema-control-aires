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
                  <td>{{ formatoFecha(bita.fecha) }}</td>
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
  import { parse, format } from "date-fns"
  
  export default {
    data() {
      return {
        bitacora: [],
        tipoBusqueda: "",
        opciones: ["Todos","Por día", "Por rango de fecha"],
        fecha: "",
        fechaISO: "",
        fecha_inicio: "",
        fecha_inicioISO: "",
        fecha_fin: "",
        fecha_finISO: "",
      };
    },
    methods: {
      async obtenerBitacora() {
        const response = await api.get("/bitacora/");
        this.bitacora = response.data;
      },
      async obtenerBitacoraPorDia(){
        const partes = this.fecha.split("/");
        if (partes.length === 3) {
          this.fechaISO = `${partes[2]}-${partes[1]}-${partes[0]}`; 
        } else {
          this.fechaISO = "";
        }
        const response = await api.get(`/bitacora/dia/${this.fechaISO}`);
        this.bitacora = response.data;
      },
      async obtenerBitacoraRango(){
        const partes_inicio = this.fecha_inicio.split("/");
        if (partes_inicio.length === 3) {
          this.fecha_inicioISO = `${partes_inicio[2]}-${partes_inicio[1]}-${partes_inicio[0]}`; 
        } else {
          this.fecha_inicioISO = "";
        }
        const partes_fin = this.fecha_fin.split("/");
        if (partes_fin.length === 3) {
          this.fecha_finISO = `${partes_fin[2]}-${partes_fin[1]}-${partes_fin[0]}`; 
        } else {
          this.fecha_finISO = "";
        }

        const response = await api.get(`/bitacora/desde/${this.fecha_inicioISO}/hasta/${this.fecha_finISO}`);
        this.bitacora = response.data;
      },
      cambiaOpcion(event) {
        if(this.tipoBusqueda==this.opciones[0]){
          this.fecha="";
          this.fecha_inicio="";
          this.ficha_fin="";
          this.obtenerBitacora();
        }
      },
      formatoFecha(fechaISO) {
        if (!fechaISO) return "";
        return format(new Date(fechaISO), "dd/MM/yyyy");
      }
    },
    mounted() {
      this.obtenerBitacora();
    },
  };
  </script>