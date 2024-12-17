<template>
  <q-page>
    <div class="container">
      <q-card v-if="hybridModel" flat class="q-mb-xl">
        <UnitFullAbstract unitType="hybrid_model" :unit="hybridModel" />

        <MetadataTable :data="otherMetadata" class="q-mb-lg" />

        <q-expansion-item
          v-if="hybridModel.latent_variables?.length"
          icon="refresh"
          label="Latent variables"
        >
          <template
            v-for="(variable, index) in hybridModel.latent_variables"
            :key="index"
          >
            <DataProperties :data="variable" />
          </template>
          <div class="q-mb-lg" />
        </q-expansion-item>

        <q-expansion-item
          v-if="hybridModel.data?.inputs?.length"
          icon="login"
          label="Input variables"
        >
          <template
            v-for="(variable, index) in hybridModel.data.inputs"
            :key="index"
          >
            <DataProperties :data="variable" />
          </template>
          <div class="q-mb-lg" />
        </q-expansion-item>

        <q-expansion-item
          v-if="hybridModel.data?.outputs?.length"
          icon="logout"
          label="Output variables"
        >
          <template
            v-for="(variable, index) in hybridModel.data.outputs"
            :key="index"
          >
            <DataProperties :data="variable" />
          </template>
          <div class="q-mb-lg" />
        </q-expansion-item>
      </q-card>

      <q-card v-else flat class="q-mt-md">
        <p><q-spinner /> Loading hybrid model data...</p>
      </q-card>

      <q-card v-if="PhysicsBasedComponents.length" flat>
        <h2 class="q-mt-lg q-mb-sm">
          <q-icon name="settings" class="q-mr-sm" />Physics-Based Components
        </h2>
        <UnitList
          unitType="physics_based_component"
          :units="PhysicsBasedComponents"
        />
      </q-card>

      <q-card v-if="MachineLearningComponents.length" flat>
        <h2 class="q-mt-lg q-mb-sm">
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
import DataProperties from 'src/components/DataProperties.vue';
import UnitList from 'src/components/UnitList.vue';

const route = useRoute();
const modelId = route.params.modelId;
const hybridModel = ref<HybridModel>();
const otherMetadata = ref<{ property: string; value: any }[]>([]);
const PhysicsBasedComponents = ref<PhysicsBasedComponentSummary[]>([]);
const MachineLearningComponents = ref<MachineLearningComponentSummary[]>([]);

const getHybridModel = () => {
  api
    .get(`/hybrid_models/${modelId}`)
    .then((response) => {
      hybridModel.value = response.data;
      otherMetadata.value = [
        { property: 'Documentation', value: hybridModel.value?.documentation },
        { property: 'Identifier', value: hybridModel.value?.identifier },
        { property: 'URL', value: hybridModel.value?.url },
        { property: 'Version', value: hybridModel.value?.version },
        { property: 'Host Physics', value: hybridModel.value?.host_physics },
        { property: 'ML Process', value: hybridModel.value?.ml_process },
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
