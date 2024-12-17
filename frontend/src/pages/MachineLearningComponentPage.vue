<template>
  <q-page>
    <div class="container">
      <q-card v-if="machineLearningComponent" flat class="q-mb-xl">
        <UnitFullAbstract
          unitType="machine_learning_component"
          :unit="machineLearningComponent"
        />

        <template v-for="(unit, index) in hybridModels" :key="index">
          <UnitLink unitType="hybrid_model" :unit="unit" />
        </template>

        <MetadataTable :data="otherMetadata" class="q-mb-lg" />

        <template v-if="machineLearningComponent.neural_networks?.length">
          <h2 class="q-mt-lg q-mb-none">
            <q-icon name="psychology" class="q-mr-sm" /> Neural Networks
          </h2>

          <template
            v-for="(
              neuralNetwork, index
            ) in machineLearningComponent.neural_networks || []"
            :key="index"
          >
            <NeuralNetwork :data="neuralNetwork" />
          </template>
        </template>
      </q-card>

      <q-card v-else flat class="q-mt-md">
        <p><q-spinner /> Loading component data...</p>
      </q-card>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from 'src/boot/api';
import type { MachineLearningComponent } from 'src/models/machine_learning_component';
import UnitFullAbstract from 'src/components/UnitFullAbstract.vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';
import UnitLink from 'src/components/UnitLink.vue';
import MetadataTable from 'src/components/MetadataTable.vue';
import NeuralNetwork from 'src/components/NeuralNetwork.vue';

const route = useRoute();
const componentId = route.params.componentId;
const machineLearningComponent = ref<MachineLearningComponent>();
const hybridModels = ref<HybridModelSummary[]>([]);
const otherMetadata = ref<{ property: string; value: any }[]>([]);

const getMachineLearningComponent = () => {
  api
    .get(`/components/machine_learning/${componentId}`)
    .then((response) => {
      machineLearningComponent.value = response.data;
      otherMetadata.value = [
        {
          property: 'Documentation',
          value: machineLearningComponent.value?.documentation,
        },
        {
          property: 'Identifier',
          value: machineLearningComponent.value?.identifier,
        },
        { property: 'URL', value: machineLearningComponent.value?.url },
        { property: 'Version', value: machineLearningComponent.value?.version },
      ];
    })
    .catch((error) => {
      console.error(`Error fetching component with ID ${componentId}:`, error);
    });
};

const getHybridModels = () => {
  api
    .get(`/hybrid_models/machine_learning/${componentId}`)
    .then((response) => {
      hybridModels.value = response.data;
    })
    .catch((error) => {
      console.error(
        `Error fetching hybrid models for component with ID ${componentId}:`,
        error,
      );
    });
};

onMounted(() => {
  getMachineLearningComponent();
  getHybridModels();
});
</script>
