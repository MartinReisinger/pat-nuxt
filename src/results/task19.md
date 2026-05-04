# Task 19

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a nuxt.config.ts that adds a custom attribute to the spa loading screen element

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#new-dom-location-for-spa-loading-screen

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```typescript
export default defineNuxtConfig({
  app: {
    head: {
      htmlAttrs: {
        'data-spa-loading': 'true'
      }
    }
  }
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** spa, loading, attribute, custom, element

> **Found Context:** --- Search hits for: 'spa' --- If you rely on the placeholder `<div>` to inherit attributes (`class`, `style`, etc.) for layout purposes (e.g., reserving space to prevent layout shift), wrap the component in `<ClientOnly>` with a `#fallback` slot instead:  ```diff - <MyComponent class="placeholder" style="min-height: 200px" /> + <ClientOnly> +   <MyComponent /> +   <template #fallback> +     <div class="placeholder" style="min-height: 200px"></div> +   </template> + </ClientOnly> ```  <tip>  You...

**LLM output:**

```ts
export default defineNuxtConfig({
  spaLoadingTemplate: {
    customAttributes: 'data-spa-loading',
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
export default defineNuxtConfig({
  app: {
    spaLoaderAttrs: {
      'data-custom': 'my-loading-screen'
    }
  }
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 67 | 51 | 118 |
| Simple DAG | 16485 | 45 | 16530 |
| Perfect Info | 294 | 46 | 340 |
