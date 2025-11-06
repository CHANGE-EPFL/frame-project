<template>
  <q-page>
    <div class="container">
      <q-card v-if="physicsBasedComponent" flat class="q-mb-lg">
        <UnitFullAbstract
          unitType="physics_based_component"
          :unit="physicsBasedComponent"
          class="q-mb-md"
        />

        <div v-if="hybridModels.length > 0">
          <p>This component is used by the following models:</p>
          <template v-for="(unit, index) in hybridModels" :key="index">
            <UnitLink unitType="hybrid_model" :unit="unit" />
            <br />
          </template>
        </div>

        <MetadataTable :data="otherMetadata" class="q-mb-lg" />

        <q-expansion-item
          v-if="physicsBasedComponent.testing_resources"
          icon="computer"
          label="Testing resources"
        >
          <ComputationalResources
            :data="physicsBasedComponent.testing_resources"
          />
          <div class="q-mb-lg" />
        </q-expansion-item>
      </q-card>

      <q-card v-else flat class="q-mt-md">
        <p><q-spinner /> Loading component data...</p>
      </q-card>

      <q-card
        v-if="physicsBasedComponent && physicsBasedComponent.readme_content"
        flat
      >
        <q-separator />
        <h2 class="q-mt-lg q-mb-sm">
          <q-icon name="description" class="q-mr-sm" />README.md
        </h2>
        <a
          :href="physicsBasedComponent.readme as string"
          target="_blank"
          rel="noopener"
          class="readme-link"
          >{{ physicsBasedComponent.readme }}</a
        >
        <q-markdown
          :src="physicsBasedComponent.readme_content"
          class="q-mt-md q-mb-xl"
          no-heading-anchor-links
        />
      </q-card>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from 'src/boot/api';
import type { PhysicsBasedComponent } from 'src/models/physics_based_component';
import UnitFullAbstract from 'src/components/UnitFullAbstract.vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';
import UnitLink from 'src/components/UnitLink.vue';
import MetadataTable from 'src/components/MetadataTable.vue';
import ComputationalResources from 'src/components/ComputationalResources.vue';

const route = useRoute();
const componentId = route.params.componentId;
const componentVersion = route.params.componentVersion;
const physicsBasedComponent = ref<PhysicsBasedComponent>();
const hybridModels = ref<HybridModelSummary[]>([]);
const otherMetadata = ref<{ property: string; value: any }[]>([]);

const getPhysicsBasedComponent = () => {
  api
    .get(`/components/physics_based/${componentId}`, {
      params: {
        component_version: componentVersion || undefined,
      },
    })
    .then((response) => {
      physicsBasedComponent.value = response.data;
      otherMetadata.value = [
        {
          property: 'Documentation',
          value: physicsBasedComponent.value?.documentation,
        },
        {
          property: 'Identifier',
          value: physicsBasedComponent.value?.identifier,
        },
        { property: 'URL', value: physicsBasedComponent.value?.url },
        { property: 'Version', value: physicsBasedComponent.value?.version },
        { property: 'Type', value: physicsBasedComponent.value?.type },
        {
          property: 'Fixed parameters count',
          value: physicsBasedComponent.value?.fixed_parameters_count,
        },
        {
          property: 'Tunable parameters count',
          value: physicsBasedComponent.value?.tunable_parameters_count,
        },
        {
          property: 'State variables count',
          value: physicsBasedComponent.value?.state_variables_count,
        },
        {
          property: 'Temporal coverage',
          value: physicsBasedComponent.value?.temporal_coverage,
        },
        {
          property: 'Spatial coverage',
          value: physicsBasedComponent.value?.spatial_coverage,
        },
        {
          property: 'Spatial resolution',
          value: physicsBasedComponent.value?.spatial_resolution,
        },
        {
          property: 'Temporal resolution',
          value: physicsBasedComponent.value?.temporal_resolution,
        },
        {
          property: 'Vertical discretization (soil)',
          value: physicsBasedComponent.value?.vertical_discretization?.soil,
        },
        {
          property: 'Vertical discretization (vegetation)',
          value:
            physicsBasedComponent.value?.vertical_discretization?.vegetation,
        },
        {
          property: 'Lateral flow',
          value: physicsBasedComponent.value?.lateral_flow,
        },
        {
          property: 'Related identifiers',
          value: physicsBasedComponent.value?.related_identifiers,
        },
      ];
    })
    .catch((error) => {
      console.error(`Error fetching component with ID ${componentId}:`, error);
    });
};

const getHybridModels = () => {
  api
    .get(`/hybrid_models/physics_based/${componentId}`)
    .then((response) => {
      hybridModels.value = response.data;
    })
    .catch((error) => {
      console.error(
        `Error fetching hybrid models for component with ID ${componentId}:`,
        error,
      );
    });
};

onMounted(() => {
  getPhysicsBasedComponent();
  getHybridModels();
});
</script>
