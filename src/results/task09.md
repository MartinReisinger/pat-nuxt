# Task 9

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a vue component that sets a page title and meta description

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#unhead-v2

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template><meta name="description" :content="description"></template>

<script setup>
const pageTitle = 'My Awesome Page'
const description = 'This is a description of my awesome page.'

useHead({
  title: pageTitle
})
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** page, title, meta, description, seo

> **Found Context:** --- Search hits for: 'page' --- - **Normalized Page Names**: Page component names will [match their route names](/dag_content/4.x/getting-started/upgrade#normalized-page-component-names) for consistent `<KeepAlive>` behavior - **clearNuxtState resets to defaults**: `clearNuxtState` will [reset state to its initial value](/dag_content/4.x/getting-started/upgrade#respect-defaults-when-clearing-usestate) instead of setting it to `undefined` - **Non-async callHook**: [`callHook` may return `void`](/...

**LLM output:**

```vue
<script setup lang="ts">
useHead({
  title: 'My Page Title',
  meta: [
    { name: 'description', content: 'This is the meta description for my page.' }
  ]
})
</script>

<template>
  <div>
    <h1>Welcome to my page!</h1>
  </div>
</template>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    Page Content
  </div>
</template>

<script setup>
useHead({
  title: 'My Awesome Page',
  meta: [
    { name: 'description', content: 'This is a great page' }
  ]
})
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 60 | 65 | 125 |
| Simple DAG | 15814 | 92 | 15906 |
| Perfect Info | 298 | 72 | 370 |
