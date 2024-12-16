<template>
  <q-card v-if="models" flat>
    <q-list>
      <template v-for="(model, index) in models" :key="model.id">
        <q-item
          clickable
          :to="`/hybrid_model/${model.id}`"
          @mouseenter="hoveredModel = model.id"
          @mouseleave="hoveredModel = null"
          class="model-item"
          >
          <HybridModelSummaryComponent
          :model="model"
          :hovered="hoveredModel === model.id"
          />
        </q-item>
          <q-separator
            v-if="index < models.length - 1"
            spaced
            color="light-grey"
            />
      </template>
    </q-list>
  </q-card>
  <q-card v-else flat>
    <q-spinner />
      <p>Loading models data...</p>
  </q-card>
</template>

<script setup lang="ts">
import { api } from 'src/boot/api';
import { ref, onMounted } from 'vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';
import HybridModelSummaryComponent from 'src/components/HybridModelSummary.vue';

const models = ref<HybridModelSummary[]>([]);
const hoveredModel = ref<number | null>(null);

const getHybridModels = () => {
  api.get('/hybrid_models')
    .then(response => {
      models.value = response.data;
    })
    .catch(error => {
      console.error('Error getting hybrid models metadata:', error);
    });
};

onMounted(() => {
  getHybridModels();
});
</script>

<style scoped lang="scss">
.model-item {
  flex-direction: column;
  padding: 0;
}
</style>
