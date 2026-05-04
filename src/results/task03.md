# Task 3

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** set up KeepAlive on NuxtPage so a user id component inside a subfolder stays mounted between navigations

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#normalized-component-names

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <NuxtPage :keep-alive="{ max: 5 }" />
</template>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** KeepAlive, page, cache, persistence, component

> **Found Context:** --- Search hits for: 'KeepAlive' --- - **Normalized Page Names**: Page component names will [match their route names](/dag_content/4.x/getting-started/upgrade#normalized-page-component-names) for consistent `<KeepAlive>` behavior - **clearNuxtState resets to defaults**: `clearNuxtState` will [reset state to its initial value](/dag_content/4.x/getting-started/upgrade#respect-defaults-when-clearing-usestate) instead of setting it to `undefined` - **Non-async callHook**: [`callHook` may return `voi...

**LLM output:**

```vue
<template>
  <NuxtPage :keepalive="{ include: ['users-id'] }" />
</template>
```

