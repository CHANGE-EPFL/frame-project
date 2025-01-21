<template>
  <q-page>
    <div class="container">
      <h1>Hybrid Models</h1>
      <UnitList unitType="hybrid_model" :units="hybridModels" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { api } from 'src/boot/api';
import { ref, onMounted } from 'vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';
import UnitList from 'src/components/UnitList.vue';

const hybridModels = ref<HybridModelSummary[]>([]);

const getHybridModels = () => {
  api
    .get('/hybrid_models/')
    .then((response) => {
      hybridModels.value = response.data;
    })
    .catch((error) => {
      console.error('Error getting hybrid models metadata:', error);
    });
};

onMounted(() => {
  getHybridModels();
});
</script>
