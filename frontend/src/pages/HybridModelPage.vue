<template>
  <q-page>
    <div class="container">
      <q-card v-if="hybridModel" flat class="q-mb-xl">
        <h1>{{ hybridModel.name }}</h1>
        <div v-if="hybridModel.contributors" class="unit-contributors">
          {{ hybridModel.contributors.join(', ') }}
        </div>
        <div class="unit-description q-mt-md">
          {{ hybridModel.description }}
        </div>
        <div class="q-mt-md">
          <KeywordList
            unitType="hybrid_model"
            :keywords="hybridModel.keywords"
          />
        </div>
        <div
          v-if="hybridModel.created || hybridModel.license"
          class="q-mt-md unit-details"
        >
          <span v-if="hybridModel.created" class="q-mr-sm"
            ><q-icon name="event" class="q-mr-xs" />Created on
            {{ hybridModel.created }}</span
          >
          <span v-if="hybridModel.license"
            ><q-icon name="description" class="q-mr-xs" />License:
            {{ hybridModel.license }}</span
          >
        </div>
        <div class="q-mt-sm"></div>
        <PullCommand
          type="model"
          :short_name="hybridModel.short_name"
          class="q-mt-lg q-mb-lg"
        />
        <q-table
          :rows="tableData"
          :columns="columns"
          row-key="field"
          class="q-mt-md"
          flat
          bordered
          hide-header
          hide-pagination
          dense
        />
      </q-card>
      <q-card v-else flat>
        <q-spinner />
        <p>Loading hybrid model data...</p>
      </q-card>

      <q-card v-if="PhysicsBasedComponents.length" flat>
        <h2 class="q-mt-lg q-mb-none">
          <q-icon name="settings" class="q-mr-sm" />Physics-Based Components
        </h2>
        <UnitList
          unitType="physics_based_component"
          :units="PhysicsBasedComponents"
        />
      </q-card>

      <q-card v-if="MachineLearningComponents.length" flat>
        <h2 class="q-mt-lg q-mb-none">
          <q-icon name="psychology" class="q-mr-sm" />Machine Learning
          Components
        </h2>
        <UnitList
          unitType="machine_learning_component"
          :units="MachineLearningComponents"
        />
      </q-card>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from 'src/boot/api';
import type { HybridModel } from 'src/models/hybrid_model';
import KeywordList from 'src/components/KeywordList.vue';
import PullCommand from 'src/components/PullCommand.vue';
import type { PhysicsBasedComponentSummary } from 'src/models/physics_based_component';
import type { MachineLearningComponentSummary } from 'src/models/machine_learning_component';
import UnitList from 'src/components/UnitList.vue';

const route = useRoute();
const modelId = route.params.model_id; // Get model ID from route params
const hybridModel = ref<HybridModel>();
const PhysicsBasedComponents = ref<PhysicsBasedComponentSummary[]>([]);
const MachineLearningComponents = ref<MachineLearningComponentSummary[]>([]);

// Info table
const columns = [
  {
    name: 'property',
    align: 'left',
    field: (row) => row.property,
    style: 'font-weight: bold',
  },
  {
    name: 'value',
    align: 'left',
    field: (row) => row.value,
    style: 'color: grey',
  },
];

const tableData = ref<object[]>([]);

const getHybridModel = () => {
  api
    .get(`/hybrid_models/${modelId}`)
    .then((response) => {
      hybridModel.value = response.data;
      tableData.value = [
        {
          property: 'Host Physics',
          value: hybridModel.value?.host_physics,
        },
        {
          property: 'ML Process',
          value: hybridModel.value?.ml_process,
        },
      ];
    })
    .catch((error) => {
      console.error(`Error fetching model with ID ${modelId}:`, error);
    });
};

const getPhysicsBasedComponents = () => {
  api
    .get(`components/model_physics_based/${modelId}`)
    .then((response) => {
      PhysicsBasedComponents.value = response.data;
    })
    .catch((error) => {
      console.error(
        `Error fetching physics-based components for model with ID ${modelId}:`,
        error,
      );
    });
};

const getMachineLearningComponents = () => {
  api
    .get(`components/model_machine_learning/${modelId}`)
    .then((response) => {
      MachineLearningComponents.value = response.data;
    })
    .catch((error) => {
      console.error(
        `Error fetching machine learning components for model with ID ${modelId}:`,
        error,
      );
    });
};

onMounted(() => {
  getHybridModel();
  getPhysicsBasedComponents();
  getMachineLearningComponents();
});
</script>
