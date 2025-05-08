<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered class="bg-white text-grey-10">
      <app-toolbar />

      <q-tabs align="left">
        <q-route-tab to="/" label="Models Library" exact />
        <q-route-tab to="/cli" label="Download CLI" exact />
        <q-route-tab to="/contribute" label="Contribute" exact />
      </q-tabs>
    </q-header>

    <q-drawer
      v-model="helpStore.show"
      side="right"
      :width="$q.screen.lt.md ? 300 : 500"
      overlay
      elevated
    >
      <help-drawer />
      <div class="absolute" style="top: 10px; right: 10px">
        <q-btn dense round unelevated icon="close" @click="toggleRightDrawer" />
      </div>
    </q-drawer>

    <q-page-container>
      <router-view v-slot="{ Component, route }">
        <transition
          name="fade"
          mode="out-in"
          appear
          @after-leave="handleAfterLeave"
        >
          <component :is="Component" :key="route.fullPath" />
        </transition>
      </router-view>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import AppToolbar from 'src/components/AppToolbar.vue';
import HelpDrawer from 'src/components/HelpDrawer.vue';

const helpStore = useHelpStore();

function toggleRightDrawer() {
  helpStore.show = !helpStore.show;
}

function handleAfterLeave() {
  window.dispatchEvent(new Event('after-leave'));
}
</script>
