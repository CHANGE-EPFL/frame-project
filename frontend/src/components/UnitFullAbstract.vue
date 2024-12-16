<template>
  <h1>{{ unit.name }}</h1>
  <div class="unit-type">
    {{
      {
        hybrid_model: 'Hybrid Model',
        physics_based_component: 'Physics-Based Component',
        machine_learning_component: 'Machine Learning Component',
      }[unitType]
    }}
  </div>
  <div v-if="unit.contributors" class="unit-contributors">
    {{ unit.contributors.join(', ') }}
  </div>
  <div class="unit-description q-mt-md">
    {{ unit.description }}
  </div>
  <div class="q-mt-md">
    <KeywordList :unitType="unitType" :keywords="unit.keywords" />
  </div>
  <div v-if="unit.created || unit.license" class="q-mt-md unit-details">
    <span v-if="unit.created" class="q-mr-sm"
      ><q-icon name="event" class="q-mr-xs" />Created on
      {{ unit.created }}</span
    >
    <span v-if="unit.license"
      ><q-icon name="description" class="q-mr-xs" />License:
      {{ unit.license }}</span
    >
  </div>
  <div class="q-mt-sm"></div>
  <PullCommand
    :type="unitType === 'hybrid_model' ? 'model' : 'component'"
    :short_name="unit.short_name"
    class="q-mt-lg q-mb-lg"
  />
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { HybridModel } from 'src/models/hybrid_model';
import type { PhysicsBasedComponent } from 'src/models/physics_based_component';
import type { MachineLearningComponent } from 'src/models/machine_learning_component';
import KeywordList from 'src/components/KeywordList.vue';
import PullCommand from 'src/components/PullCommand.vue';

const props = defineProps({
  unitType: {
    type: String as PropType<
      'hybrid_model' | 'physics_based_component' | 'machine_learning_component'
    >,
    required: true,
  },
  unit: {
    type: Object as PropType<
      HybridModel | PhysicsBasedComponent | MachineLearningComponent
    >,
    required: true,
  },
});
</script>

<style scoped lang="scss">
h1 {
  margin-bottom: 0;
}

.unit-type {
  font-size: 1.2em;
  color: $grey-7;
  margin-bottom: 0.7em;
}
</style>
