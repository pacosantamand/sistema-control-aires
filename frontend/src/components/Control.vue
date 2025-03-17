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
                                                            <input class="form-check-input" type="checkbox" role="switch" :id="'aireEstado'+aire.id" :checked="aire.estado"
                                                            @change="accionAire($event, aire.id)">
                                                            <label class="form-check-label" :for="'aireEstado'+aire.id"><span :class="aire.estado ? 'text-bg-success badge':'text-bg-danger badge'">{{ aire.estado ? 'Encendido':'Apagado' }}</span></label>
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
        <div class="modal fade" id="modalBitacora" ref="modalBitacora" tabindex="-1" aria-labelledby="modalBitacoraLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="modalBitacoraLabel">Datos de la acción</h1>
                    <button type="button" class="btn-close" @click="cancelarCambio" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form>
                    <div class="mb-3">
                        <label for="razon"  class="col-form-label">Razón:</label>
                        <textarea class="form-control" v-model="this.bitacora.razon" id="razon"></textarea>
                    </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="cancelarCambio">Cancelar</button>
                    <button type="button" class="btn btn-primary" @click="confirmarCambio">Guardar</button>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import api from "../services/api";
import { ref, onMounted, nextTick, reactive } from "vue";
import { Modal } from "bootstrap";


export default {
  setup() {
    const modalBitacora = ref(null);
    let modalInstance = null;

    const edificios = ref([]);
    const estadoTemporal = ref(false);
    const estadoReal = ref(false);
    let aireSeleccionado = null;
    const bitacora = reactive({
        aire_id: 0,
        usuario_id: 4,
        razon: "",
        accion: "",
    });

    onMounted(async () => {
      await obtenerEdificios();
      nextTick(() => {
        if (modalBitacora.value) {
            modalInstance = new Modal(modalBitacora.value);
        }
      });
    });

    const abrirModal = () => {
        if (!modalInstance && modalBitacora.value) {
            modalInstance = new Modal(modalBitacora.value);
        }
        modalInstance?.show();
    };


    const cerrarModal = () => {
      modalInstance?.hide();
    };

    const accionAire = (event, aireId) => {
      aireSeleccionado = aireId;
      estadoTemporal.value = event.target.checked;
      event.target.checked = estadoReal.value; 
      abrirModal();
    };

    const cancelarCambio = () => {
      cerrarModal();
      estadoTemporal.value = estadoReal.value; 
    };

    const confirmarCambio = async () => {
      estadoReal.value = estadoTemporal.value; 
      cerrarModal();

      try {
        await api.post(`/control_manual/${aireSeleccionado}?encender=${estadoReal.value}`);
        bitacora.aire_id = aireSeleccionado
        bitacora.accion = estadoReal.value ? 'encender':'apagar';
        console.log(bitacora);
        await api.post("/bitacora/", bitacora);
        bitacora.razon="";
        obtenerEdificios();
      } catch (error) {
        console.error("Error actualizando estado:", error);
      }
    };

    const obtenerEdificios = async () => {
      try {
        const response = await api.get("/edificios");
        edificios.value = response.data;
      } catch (error) {
        console.error("Error obteniendo edificios:", error);
      }
    };

    return {
      bitacora,
      modalBitacora,
      abrirModal,
      cerrarModal,
      edificios,
      obtenerEdificios,
      accionAire,
      cancelarCambio,
      confirmarCambio,
    };
  }
};
</script>