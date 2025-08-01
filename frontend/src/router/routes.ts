import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('src/pages/HomePage.vue') },
      {
        path: '/hybrid_model/:modelId/:modelVersion?',
        component: () => import('pages/HybridModelPage.vue'),
      },
      {
        path: '/physics_based_component/:componentId/:componentVersion?',
        component: () => import('pages/PhysicsBasedComponentPage.vue'),
      },
      {
        path: '/machine_learning_component/:componentId/:componentVersion?',
        component: () => import('pages/MachineLearningComponentPage.vue'),
      },
      { path: '/cli', component: () => import('src/pages/CliPage.vue') },
      {
        path: '/protocol',
        component: () => import('src/pages/ProtocolPage.vue'),
      },
      {
        path: '/contribute',
        component: () => import('src/pages/ContributePage.vue'),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
