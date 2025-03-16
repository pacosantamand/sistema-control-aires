<template>
    <div class="container">
      <h2 class="text-center my-4">Registro de Horario</h2>
      <div class="row">
        <div class="col-md-8 offset-md-2">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Horario del salon - <span v-if="this.salon !=null" class="fw-bold">{{ this.salon.nombre }}</span> </h5>
            </div>
            <div class="card-body">
                <form @submit.prevent="guardarHorario">
                    <div class="mb-3" >
                        <label class="form-label">Día</label>
                        <select 
                        v-model="horario.dia"
                        class="form-control" >
                            <option v-for="dia in dias" :value="dia">{{ dia }}</option>
                        </select>
                    </div>
                    <div class="mb-3" >
                        <label class="form-label">Hora inicio</label>
                        <input 
                        v-model="horario.hora_inicio"
                        class="form-control"
                        placeholder="hora inicial"
                        required/>
                    </div>
                    <div class="mb-3" >
                        <label class="form-label">Hora fin</label>
                        <input 
                        v-model="horario.hora_fin"
                        class="form-control"
                        placeholder="hora inicial"
                        required/>
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
  
export default{
    data(){
        return {
            esEdicion: false,
            salon: null,
            dias: ["Lunes","Martes","Miércoles","Juves","Viernes","Sábado"],
            horario: {
                dia: "",
                hora_inicio: "",
                hora_fin: "",
                aire_id: null
            },
            route: useRoute(),
            router: useRouter(),
        };
    },
    methods: {
        async cargarSalon(){
            const response = await api.get(`/salones/${this.route.params.idsalon}`);
            this.salon = response.data;
            console.log(this.salon);
        },
        async guardarHorario(){
            for (const aire of this.salon.aires) {
                this.horario.aire_id = aire.id;
                await api.post("/horarios", this.horario);
            }
            this.router.push("/horarios");
        },
    },
    mounted(){
        //console.log(this.route.params.idsalon);
        this.cargarSalon();
    }
}

</script>