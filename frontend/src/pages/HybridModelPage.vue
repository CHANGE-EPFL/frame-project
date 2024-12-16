<template>
  <q-page>
    <div class="container">
      <q-card v-if="model" flat>
        <HybridModelSummaryComponent :model="model" />
      </q-card>
      <q-card v-else flat>
        <q-spinner />
        <p>Loading model data...</p>
      </q-card>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from 'src/boot/api';
import type { HybridModelSummary as HybridModel } from 'src/models/hybrid_model';
import HybridModelSummaryComponent from 'src/components/HybridModelSummary.vue';

const route = useRoute();
const modelId = route.params.model_id; // Get model ID from route params
const model = ref<HybridModel | null>(null);

const fetchModel = () => {
  api.get(`/hybrid_models/${modelId}`)
    .then(response => {
      model.value = response.data;
    })
    .catch(error => {
      console.error(`Error fetching model with ID ${modelId}:`, error);
    });
};

onMounted(() => {
  fetchModel();
});
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: 0 auto;
  padding: 16px;
}
</style>
