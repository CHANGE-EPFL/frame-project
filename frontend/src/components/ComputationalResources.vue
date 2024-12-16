<template>
  <MetadataTable :data="properties" />

  <template v-if="props.data.cpus.length">
    <h4 class="q-mt-md q-mb-none">CPUs</h4>
    <template v-for="(cpu, index) in props.data.cpus" :key="index">
      <CpuResource :data="cpu" />
    </template>
  </template>

  <template v-if="props.data.gpus.length">
    <h4 class="q-mt-md q-mb-none">GPUs</h4>
    <template v-for="(gpu, index) in props.data.gpus" :key="index">
      <GpuResource :data="gpu" />
    </template>
  </template>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { ComputationalResources } from 'src/models/physics_based_component';
import MetadataTable from 'src/components/MetadataTable.vue';
import CpuResource from 'src/components/CpuResource.vue';
import GpuResource from 'src/components/GpuResource.vue';

const props = defineProps({
  data: {
    type: Object as PropType<ComputationalResources>,
    required: true,
  },
});

const properties = [
  { property: 'Memory', value: props.data.memory },
  { property: 'Storage', value: props.data.storage },
  { property: 'Software', value: props.data.software },
  { property: 'Operating system', value: props.data.operating_system },
  { property: 'Compute time', value: props.data.compute_time },
];
</script>
