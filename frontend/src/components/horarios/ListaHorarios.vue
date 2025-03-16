<template>
    <div class="container">
        <h2 class="text-center my-4">Registro de horarios</h2>
        <div class="row">
            <div class="col-md-8 offset-md-2">
                <div class="card">
                    <div class="card-header">
                    <h5 class="card-title"></h5>
                    </div>
                    <div class="card-body">
                        <div class="mb-3" >
                            <label class="form-label">Selecciona el edificio </label>
                            <select 
                            v-model="edificio_index"
                            @change="asignaSalon()"
                            class="form-control" >
                                <option v-for="(edificio, index) in edificios" :value="index">{{ edificio.nombre }}</option>
                            </select>
                        </div>
                        <div class="mb-3" >
                            <label class="form-label">Selecciona el salón</label>
                            <select 
                            v-model="salon_index"
                            @change="asignaAires()"
                            class="form-control" >
                                <option v-for="(salon, index) in salones" :value="index">{{ salon.nombre }}</option>
                            </select>
                        </div>
                    </div>   
                </div>
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-md-4 offset-md-2">
                <button class="btn btn-primary" @click="router.push(`/horarios/${this.salon_id}/nuevo`)">Nuevo</button>
            </div>
        </div>
        <div v-if="horarios.length>0" class="row mt-4">
            <div class="col-md-8 offset-md-2">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title">Horario de uso</h5>
                    </div>
                    <table class="table table-hover">
                        <thead class="bg-success">
                            <tr>
                                <th>Día</th>
                                <th>Inicio</th>
                                <th>Fin</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="horario in horarios">
                                <td>{{ horario.dia }}</td>
                                <td>{{ horario.hora_inicio }}</td>
                                <td>{{ horario.hora_fin }}</td>
                                <td>
                                    <button class="btn btn-sm btn-danger mx-1" @click="eliminarHorarios(horario.dia)">Eliminar</button>
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
import { useRouter } from 'vue-router'

export default {
    data(){
        return {
            edificios: [],
            salones: [],
            aires: [],
            edificio_index: -1,
            salon_index: -1,
            salon_id: 0,
            aire_id: 0,
            horarios: [],
            router: useRouter(),
        };
    },
    methods:{
        async obtenerEdificios() {
            const response = await api.get("/edificios");
            this.edificios = response.data;
        },
        asignaSalon(){
            this.salones = this.edificios[this.edificio_index].salones;

        },
        asignaAires(){
            this.aires = this.salones[this.salon_index].aires;
            this.salon_id = this.salones[this.salon_index].id;
            if(this.aires.length>0){
                this.aire_id = this.aires[0].id;
                console.log(this.aire_id);
                this.obtenerHorarios()
            }else{
                this.limpiaHorarios();
            }
        },
        async obtenerHorarios(){
            const response = await api.get(`/horarios/aire/${this.aire_id}`);
            this.horarios = response.data;
        },
        async eliminarHorarios(dia){
            console.log(dia);
            for(const aire of this.aires){
                for(const h of aire.horarios){
                    if(dia === h.dia){
                        await api.delete(`/horarios/${h.id}`);
                    }
                }
            }
            this.limpiaHorarios();
            this.obtenerEdificios();
        },
        limpiaHorarios(){
            this.horarios = [];
        }
    },
    mounted(){
        this.obtenerEdificios();
    }

}


</script>