<template>
    <div class="container">
        <h2 class="text-center my-4">Control de Aires</h2>
        <div class="row">
            <div class="accordion" id="accordionExample">
                <div v-for="(edificio, index) in edificios" class="accordion-item">
                    <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapse'+edificio.id" :aria-expanded="false" :aria-controls="'#collapse'+edificio.id">
                        {{edificio.nombre}}
                    </button>
                    </h2>
                    <div :id="'collapse'+edificio.id" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <div class="row">
                                <div class="col-md-2">
                                    <h3>Salones</h3>
                                </div>
                                <div class="col-md-10">
                                    <ul class="list-group list-group-flush">
                                        <li class="list-group-item" v-for="salon in edificio.salones">
                                            <div class="row">
                                                <div class="col-md-4">
                                                    <h4>{{salon.nombre}}</h4>
                                                </div>
                                                <div class="col-md-8">
                                                    <div v-for="aire in salon.aires" class="d-md-flex flex-md-row justify-content-between align-items-center">
                                                        <p class="fs-5 m-md-0">{{ aire.nombre }}</p>
                                                        <div class="form-check form-switch">
                                                            <input class="form-check-input" type="checkbox" role="switch" id="aireEstado" :checked="aire.estado"
                                                            @change="accionAire(aire.id, !aire.estado)">
                                                            <label class="form-check-label" for="aireEstado"><span :class="aire.estado ? 'text-bg-success badge':'text-bg-danger badge'">{{ aire.estado ? 'Encendido':'Apagado' }}</span></label>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import api from "../services/api";

export default {
    data(){
        return{
            edificios: [],
        }
    },
    methods:{
        async obtenerEdificios() {
            const response = await api.get("/edificios");
            this.edificios = response.data;
        },
        accionAire(id, estado){
            
        }
    },
    mounted(){
        this.obtenerEdificios();
    }
} 

</script>