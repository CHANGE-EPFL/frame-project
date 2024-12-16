<template>
  <q-page>
    <div class="container">
      <q-card v-if="physicsBasedComponent" flat class="q-mb-xl">
        <UnitFullAbstract
          unitType="physics_based_component"
          :unit="physicsBasedComponent"
        />
        <MetadataTable :data="otherMetadata" />
      </q-card>
      <q-card v-else flat>
        <p><q-spinner /> Loading component data...</p>
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
import MetadataTable from 'src/components/MetadataTable.vue';

const route = useRoute();
const componentId = route.params.componentId;
const physicsBasedComponent = ref<PhysicsBasedComponent>();
const otherMetadata = ref<{ property: string; value: any }[]>([]);

const getPhysicsBasedComponent = () => {
  api
    .get(`/components/physics_based/${componentId}`)
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
        {
          property: 'Testing resources',
          value: physicsBasedComponent.value?.testing_resources,
        },
      ];
    })
    .catch((error) => {
      console.error(`Error fetching component with ID ${componentId}:`, error);
    });
};

onMounted(() => {
  getPhysicsBasedComponent();
});
</script>
