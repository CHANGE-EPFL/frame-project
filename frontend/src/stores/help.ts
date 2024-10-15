import { defineStore } from 'pinia';

export const useHelpStore = defineStore('help', () => {
  const show = ref(false);
  const content = ref('');
  const current = ref('');

  async function toggleHelp(name: string) {
    if (current.value === name) {
      show.value = !show.value;
    } else {
      current.value = name;
      const response = await fetch(`${name}.md`);
      content.value = await response.text();
      show.value = true;
    }
  }

  return {
    show,
    content,
    toggleHelp,
  };
});
