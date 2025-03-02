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
              <form @submit.prevent="guardarAire">
                <div class="mb-3" >
                  <label class="form-label">Nombre</label>
                  <input 
                    v-model="aire.nombre" 
                    placeholder="Nombre" 
                    class="form-control"
                    required 
                  />
                </div>
                <div class="mb-3" >
                  <label class="form-label">Salon</label>
                  <select 
                    v-model="aire.salon_id"
                    class="form-control" >
                      <option v-for="salon in salones" :value="salon.id">{{ salon.nombre }}</option>
                  </select>
                </div>
                <button 
                  type="submit"
                  class="btn btn-primary">{{ esEdicion ? 'Actualizar' : 'Guardar' }}</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import api from "../../services/api";
import { useRouter, useRoute } from 'vue-router'
  
export default {
    data() {
      return {
        esEdicion: false,
        router: useRouter(),
        route: useRoute(),
        salones: [],
        aire: { nombre: "", salon_id: null },
      };
    },
    methods: {
      async obtenerSalones(){
        const response = await api.get("/salones/");
        this.salones = response.data;
      },
      async guardarAire() {
        if(this.esEdicion){
            await api.put(`/aires/${this.aire.id}/`, this.aire);
        }else{
            await api.post("/aires/", this.aire);
        }
        this.router.push("/aires");
      },
      async cargarAire(){
        const response = await api.get(`/aires/${this.route.params.id}`);
        this.aire = response.data;
      }
    },
    mounted() {
      this.obtenerSalones();
      if(this.route.params.id){
        this.esEdicion = true;
        this.cargarAire();
      }
    },
}  
</script>