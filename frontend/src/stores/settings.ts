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
    // cookies.get() declares to return a string but apparently it automatically parses the JSON string to an object
    if (settingsSaved !== null) {
      if (typeof settingsSaved === 'string') {
        settingsData = JSON.parse(settingsSaved);
      } else if (typeof settingsSaved === 'object') {
        settingsData = settingsSaved as Settings;
      }
    }
    settings.value = settingsData;
    return settings.value;
  }

  function saveSettings(settingsData: Settings) {
    settings.value = { ...settings.value, ...settingsData };
    LocalStorage.set(APP_STORAGE_NAME, JSON.stringify(settings.value));
  }

  return {
    settings,
    initSettings,
    saveSettings,
  };
});
