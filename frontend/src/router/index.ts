import { route } from 'quasar/wrappers';
import {
  createMemoryHistory,
  createRouter,
  createWebHashHistory,
  createWebHistory,
} from 'vue-router';

import routes from './routes';

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default route(function (/* { store, ssrContext } */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : process.env.VUE_ROUTER_MODE === 'history'
      ? createWebHistory
      : createWebHashHistory;

  const Router = createRouter({
    scrollBehavior: (to, from, savedPosition) => {
      // Scroll between page transitions
      return new Promise((resolve) => {
        const scrollTriggerEvent = 'after-leave'; // Custom event name

        const scrollHandler = () => {
          window.removeEventListener(scrollTriggerEvent, scrollHandler);

          setTimeout(() => {
            resolve(savedPosition || { top: 0 });
          }, 50); // Small delay to ensure we're between transitions
        };

        window.addEventListener(scrollTriggerEvent, scrollHandler);

        // Fallback in case the event never fires
        setTimeout(() => {
          window.removeEventListener(scrollTriggerEvent, scrollHandler);
          resolve(savedPosition || { top: 0 });
        }, 350);
      });
    },
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(process.env.VUE_ROUTER_BASE),
  });

  return Router;
});
