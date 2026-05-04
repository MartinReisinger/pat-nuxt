# Task 3

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** set up KeepAlive on NuxtPage so a component inside a subfolder stays mounted between navigations

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#normalized-component-names

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <NuxtLayout>
    <NuxtPage keep-alive />
  </NuxtLayout>
</template>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** KeepAlive, page, cache, component, persist

> **Found Context:** --- Search hits for: 'KeepAlive' --- - **Normalized Page Names**: Page component names will [match their route names](/dag_content/4.x/getting-started/upgrade#normalized-page-component-names) for consistent `<KeepAlive>` behavior - **clearNuxtState resets to defaults**: `clearNuxtState` will [reset state to its initial value](/dag_content/4.x/getting-started/upgrade#respect-defaults-when-clearing-usestate) instead of setting it to `undefined` - **Non-async callHook**: [`callHook` may return `voi...

**LLM output:**

```vue
<template>
  <NuxtLayout>
    <NuxtPage :keepalive="{ max: 5 }" />
  </NuxtLayout>
</template>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <NuxtPage :keepalive="{ include: ['MySubfolderMyComponent'] }" />
</template>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 66 | 36 | 102 |
| Simple DAG | 553 | 52 | 605 |
| Perfect Info | 407 | 33 | 440 |
