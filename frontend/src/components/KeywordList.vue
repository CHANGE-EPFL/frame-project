<template>
  <q-chip
    v-for="keyword in keywords"
    :key="keyword"
    class="keyword"
    :color="unitType === 'hybrid_model' ? 'primary' : unitType === 'physics_based_component' ? 'secondary' : 'accent'"
    text-color="white"
  >
    {{ keyword }}
  </q-chip>
</template>

<script setup lang="ts">
import { PropType } from 'vue';

const props = defineProps({
  unitType: {
    type: String as PropType<
      'hybrid_model' | 'physics_based_component' | 'machine_learning_component'
    >,
    required: true,
  },
  keywords: {
    type: Array as PropType<string[]>,
    required: true,
  },
});
</script>
