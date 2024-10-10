import { createApp } from 'vue'
import ElementPlus from "element-plus"

import './global.css'
import App from './App.vue'

// 创建前端应用 
const app = createApp(App)


/**
 * 1. 使用Element-Plus UI组件库
 */
app.use(ElementPlus)

// 前端应用挂载
app.mount('#app')
