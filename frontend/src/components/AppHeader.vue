<template>
  <div>
    <q-img
      :src="url"
      spinner-color="white"
      :style="
        $q.screen.lt.sm
          ? 'height: 144px'
          : $q.screen.lt.md
            ? 'height: 136px'
            : 'height: 220px'
      "
    >
      <div
        :class="
          $q.screen.lt.sm ? 'q-mt-sm' : $q.screen.lt.md ? 'q-mt-md' : 'q-mt-xl'
        "
        class="row q-pa-lg full-width"
        style="background: transparent"
      >
        <div class="col-2"></div>
        <div
          class="col-lg-3 col-md-5 col-sm-5 col-xs-6 q-pl-md text-black bg-white"
          style="opacity: 0.6"
        >
          <div
            :class="
              $q.screen.lt.sm
                ? 'text-h4'
                : $q.screen.lt.md
                  ? 'text-h4'
                  : 'text-h2'
            "
            class="text-weight-thin"
          >
            {{ $t('app_title') }}
          </div>
          <div
            :class="
              $q.screen.lt.sm
                ? 'text-subtitle1'
                : $q.screen.lt.md
                  ? 'text-h6'
                  : 'text-h5'
            "
            class="text-black"
          >
            {{ $t('app_subtitle') }}
          </div>
        </div>
        <div class="col"></div>
      </div>
    </q-img>
  </div>
</template>

<script lang="ts">
export default defineComponent({
  name: 'AppHeader',
});
</script>
<script setup lang="ts">
interface AppHeaderProps {
  url: string;
}

defineProps<AppHeaderProps>();
</script>
