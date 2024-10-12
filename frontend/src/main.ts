import { createApp } from 'vue'
import ElementPlus from "element-plus"
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

import './global.css'
import App from './App.vue'

// 创建前端应用 
const app = createApp(App)

/**
 * 1. 使用Element-Plus UI组件库
 * 2. 注册所有图标
 */
app.use(ElementPlus)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

// 前端应用挂载
app.mount('#app')
