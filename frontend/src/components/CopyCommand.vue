<template>
  <div class="copy-command-container">
    <q-input
      v-model="inputText"
      readonly
      standout
      rounded
      dense
      bg-color="grey-9"
      dark
      class="command q-pa-none"
    >
      <template v-slot:append>
        <q-icon name="content_copy" @click="copy" class="cursor-pointer" />
      </template>
    </q-input>
  </div>
</template>

<script setup lang="ts">
import { defineProps, ref } from 'vue';
import { copyToClipboard, Notify } from 'quasar';

const props = defineProps({
  command: {
    type: String,
    required: true,
  },
});

const inputText = ref(props.command);

function copy() {
  copyToClipboard(inputText.value)
    .then(() => {
      Notify.create({
        message: 'Copied to clipboard',
        color: 'positive',
      });
    })
    .catch(() => {
      Notify.create({
        message: 'Failed to copy to clipboard',
        color: 'negative',
      });
    });
}
</script>

<style scoped lang="scss">
.copy-command-container {
  margin: 1em 0;
}

.command {
  font-family: monospace;
  font-size: 0.9em;
}

.q-icon {
  margin-left: 8px;
  cursor: pointer;
  font-size: 0.9em;
}
</style>
