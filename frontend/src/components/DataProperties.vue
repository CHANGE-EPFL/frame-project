<template>
  <h4 class="q-mt-md q-mb-none">{{ data.name }}</h4>
  <MetadataTable :data="properties" />
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { Data } from 'src/models/hybrid_model';
import MetadataTable from 'src/components/MetadataTable.vue';

const props = defineProps({
  data: {
    type: Object as PropType<Data>,
    required: true,
  },
});

const properties = [
  { property: 'Identifier', value: props.data.identifier },
  { property: 'Encoding format', value: props.data.encoding_format },
  { property: 'Identifier', value: props.data.identifier },
  { property: 'URL', value: props.data.url },
  { property: 'Quality', value: props.data.quality },
  { property: 'Units', value: props.data.units },
  { property: 'Precision', value: props.data.precision },
  { property: 'Scale', value: props.data.scale },
  { property: 'Offset', value: props.data.offset },
  { property: 'Description', value: props.data.description },
  { property: 'Min value', value: props.data.min_value },
  { property: 'Max value', value: props.data.max_value },
  { property: 'Temporal coverage', value: props.data.temporal_coverage },
  { property: 'Spatial coverage', value: props.data.spatial_coverage },
  { property: 'Spatial resolution', value: props.data.spatial_resolution },
  { property: 'Temporal resolution', value: props.data.temporal_resolution },
];
</script>
