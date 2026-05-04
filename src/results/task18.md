# Task 18

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a custom error.vue that displays extra details attached to the thrown error

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#parsed-errordata

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <div>
    <h1>{{ error.statusCode }}</h1>
    <p>{{ error.message }}</p>
    <pre v-if="error.data">{{ JSON.stringify(error.data, null, 2) }}</pre>
  </div>
</template>

<script setup>
const props = defineProps({
  error: Object
})
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** error, page, layout, custom, component

> **Found Context:** --- Search hits for: 'error' --- 2. Move your `assets/`, `components/`, `composables/`, `app/layouts/`, `app/middleware/`, `app/pages/`, `app/plugins/` and `utils/` folders under it, as well as `app.vue`, `error.vue`, `app.config.ts`. If you have an `app/router-options.ts` or `app/spa-loading-template.html`, these paths remain the same. 3. Make sure your `nuxt.config.ts`, `content/`, `layers/`, `modules/`, `public/`, `shared/` and `server/` folders remain outside the `app/` folder, in the root o...

**LLM output:**

```vue
<template>
  <div>
    <h1>{{ error.statusCode }}</h1>
    <p>{{ error.message }}</p>
    <pre v-if="error.data">{{ error.data }}</pre>
    <button @click="handleError">Clear errors</button>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  error: Object
})

const handleError = () => clearError({ redirect: '/' })
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    <h1>{{ error.statusCode }}</h1>
    <h2>{{ error.message }}</h2>
    <pre v-if="error.data">{{ error.data }}</pre>
  </div>
</template>

<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps({
  error: Object as () => NuxtError
})
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 61 | 91 | 152 |
| Simple DAG | 568 | 121 | 689 |
| Perfect Info | 250 | 99 | 349 |
