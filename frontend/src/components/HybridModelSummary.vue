<template>
  <h2 :class="['model-name q-mt-sm q-mb-xs', { 'model-name-hovered': hovered }]">{{ model.name }}</h2>
  <div class="model-description">{{ model.description }}</div>
  <div class="q-mt-md">
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
  <div v-if="model.created" class="q-mt-sm model-date">
    <q-icon name="event" class="q-mr-xs" />
      <span>Created on {{ model.created }}</span>
  </div>
  <div class="q-mt-sm">
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

<style scoped>
.model-name {
  font-size: 1.5rem;
  font-weight: bold;
  line-height: 1.5;
}

.model-name-hovered {
  text-decoration: underline;
}

.model-description {
  font-size: 1rem;
}

.keyword {
  font-size: 0.8rem;
}

.model-date {
  display: flex;
  align-items: center;
  font-size: 0.8rem;
  color: grey;
}
</style>
