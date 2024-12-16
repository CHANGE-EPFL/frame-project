<template>
  <q-page>
    <div class="container">
      <q-card v-if="physicsBasedComponent" flat class="q-mb-xl">
        <UnitFullAbstract
          unitType="physics_based_component"
          :unit="physicsBasedComponent"
        />
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

const route = useRoute();
const componentId = route.params.componentId;
const physicsBasedComponent = ref<PhysicsBasedComponent>();

const getPhysicsBasedComponent = () => {
  api
    .get(`/components/physics_based/${componentId}`)
    .then((response) => {
      physicsBasedComponent.value = response.data;
    })
    .catch((error) => {
      console.error(`Error fetching component with ID ${componentId}:`, error);
    });
};

onMounted(() => {
  getPhysicsBasedComponent();
});
</script>
