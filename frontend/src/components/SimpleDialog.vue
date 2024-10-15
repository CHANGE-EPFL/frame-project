<template>
  <q-dialog :maximized="$q.screen.lt.sm" v-model="showDialog" @hide="onHide">
    <q-card :style="$q.screen.lt.sm ? '' : `width: ${width ? width : '500px'}; max-width: 80vw; max-height: 90vh`">
      <q-card-actions>
        <div v-if="title" class="text-h6 q-pl-sm">
          {{ title }}
        </div>
        <q-space />
        <q-btn flat icon="close" color="primary" v-close-popup class="float-right" />
        </q-card-actions>
      <q-card-section class="q-pt-none">
        <div v-if="props.content">
          <q-markdown :src="props.content" />
        </div>
        <slot></slot>
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script lang="ts">
export default defineComponent({
  name: 'SimpleDialog',
});
</script>
<script setup lang="ts">
interface Props {
  modelValue: boolean;
  title?: string;
  content?: string;
  width?: string;
}
const props = defineProps<Props>();
const emit = defineEmits(['update:modelValue']);

const showDialog = ref(props.modelValue);

watch(
  () => props.modelValue,
  (value) => {
    showDialog.value = value;
  },
);

function onHide() {
  emit('update:modelValue', false);
}
</script>
