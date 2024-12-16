<template>
  <q-page>
    <div class="container">
      <q-card v-if="hybridModel" flat class="q-mb-xl">
        <UnitFullAbstract unitType="hybrid_model" :unit="hybridModel" />
        <MetadataTable :data="otherMetadata" />
      </q-card>
      <q-card v-else flat>
        <p><q-spinner /> Loading hybrid model data...</p>
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
import type { PhysicsBasedComponentSummary } from 'src/models/physics_based_component';
import type { MachineLearningComponentSummary } from 'src/models/machine_learning_component';
import UnitFullAbstract from 'src/components/UnitFullAbstract.vue';
import MetadataTable from 'src/components/MetadataTable.vue';
import UnitList from 'src/components/UnitList.vue';

const route = useRoute();
const modelId = route.params.modelId;
const hybridModel = ref<HybridModel>();
const otherMetadata = ref<{ property: string; value: string }[]>([]);
const PhysicsBasedComponents = ref<PhysicsBasedComponentSummary[]>([]);
const MachineLearningComponents = ref<MachineLearningComponentSummary[]>([]);

const getHybridModel = () => {
  api
    .get(`/hybrid_models/${modelId}`)
    .then((response) => {
      hybridModel.value = response.data;
      otherMetadata.value = [
        {
          property: 'Documentation',
          value: hybridModel.value?.documentation,
        },
        {
          property: 'Identifier',
          value: hybridModel.value?.identifier,
        },
        {
          property: 'URL',
          value: hybridModel.value?.url,
        },
        {
          property: 'Version',
          value: hybridModel.value?.version,
        },
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
