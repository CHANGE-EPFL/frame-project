<template>
  <q-toolbar>
    <a href="https://epfl.ch" target="_blank" class="q-mt-sm">
      <img src="/EPFL_logo.png" style="height: 25px" />
    </a>
    <span class="q-ml-md text-h6">{{ $t('app_title') }}</span>
    <q-space />
    <span v-if="!$q.screen.lt.md">
      <q-btn
        flat
        round
        icon="menu_book"
        :title="$t('resources')"
        @click="showResources = true"
      ></q-btn>
      <q-btn
        flat
        round
        icon="info"
        :title="$t('introduction')"
        @click="showIntro = true"
        class="on-left"
      ></q-btn>
    </span>
    <q-btn v-if="$q.screen.lt.md" flat round icon="more_vert">
      <q-popup-proxy>
        <q-list class="bg-white">
          <q-item clickable v-close-popup @click="showResources = true">
            <q-item-section>
              <q-item-label>{{ $t('resources') }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item clickable v-close-popup @click="showIntro = true">
            <q-item-section>
              <q-item-label>{{ $t('introduction') }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-popup-proxy>
    </q-btn>
    <a href="https://www.epfl.ch/labs/change/" target="_blank" class="q-mt-xs">
      <span class="text-logo q-mb-xs">CHANGE</span>
    </a>
  </q-toolbar>

  <simple-dialog
    v-model="showIntro"
    :title="$t('app_title')"
    :content="IntroductionMd"
  />

  <simple-dialog v-model="showResources" :title="$t('resources')">
    <q-list separator>
      <essential-link
        v-for="link in essentialLinks"
        :key="link.title"
        v-bind="link"
      />
    </q-list>
  </simple-dialog>
</template>

<script lang="ts">
export default defineComponent({
  components: { SimpleDialog },
  name: 'AppToolbar',
});
</script>
<script setup lang="ts">
import IntroductionMd from 'src/assets/introduction.md';
import essentialLinks from 'src/assets/links.json';
import EssentialLink from 'src/components/EssentialLink.vue';
import SimpleDialog from 'src/components/SimpleDialog.vue';
import { Settings } from 'src/stores/settings';

interface Props {
  noMenu?: boolean;
}

withDefaults(defineProps<Props>(), {
  noMenu: false,
});
const settingsStore = useSettingsStore();

const showIntro = ref(false);
const showResources = ref(false);

onMounted(() => {
  if (!settingsStore.settings?.intro_shown) {
    showIntro.value = true;
    settingsStore.saveSettings({ intro_shown: true } as Settings);
  }
});
</script>
