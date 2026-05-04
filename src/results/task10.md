# Task 10

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a nuxt.config.ts that configures which routes to prerender and which to exclude

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-top-level-generate-configuration

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```ts
export default defineNuxtConfig({
  routeRules: {
    '/admin/**': { ssr: false },
    '/about': { prerender: true },
    '/contact': { prerender: false },
  },
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** prerender, routes, exclude, config, app

> **Found Context:** --- Search hits for: 'prerender' --- ### Shared Prerender Data  🚦 **Impact Level**: Medium  #### What Changed  We enabled a previously experimental feature to share data from `useAsyncData` and `useFetch` calls, across different pages. See [original PR](https://github.com/nuxt/nuxt/pull/24894).  #### Reasons for Change  This feature automatically shares payload *data* between pages that are prerendered. This can result in a significant performance improvement when prerendering sites that use `us...

**LLM output:**

```ts
export default defineNuxtConfig({
  nitro: {
    prerender: {
      routes: ['/about', '/contact'],
      ignore: ['/admin'],
    },
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```typescript
export default defineNuxtConfig({
  nitro: {
    prerender: {
      routes: ['/contact', '/about'],
      ignore: ['/dashboard']
    }
  }
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 68 | 57 | 125 |
| Simple DAG | 13954 | 62 | 14016 |
| Perfect Info | 339 | 51 | 390 |
