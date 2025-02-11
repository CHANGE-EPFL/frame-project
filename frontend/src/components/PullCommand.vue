<template>
  <div class="row items-center">
    <q-input
      v-model="inputText"
      readonly
      outlined
      rounded
      dense
      class="pull-command q-pa-none col"
    >
      <template v-slot:append>
        <q-icon name="content_copy" @click="copy" class="cursor-pointer" />
      </template>
    </q-input>
    <router-link to="/cli">
      <q-icon name="info" size="1.5em" color="grey-7">
        <q-tooltip>
          Run this command after installing the FRAME CLI tool. Click for
          instructions.
        </q-tooltip>
      </q-icon>
    </router-link>
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

const inputText = ref(`frame-cli pull ${props.type} ${props.id}`);

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
