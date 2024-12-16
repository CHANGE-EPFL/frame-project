<template>
  <q-page>
    <div class="container">
      <q-card v-if="machineLearningComponent" flat class="q-mb-xl">
        <UnitFullAbstract
          unitType="machine_learning_component"
          :unit="machineLearningComponent"
        />

        <MetadataTable :data="otherMetadata" class="q-mb-lg" />
      </q-card>

      <q-card v-else flat>
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
import MetadataTable from 'src/components/MetadataTable.vue';

const route = useRoute();
const componentId = route.params.componentId;
const machineLearningComponent = ref<MachineLearningComponent>();
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
        // { property: 'Type', value: machineLearningComponent.value?.type },
        // { property: 'Layer count', value: machineLearningComponent.value?.layer_count },
        // { property: 'Node count', value: machineLearningComponent.value?.node_count },
        // { property: 'Batch size', value: machineLearningComponent.value?.batch_size },
        // { property: 'Learning rate', value: machineLearningComponent.value?.learning_rate },
        // { property: 'Predictor count', value: machineLearningComponent.value?.predictor_count },
        // { property: 'Activation functions', value: machineLearningComponent.value?.activation_functions },
        // { property: 'Input scaling', value: machineLearningComponent.value?.input_scaling },
        // { property: 'Initialization', value: machineLearningComponent.value?.initialization },
        // { property: 'Loss function', value: machineLearningComponent.value?.loss_function },
        // { property: 'Regularization', value: machineLearningComponent.value?.regularization },
        // { property: 'Optimization method', value: machineLearningComponent.value?.optimization_method },
        // { property: 'Host physics model', value: machineLearningComponent.value?.host_physics_model },
        // { property: 'Target variables', value: machineLearningComponent.value?.target_variables },
        // { property: 'Training requirements', value: machineLearningComponent.value?.training_requirements },
        // { property: 'Training resources', value: machineLearningComponent.value?.training_resources },
      ];
    })
    .catch((error) => {
      console.error(`Error fetching component with ID ${componentId}:`, error);
    });
};

onMounted(() => {
  getMachineLearningComponent();
});
</script>
