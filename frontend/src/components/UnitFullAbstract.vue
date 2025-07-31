<template>
  <div>
    <h1>{{ unit.name }}</h1>
    <div class="unit-type">
      {{
        {
          hybrid_model: 'Hybrid Model',
          physics_based_component: 'Physics-Based Component',
          machine_learning_component: 'Machine Learning Component',
        }[unitType]
      }}
      <a
        class="unit-fair-level q-ml-xs"
        href="https://www.nature.com/articles/s41597-022-01710-x"
        target="_blank"
        v-if="unit.fair_level !== undefined"
      >
        <q-icon
          v-for="i in unit.fair_level"
          :key="i"
          name="star"
          :color="
            unitType === 'hybrid_model'
              ? 'primary'
              : unitType === 'physics_based_component'
                ? 'secondary'
                : 'accent'
          "
        />
        <q-icon
          v-for="i in MAX_FAIR_LEVEL - unit.fair_level"
          :key="i"
          name="star"
          color="grey-4"
        />
        <q-tooltip>
          Indication of the FAIR level of this unit ({{ unit.fair_level }}/{{
            MAX_FAIR_LEVEL
          }}). Click for more information (external link).
        </q-tooltip>
      </a>
    </div>
    <div v-if="unit.contributors" class="unit-contributors">
      {{ unit.contributors.join(', ') }}
    </div>
    <div
      class="unit-description q-mt-md"
      v-html="unit.description.replace(/(?:\r\n|\r|\n)/g, '<br>')"
    ></div>
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
    <div class="row items-center">
      <CopyCommand
        :command="`frame pull ${unitType === 'hybrid_model' ? 'model' : 'component'} ${unit.id}${unit.latest ? '' : `:${unit.version}`} ${unitType === 'hybrid_model' ? '' : '<LOCAL_MODEL_PATH>'}`"
        class="q-mt-lg q-mb-lg col"
      />
      <router-link to="/cli" class="q-ml-sm">
        <q-icon name="info" size="1.5em" color="grey-9">
          <q-tooltip>
            Run this command after installing the FRAME CLI tool. Click for
            instructions.
          </q-tooltip>
        </q-icon>
      </router-link>
    </div>
    <div class="q-mt-md">
      <VersionSelector
        :unitType="unitType"
        :unitId="unit.id"
        :unitVersion="unit.version"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import type { HybridModel } from 'src/models/hybrid_model';
import type { PhysicsBasedComponent } from 'src/models/physics_based_component';
import type { MachineLearningComponent } from 'src/models/machine_learning_component';
import KeywordList from 'src/components/KeywordList.vue';
import CopyCommand from 'src/components/CopyCommand.vue';
import VersionSelector from 'src/components/VersionSelector.vue';

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

const MAX_FAIR_LEVEL = 4; // Match to FAIR_LEVEL_PROPERTIES size in backend/api/services/metadata.py
</script>

<style scoped lang="scss">
h1 {
  margin-bottom: 0;
}

.unit-type {
  font-size: 1.2em;
  color: $grey-7;
}

.unit-fair-level {
  font-size: 1.1em;
  line-height: 1.2em;
  display: inline-block;
  transform: translateY(-0.08em);
}

.unit-contributors {
  margin-top: 0.7em;
}
</style>
