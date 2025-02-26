<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="border-bottom navbar navbar-expand-lg bg-primary">
    <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            
            <li class="nav-item">
            <RouterLink class="nav-link" to="/edificios">Edificios</RouterLink>
            </li>
            <li class="nav-item">
            <RouterLink class="nav-link" to="/salones">Salones</RouterLink>
            </li>
            <li class="nav-item">
            <RouterLink class="nav-link" to="/aires">Aires acondicionados</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <RouterView />
</template>
