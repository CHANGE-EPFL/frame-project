import { boot } from 'quasar/wrappers';
import { useSettingsStore } from 'src/stores/settings';

export default boot(() => {
  const settingsStore = useSettingsStore();
  settingsStore.initSettings();
});
