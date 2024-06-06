<template>
    <div class="min-h-screen bg-gray-100 text-gray-900 flex justify-center">
            <h1 class="text-2xl xl:text-2xl font-extrabold">Datos de persona</h1>
            <Persona></Persona>
            <h1 class="text-2xl xl:text-2xl font-extrabold">Datos de acceso</h1>
            <Usuario></Usuario>
                <RouterLink to="/">
                <button type="submit" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">
                    Cancelar
                </button>
                </RouterLink>
    </div>
</template>

<script>
import Persona from './Persona.vue'
import Usuario from './Usuario.vue'
export default {
  components: {
    Persona,
    Usuario
  }
}
</script>