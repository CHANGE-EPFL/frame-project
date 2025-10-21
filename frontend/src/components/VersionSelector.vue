<template>
  <q-select
    outlined
    dense
    :color="
      props.unitType === 'hybrid_model'
        ? 'primary'
        : props.unitType === 'physics_based_component'
          ? 'secondary'
          : 'accent'
    "
    v-model="selectedVersion"
    :options="versions"
    label="Version"
    class="q-mt-md"
    v-if="
      versions.length > 0 && !(versions.length === 1 && versions[0] === 'none')
    "
    @update:model-value="redirectToVersion"
  >
    <!-- In v-if, match 'none' to DEFAULT_VERSION in backend/api/services/metadata.py -->
  </q-select>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import { ref, onMounted } from 'vue';
import { api } from 'src/boot/api';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
  unitType: {
    type: String as PropType<
      'hybrid_model' | 'physics_based_component' | 'machine_learning_component'
    >,
    required: true,
  },
  unitId: {
    type: String,
    required: true,
  },
  unitVersion: {
    type: String as PropType<string | null | undefined>,
    required: true,
  },
});

const versions = ref<string[]>([]);
const selectedVersion = ref<string | null>(props.unitVersion);

const redirectToVersion = (version: string) => {
  if (version) {
    router.push({ path: `/${props.unitType}/${props.unitId}/${version}` });
  }
};

const getUnitVersions = () => {
  const endpoint =
    props.unitType === 'hybrid_model'
      ? `hybrid_models/versions/${props.unitId}`
      : props.unitType === 'physics_based_component'
        ? `components/physics_based_versions/${props.unitId}`
        : `components/machine_learning_versions/${props.unitId}`;

  return api
    .get(endpoint)
    .then((response) => {
      versions.value = response.data;
    })
    .catch((error) => {
      console.error(
        `Error fetching ${props.unitType} with ID ${props.unitId}:`,
        error,
      );
    });
};

onMounted(() => {
  getUnitVersions();
});
</script>
