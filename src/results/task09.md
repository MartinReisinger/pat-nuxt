# Task 9

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a vue component that sets a page title and meta description

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#unhead-v2

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <Head>
    <Title>{{ title }}</Title>
    <Meta name="description" :content="description" />
  </Head>
  <slot />
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  }
});
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** vue, component, page, title, meta

> **Found Context:** --- Search hits for: 'vue' --- With `compatibilityVersion: 5`, client-only components (`.client.vue` files and `createClientOnly()` wrappers) now render an HTML comment (`<!--placeholder-->`) on the server instead of an empty `<div>` element.  #### Reasons for Change  When the placeholder `<div>` and the actual component root share the same tag name, Vue's runtime skips re-applying `setScopeId` during hydration. This causes scoped styles to be missing after the component mounts. Using a comment ...

**LLM output:**

```vue
<script setup lang="ts">
useHead({
  title: 'My Page Title',
  meta: [
    { name: 'description', content: 'My page description' }
  ]
})
</script>

<template>
  <div>
    <h1>Welcome!</h1>
  </div>
</template>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template></template>

<script setup lang="ts">
import { useHead } from '#imports'

useHead({
  title: 'My Awesome Page',
  meta: [
    { name: 'description', content: 'This is a great page about something interesting.' }
  ]
})
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 58 | 107 | 165 |
| Simple DAG | 534 | 84 | 618 |
| Perfect Info | 296 | 76 | 372 |
