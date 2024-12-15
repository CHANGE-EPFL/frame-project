<template>
  <div class="container">
    <q-list>
      <template v-for="(model, index) in models" :key="model.id">
        <q-item>
          <q-item-section>
            <q-item-label class="model-name">{{ model.name }}</q-item-label>
            <q-item-label caption>{{ model.description }}</q-item-label>
            <div class="q-mt-sm">
              <q-chip
                v-for="keyword in model.keywords"
                :key="keyword"
                class="q-mr-sm keyword-chip"
                color="primary"
                text-color="white"
                >
                {{ keyword }}
              </q-chip>
            </div>
          </q-item-section>
        </q-item>
        <!-- Place separator between items -->
        <q-separator
          v-if="index < models.length - 1"
          spaced
          color="light-grey"
          />
      </template>
    </q-list>
  </div>
</template>

<script setup lang="ts">
  import { api } from 'src/boot/api';
import { ref, onMounted } from 'vue';
import type { HybridModelSummary } from 'src/models/hybrid_model';

const models = ref<HybridModelSummary[]>([]);

const getHybridModels = () => {
  api.get('/hybrid_models')
    .then(response => {
      models.value = response.data;
    })
    .catch(error => {
      console.error('Error getting hybrid models metadata:', error);
    });
};

onMounted(() => {
  getHybridModels();
});
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: 0 auto;
  padding: 16px;
}

.model-name {
  font-size: 1.25rem;
  font-weight: bold;
}

.keyword-chip {
  font-size: 0.75rem;
}
</style>
