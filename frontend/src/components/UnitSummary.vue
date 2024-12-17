<template>
  <div>
    <h3 :class="['unit-name q-mt-lg q-mb-sm', { [hoveredClass]: hovered }]">
      {{ unit.name }}
    </h3>
    <div class="unit-description">{{ unit.description }}</div>
    <div class="q-mt-sm">
      <KeywordList :unitType="unitType" :keywords="unit.keywords" />
    </div>
    <div v-if="unit.created" class="q-mt-sm unit-details">
      <span v-if="unit.created"
        ><q-icon name="event" class="q-mr-xs" />Created on
        {{ unit.created }}</span
      >
    </div>
    <div class="q-mt-lg"></div>
  </div>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';
import type { PhysicsBasedComponentSummary } from 'src/models/physics_based_component';
import type { MachineLearningComponentSummary } from 'src/models/machine_learning_component';
import KeywordList from 'src/components/KeywordList.vue';

const props = defineProps({
  unitType: {
    type: String as PropType<
      'hybrid_model' | 'physics_based_component' | 'machine_learning_component'
    >,
    required: true,
  },
  unit: {
    type: Object as PropType<
      | HybridModelSummary
      | PhysicsBasedComponentSummary
      | MachineLearningComponentSummary
    >,
    required: true,
  },
  hovered: {
    type: Boolean,
    default: false,
  },
});

const hoveredClass = computed(() => {
  return props.unitType === 'hybrid_model'
    ? 'unit-name-hovered-primary'
    : 'unit-name-hovered-secondary';
});
</script>

<style scoped lang="scss">
.unit-description {
  font-size: 0.95em;
  color: $grey-9;
}

.unit-name-hovered-primary {
  color: $primary;
}

.unit-name-hovered-secondary {
  color: $secondary;
}
</style>
