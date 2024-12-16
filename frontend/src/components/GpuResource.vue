<template>
  <h5 class="q-mt-md q-mb-none">
    {{ data.model
    }}<span v-if="data.manufacturer"> ({{ data.manufacturer }})</span>
  </h5>
  <MetadataTable :data="properties" />
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { Gpu } from 'src/models/physics_based_component';
import MetadataTable from 'src/components/MetadataTable.vue';

const props = defineProps({
  data: {
    type: Object as PropType<Gpu>,
    required: true,
  },
});

const properties = [
  { property: 'Count', value: props.data.count },
  { property: 'Manufacturer', value: props.data.manufacturer },
  { property: 'Memory', value: props.data.memory },
  { property: 'Memory bandwidth', value: props.data.memory_bandwidth },
  { property: 'Clock speed', value: props.data.clock_speed },
  { property: 'Cuda cores', value: props.data.cuda_cores },
  { property: 'Tensor cores', value: props.data.tensor_cores },
  { property: 'RT cores', value: props.data.rt_cores },
  { property: 'Ray tracing', value: props.data.ray_tracing },
];
</script>
