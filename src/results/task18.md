# Task 18

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

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
    <pre v-if="error.data">{{ error.data }}</pre>
    <NuxtLink to="/">Home page</NuxtLink>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  error: Object
})
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** error, page, layout, component, component

> **Found Context:** --- Search hits for: 'error' --- 2. Move your `assets/`, `components/`, `composables/`, `app/layouts/`, `app/middleware/`, `app/pages/`, `app/plugins/` and `utils/` folders under it, as well as `app.vue`, `error.vue`, `app.config.ts`. If you have an `app/router-options.ts` or `app/spa-loading-template.html`, these paths remain the same. 3. Make sure your `nuxt.config.ts`, `content/`, `layers/`, `modules/`, `public/`, `shared/` and `server/` folders remain outside the `app/` folder, in the root o...

**LLM output:**

```vue
<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps({
  error: Object as () => NuxtError
})
</script>

<template>
  <div>
    <h1>{{ error.statusCode }}</h1>
    <p>{{ error.message }}</p>
    <pre v-if="error.data">{{ error.data }}</pre>
  </div>
</template>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps({
  error: Object as () => NuxtError
})
</script>

<template>
  <div>
    <h1>{{ error.statusCode }}</h1>
    <h2>{{ error.message }}</h2>
    <pre v-if="error.data">{{ error.data }}</pre>
  </div>
</template>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 63 | 99 | 162 |
| Simple DAG | 15000 | 111 | 15111 |
| Perfect Info | 252 | 99 | 351 |
