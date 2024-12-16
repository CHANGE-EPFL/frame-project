<template>
  <q-table
    :rows="filteredData"
    :columns="columns"
    row-key="field"
    class="q-mt-md"
    flat
    bordered
    hide-header
    hide-pagination
    :rows-per-page-options="[0]"
    dense
    wrap-cells
  >
    <template v-slot:body-cell-value="props">
      <q-td :props="props">
        <div v-if="Array.isArray(props.row.value)">
          <div v-for="(item, index) in props.row.value" :key="index">
            <span v-if="isUrl(item)">
              <a :href="item" target="_blank">{{ item }}</a>
            </span>
            <span v-else>
              {{ item }}
            </span>
          </div>
        </div>
        <span v-else-if="isUrl(props.row.value)">
          <a :href="props.row.value" target="_blank">{{ props.row.value }}</a>
        </span>
        <span v-else>
          {{ props.row.value }}
        </span>
      </q-td>
    </template>
  </q-table>
</template>

<script setup lang="ts">
import { PropType } from 'vue';

const columns = [
  {
    name: 'property',
    align: 'left',
    field: 'property',
    classes: 'metadata-table-property',
  },
  {
    name: 'value',
    align: 'left',
    field: 'value',
    classes: 'metadata-table-value',
  },
];

const props = defineProps({
  data: {
    type: Array as PropType<
      Array<{ property: string; value: string | string[] }>
    >,
    required: true,
  },
});

function isUrl(value: string): boolean {
  const urlRegex =
    /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/;
  return typeof value === 'string' && urlRegex.test(value);
}

const filteredData = computed(() => {
  return props.data.filter((row) => {
    if (row.value === null || row.value === '') return false;
    if (Array.isArray(row.value) && row.value.length === 0) return false;
    return true;
  });
});
</script>
