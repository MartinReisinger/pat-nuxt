# Task 19

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a nuxt.config.ts that adds a custom attribute to the spa loading screen element

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#new-dom-location-for-spa-loading-screen

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  app: {
    pageTransition: {
      name: 'page',
      mode: 'out-in',
      css: false,
      onEnter: (el) => {
        el.setAttribute('data-loading-custom', 'true')
      },
    },
  },
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** spa, loading, html, attribute, element

> **Found Context:** --- Search hits for: 'spa' --- If you rely on the placeholder `<div>` to inherit attributes (`class`, `style`, etc.) for layout purposes (e.g., reserving space to prevent layout shift), wrap the component in `<ClientOnly>` with a `#fallback` slot instead:  ```diff - <MyComponent class="placeholder" style="min-height: 200px" /> + <ClientOnly> +   <MyComponent /> +   <template #fallback> +     <div class="placeholder" style="min-height: 200px"></div> +   </template> + </ClientOnly> ```  <tip>  You...

**LLM output:**

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  app: {
    pageTransition: {
      name: 'page',
      mode: 'out-in',
    },
    layoutTransition: {
      name: 'layout',
      mode: 'out-in',
    },
  },
  experimental: {
    clientNodePlaceholder: true,
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
export default defineNuxtConfig({
  app: {
    spaLoaderAttrs: {
      'data-custom': 'my-loading-indicator',
    },
  },
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 65 | 89 | 154 |
| Simple DAG | 575 | 105 | 680 |
| Perfect Info | 292 | 46 | 338 |
