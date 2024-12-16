<template>
  <h3 class="q-mb-md">{{ props.data.name }}</h3>

  <MetadataTable :data="properties" class="q-mb-lg" />

  <q-expansion-item
    v-if="data.training_resources"
    icon="train"
    label="Training resources"
  >
    <ComputationalResources :data="data.training_resources" />
    <div class="q-mb-lg" />
  </q-expansion-item>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { NeuralNetwork } from 'src/models/machine_learning_component';
import MetadataTable from 'src/components/MetadataTable.vue';
import ComputationalResources from 'src/components/ComputationalResources.vue';

const props = defineProps({
  data: {
    type: Object as PropType<NeuralNetwork>,
    required: true,
  },
});

const properties = [
  { property: 'Type', value: props.data.type },
  { property: 'Layer count', value: props.data.layer_count },
  { property: 'Node count', value: props.data.node_count },
  { property: 'Batch size', value: props.data.batch_size },
  { property: 'Learning rate', value: props.data.learning_rate },
  { property: 'Predictor count', value: props.data.predictor_count },
  { property: 'Activation functions', value: props.data.activation_functions },
  { property: 'Input scaling', value: props.data.input_scaling },
  { property: 'Initialization', value: props.data.initialization },
  { property: 'Loss function', value: props.data.loss_function },
  { property: 'Regularization', value: props.data.regularization },
  { property: 'Optimization_method', value: props.data.optimization_method },
  { property: 'Host physics_model', value: props.data.host_physics_model },
  { property: 'Target variables', value: props.data.target_variables },
];
</script>
