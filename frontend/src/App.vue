<script setup>

</script>

<template>
  <header>
    <nav class="mt-0 dark:bg-gray-700 bg-white dark:border-gray-700 border-gray-200 w-full">
      <div class="max-w-screen-xl flex items-center justify-evenly">
       
          <router-link class="dark:text-blue-300 block py-3 px-3 text-2xl" to="/edificios">Edificios</router-link> 
          <router-link class="dark:text-blue-300 block py-3 px-3 text-2xl" to="/salones">Salones</router-link> 
          <router-link class="dark:text-blue-300 block py-3 px-3 text-2xl" to="/aires">Aires acondicionados</router-link> 
      </div>
    </nav>
  </header>
  <main class="container">
    <router-view />
  </main>
</template>
