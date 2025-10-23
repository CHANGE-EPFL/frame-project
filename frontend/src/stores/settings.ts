import { defineStore } from 'pinia';
import { LocalStorage } from 'quasar';

const APP_STORAGE_NAME = 'frame_settings';

export type Settings = {
  intro_shown: boolean;
  show_globe: boolean;
};

export const useSettingsStore = defineStore('settings', () => {
  const settings = ref<Settings>();

  function initSettings(): Settings {
    if (settings.value != undefined) return settings.value;
    let settingsData: Settings = {
      intro_shown: false,
      show_globe: false,
    };
    const settingsSaved = LocalStorage.getItem(APP_STORAGE_NAME);
    if (settingsSaved !== null && typeof settingsSaved === 'object') {
      settingsData = settingsSaved as Settings;
    }
    settings.value = settingsData;
    return settings.value;
  }

  function saveSettings(settingsData: Settings) {
    settings.value = { ...settings.value, ...settingsData };
    LocalStorage.set(APP_STORAGE_NAME, settings.value);
  }

  return {
    settings,
    initSettings,
    saveSettings,
  };
});
