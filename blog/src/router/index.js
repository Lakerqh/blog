import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/login'
import Home from '@/views/home'

import User from '@/views/user/user'

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            redirect: '/login'
        }, {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/home',
            name: 'Home',
            component: Home,
            children:[
                {
                    path: 'user',
                    name: 'User',
                    component: User,
                }
            ]
        }
    ]
})
