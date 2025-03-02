<template>
    <div class="container">
        <h2 class="text-center my-4">Registro de Salones</h2>
        <div class="row">
            <div class="col-md-8 offset-md-2">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title">Datos del Salon</h5>
                    </div>
                    <div class="card-body">
                        <form @submit.prevent="guardarSalon">
                        <div class="mb-3" >
                            <label class="form-label">Nombre </label>
                            <input 
                            v-model="salon.nombre" 
                            placeholder="Nombre" 
                            class="form-control"
                            required 
                            />
                        </div>
                        <div class="mb-3" >
                            <label class="form-label">Edificio </label>
                            <select 
                            v-model="salon.edificio_id"
                            class="form-control" >
                                <option v-for="edificio in edificios" :value="edificio.id">{{ edificio.nombre }}</option>
                            </select>
                        </div>
                        <button 
                            type="submit"
                            class="btn btn-primary"
                            >{{ esEdicion ? 'Actualizar' : 'Guardar' }}</button>
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
        edificios: [],
        salon: { nombre: "", edificio_id: null },
      };
    },
    methods: {
      async obtenerEdificios(){
        const response = await api.get("/edificios/");
        this.edificios = response.data;
      },
      async guardarSalon() {
        if(this.esEdicion){
            await api.put(`/salones/${this.salon.id}/`, this.salon);
        }else{
            await api.post("/salones/", this.salon);
        }
        this.router.push("/salones");
      },
      async cargarSalon(){
        const response = await api.get(`/salones/${this.route.params.id}`);
        this.salon = response.data;
      }
    },
    mounted() {
      this.obtenerEdificios();
      if(this.route.params.id){
        this.esEdicion = true;
        this.cargarSalon();
      }
    },
  };
</script>