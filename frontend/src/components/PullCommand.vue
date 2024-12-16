<template>
  <q-input
    v-model="inputText"
    readonly
    outlined
    rounded
    dense
    class="pull-command q-pa-none"
  >
    <template v-slot:append>
      <q-icon
        name="content_copy"
        @click="copyToClipboard"
        class="cursor-pointer"
      />
    </template>
  </q-input>
</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue';
import { useQuasar } from 'quasar';

const props = defineProps({
  type: {
    type: String,
    required: true,
  },
  short_name: {
    type: String,
    required: true,
  },
});

const inputText = ref(`frame pull ${props.type} ${props.short_name}`);
const $q = useQuasar();

// Method to copy text to the clipboard
const copyToClipboard = () => {
  // Create a temporary text area to help with copying text to clipboard
  const textArea = document.createElement('textarea');
  textArea.value = inputText.value;
  document.body.appendChild(textArea);
  textArea.select();
  document.execCommand('copy');
  document.body.removeChild(textArea);

  $q.notify({
    type: 'positive',
    message: 'Command copied to clipboard',
  });
};
</script>

<style scoped>
.pull-command {
  font-family: monospace;
  font-size: 0.9em;
}

.q-icon {
  margin-left: 8px;
  cursor: pointer;
  font-size: 0.9em;
}
</style>
