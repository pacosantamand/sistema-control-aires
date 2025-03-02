<template>
  <div class="container">
    <h2 class="text-center my-4">Registro de usuarios</h2>
    <div class="row">
      <div class="col-md-4 offset-md-1">
        <button class="btn btn-primary" @click="router.push('/usuarios/nuevo')">Crear usuario</button>
      </div>
    </div>
    <div class="row mt-4">
        <div class="col-md-10 offset-md-1">
          <div class="card">
            <div class="card-header">              
              <h5 class="card-title">Usuarios registrados</h5>
            </div>
            <table class="table table-hover">
              <thead class="bg-success">
                <tr >
                  <th >ID</th>
                  <th >Nombre</th>
                  <th> Email</th>
                  <th>Rol</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="usuario in usuarios" :key="usuario.id">
                  <td >{{ usuario.id }}</td>
                  <td >{{ usuario.nombre }}</td>
                  <td> {{ usuario.email }}</td>
                  <td> {{ usuario.rol }}</td>
                  <td >
                    <button class="btn btn-sm btn-warning mx-1" @click="actualizarUsuario(usuario.id)" >Actualizar</button>
                    <button class="btn btn-sm btn-danger mx-1" @click="eliminarUsuario(usuario.id)">Eliminar</button>
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
    data() {
      return {
        usuarios: [],
        router: useRouter(),
      };
    },
    methods: {

      async obtenerUsuarios(){
        const response = await api.get("/usuarios/");
        this.usuarios = response.data;
      },

      async eliminarUsuario(id){
        await api.delete(`/usuarios/${id}`);
        this.obtenerUsuarios();
      },
      actualizarUsuario(id){
        this.router.push(`/usuarios/editar/${id}`);
      }

    },
    mounted() {
        this.obtenerUsuarios();
    },
  };
  </script>