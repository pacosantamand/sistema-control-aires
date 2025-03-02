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
                    <form @submit.prevent="guardarEdificio">
                        <div class="mb-3" >
                        <label for="nombre" class="form-label">Nombre </label>
                        <input 
                            v-model="edificio.nombre" 
                            placeholder="Nombre" 
                            class="form-control"
                            id="nombre"
                            required 
                        />
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
        edificio: { id: 0, nombre: "" },
      };
    },
    methods: {
      async guardarEdificio() {
        if(this.esEdicion){
            await api.put(`/edificios/${this.edificio.id}/`, this.edificio);
        }else{
            await api.post("/edificios/", this.edificio);
        }
        this.router.push("/edificios");
      },
      async cargarEdificio(){
        const response = await api.get(`/edificios/${this.route.params.id}`);
        this.edificio = response.data;
      }
    },
    mounted() {
        if(this.route.params.id){
            this.esEdicion = true;
            this.cargarEdificio();
        }
    },
  };
</script>