import {createRouter, createWebHistory} from "vue-router";
import HomeView from "@/views/HomeView.vue";
import MyPage from "@/views/MyPage.vue";
import RegisterView from "@/views/RegisterView.vue";

const routes = [
    {
        path: '/',
        name: "Home",
        component: HomeView,
    },
    {
        path: '/mypage',
        name: 'myPage',
        component: MyPage
    },
    {
        path: '/register',
        name: 'register',
        component: RegisterView
    }
]

const router = createRouter({
    history: createWebHistory("/"),
    routes,
})

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // if (store.getters.isAuthenticated) {
    //   next();
    //   return;
    // }
    next('/login');
  } else {
    next();
  }
});

export default router;