<template>
  <div>
    <q-input
      v-model="inputText"
      readonly
      outlined
      rounded
      dense
      class="pull-command q-pa-none"
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
  type: {
    type: String,
    required: true,
  },
  id: {
    type: String,
    required: true,
  },
});

const inputText = ref(`frame pull ${props.type} ${props.id}`);

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
