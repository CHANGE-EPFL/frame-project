<template>
  <q-card v-if="units" flat>
    <q-list class="unit-list">
      <template v-for="(unit, index) in units" :key="unit.id">
        <q-item
          clickable
          :to="`/${unitType}/${unit.id}`"
          @mouseenter="hoveredUnit = unit.id"
          @mouseleave="hoveredUnit = null"
          class="unit-item"
        >
          <UnitSummary
            :unitType="unitType"
            :unit="unit"
            :hovered="hoveredUnit === unit.id"
          />
        </q-item>
        <q-separator
          v-if="index < units.length - 1"
          spaced
          color="light-grey"
        />
      </template>
    </q-list>
  </q-card>
  <q-card v-else flat>
    <q-spinner />
    <p>Loading models data...</p>
  </q-card>
</template>

<script setup lang="ts">
import { ref, PropType } from 'vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';
import type { PhysicsBasedComponentSummary } from 'src/models/physics_based_component';
import type { MachineLearningComponent } from 'src/models/machine_learning_component';
import UnitSummary from 'src/components/UnitSummary.vue';

const hoveredUnit = ref<number | null>(null);

const props = defineProps({
  unitType: {
    type: String as PropType<
      'hybrid_model' | 'physics_based_component' | 'machine_learning_component'
    >,
    required: true,
  },
  units: {
    type: Object as PropType<
      | HybridModelSummary
      | PhysicsBasedComponentSummary
      | MachineLearningComponent
    >,
    required: true,
  },
});
</script>

<style scoped lang="scss">
.unit-item {
  flex-direction: column;
  padding: 0;
}
</style>
