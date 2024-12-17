<template>
  <span>
    <q-icon :name="iconName" class="q-mr-xs" />
    <a :href="`${unitType}/${unit.id}`" :class="linkClass">{{ unit.name }}</a>
  </span>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';
import type { PhysicsBasedComponentSummary } from 'src/models/physics_based_component';
import type { MachineLearningComponentSummary } from 'src/models/machine_learning_component';

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
});

const linkClass = computed(() => {
  return props.unitType === 'hybrid_model'
    ? 'unit-link-model'
    : 'unit-link-component';
});

const iconName = computed(() => {
  const iconMap = {
    hybrid_model: 'thermostat',
    physics_based_component: 'settings',
    machine_learning_component: 'psychology',
  };
  return iconMap[props.unitType] || '';
});
</script>

<style scoped lang="scss">
.unit-link-model,
.unit-link-component {
  color: black;
  font-weight: bold;
  transition: color 0.3s;
}

.unit-link-model:hover {
  color: $primary;
}

.unit-link-component:hover {
  color: $secondary;
}
</style>
