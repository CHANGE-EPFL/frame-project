<template>
  <h3 :class="['model-name q-mt-md q-mb-sm', { 'model-name-hovered': hovered }]">{{ model.name }}</h3>
  <div class="model-description">{{ model.description }}</div>
  <div class="q-mt-sm">
    <q-chip
      v-for="keyword in model.keywords"
      :key="keyword"
      class="q-mr-sm keyword"
      color="primary"
      text-color="white"
      >
      {{ keyword }}
    </q-chip>
  </div>
  <div v-if="model.created" class="q-mt-sm model-details">
    <span v-if="model.created"><q-icon name="event" class="q-mr-xs" />Created on {{ model.created }}</span>
  </div>
  <div class="q-mt-md">
  </div>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';

const props = defineProps({
  model: {
    type: Object as PropType<HybridModelSummary>,
    required: true
  },
  hovered: {
    type: Boolean,
    default: false
  }
});
</script>

<style scoped lang="scss">
.model-name {
  font-weight: bold;
}

.model-name-hovered {
  text-decoration: underline;
}

.model-description {
  font-size: 0.9em;
}

</style>
