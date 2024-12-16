<template>
  <q-page>
    <div class="container">
      <q-card v-if="model" flat>
        <h1>{{ model.name }}</h1>
        <div v-if="model.contributors" class="model-contributors">{{ model.contributors.join(', ') }}</div>
        <div class="model-description q-mt-md">{{ model.description }}</div>
        <div class="q-mt-md">
          <q-chip
            v-for="keyword in model.keywords"
            :key="keyword"
            class="q-mr-sm keyword"
            color="primary"
            text-color="white"
            >
            {{ keyword }}
          </q-chip>
        </div>
        <div v-if="model.created || model.license" class="q-mt-md model-details">
            <span v-if="model.created" class="q-mr-sm"><q-icon name="event" class="q-mr-xs" />Created on {{ model.created }}</span>
            <span v-if="model.license"><q-icon name="description" class="q-mr-xs" />License: {{ model.license }}</span>
        </div>
        <div class="q-mt-sm">
        </div>
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
