<template>
  <q-page>
    <div class="container">
      <q-card v-if="model" flat>
        <HybridModelSummaryComponent :model="model" />
        <PullCommand :type="'model'" :short_name="model.short_name" class="q-mt-md q-mb-lg"/>
        <q-table
          :rows="tableData"
          :columns="columns"
          row-key="field"
          class="q-mt-md"
          flat bordered hide-header hide-pagination dense
        />
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
import type { HybridModel } from 'src/models/hybrid_model';
import HybridModelSummaryComponent from 'src/components/HybridModelSummary.vue';
import PullCommand from 'src/components/PullCommand.vue';

const route = useRoute();
const modelId = route.params.model_id; // Get model ID from route params
const model = ref<HybridModel | null>(null);

// Info table
const columns = [
  {
    name: 'property',
    align: 'left',
    field: row => row.property,
    style: 'font-weight: bold',
  },
  {
    name: 'value',
    align: 'left',
    field: row => row.value,
    style: 'color: grey',
  }
];

const tableData = ref<object[]>([]);

const fetchModel = () => {
  api.get(`/hybrid_models/${modelId}`)
    .then(response => {
      model.value = response.data;
      tableData.value = [
        {
          property: 'Host Physics',
          value: model.value?.host_physics
        },
        {
          property: 'ML Process',
          value: model.value?.ml_process
        },
      ];
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
