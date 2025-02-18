<script setup>

</script>

<template>
  <header>
    <nav class="dark:bg-gray-700 bg-white dark:border-gray-700 border-gray-200 w-full">
      <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto">
        <ul class="flex flex-col gap-3 p-4 md:p-0 mt-4 border rounded-lg md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-700 md:dark:bg-gray-700 dark:border-gray-700">
          <router-link class="dark:text-blue-300 block py-3 px-3 text-2xl" to="/edificios">Edificios</router-link> 
          <router-link class="dark:text-blue-300 block py-3 px-3 text-2xl" to="/salones">Salones</router-link> 
          <router-link class="dark:text-blue-300 block py-3 px-3 text-2xl" to="/aires">Aires acondicionados</router-link> 
        </ul>
        
      </div>
    </nav>
  </header>
  <main>
    <router-view />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
