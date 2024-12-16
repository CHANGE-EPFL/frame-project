<template>
  <q-page>
    <div class="container">
      <q-card v-if="machineLearningComponent" flat class="q-mb-xl">
        <UnitFullAbstract
          unitType="machine_learning_component"
          :unit="machineLearningComponent"
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
import type { MachineLearningComponent } from 'src/models/machine_learning_component';
import UnitFullAbstract from 'src/components/UnitFullAbstract.vue';

const route = useRoute();
const componentId = route.params.componentId;
const machineLearningComponent = ref<MachineLearningComponent>();

const getMachineLearningComponent = () => {
  api
    .get(`/components/machine_learning/${componentId}`)
    .then((response) => {
      machineLearningComponent.value = response.data;
    })
    .catch((error) => {
      console.error(`Error fetching component with ID ${componentId}:`, error);
    });
};

onMounted(() => {
  getMachineLearningComponent();
});
</script>
