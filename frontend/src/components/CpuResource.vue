<template>
  <h4 class="q-mt-md q-mb-none">
    {{ data.model
    }}<span v-if="data.manufacturer"> ({{ data.manufacturer }})</span>
  </h4>
  <MetadataTable :data="properties" />
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { Cpu } from 'src/models/physics_based_component';
import MetadataTable from 'src/components/MetadataTable.vue';

const props = defineProps({
  data: {
    type: Object as PropType<Cpu>,
    required: true,
  },
});

const properties = [
  { property: 'Count', value: props.data.count },
  { property: 'Cores', value: props.data.cores },
  { property: 'Threads', value: props.data.threads },
  { property: 'Cache', value: props.data.cache },
  { property: 'Clock speed', value: props.data.clock_speed },
];
</script>
