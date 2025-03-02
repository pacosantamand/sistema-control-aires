<template>
    <div class="container">
        <h2 class="text-center my-4">Registro de usuarios</h2>
        <div class="col-md-8 offset-md-2">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Datos del usuario</h5>
            </div>
            <div class="card-body">
              <form @submit.prevent="guardarUsuario">
                <div class="mb-3" >
                  <label class="form-label">Nombre</label>
                  <input 
                    v-model="usuario.nombre" 
                    placeholder="Nombre" 
                    class="form-control"
                    required 
                  />
                </div>
                <div class="mb-3" >
                  <label class="form-label">Email</label>
                  <input 
                    v-model="usuario.email" 
                    placeholder="Email" 
                    class="form-control"
                    required 
                    type="email"
                  />
                </div>
                <div class="mb-3" >
                  <label class="form-label">Password</label>
                  <input 
                    v-model="usuario.password" 
                    placeholder="Password" 
                    class="form-control"
                    required 
                    type="password"
                  />
                </div>
                <div class="mb-3" >
                  <label class="form-label">Rol</label>
                  <select 
                    v-model="usuario.rol"
                    class="form-control" >
                      <option v-for="rol in roles" :value="rol">{{ rol }}</option>
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
        roles: ["colaborador","administrador"],
        usuario: { id: 0, nombre: "", email: "", password: "", rol: "" },
      };
    },
    methods: {
      async guardarUsuario() {
        if(this.esEdicion){
            await api.put(`/usuarios/${this.usuario.id}/`, this.usuario);
        }else{
            await api.post("/usuarios/", this.usuario);
        }
        this.router.push("/usuarios");
      },
      async cargarUsuario(){
        const response = await api.get(`/usuarios/${this.route.params.id}`);
        this.usuario = response.data;
      }
    },
    mounted() {
        if(this.route.params.id){
            this.esEdicion = true;
            this.cargarUsuario();
        }
    },
  };
  </script>