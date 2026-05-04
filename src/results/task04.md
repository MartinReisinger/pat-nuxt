# Task 4

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a nuxt.config.ts hook that sets a custom layout on the home page

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#scan-page-meta-after-resolution

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```typescript
export default defineNuxtConfig({
  hooks: {
    'pages:extend'(pages) {
      const homePage = pages.find(page => page.name === 'index')
      if (homePage) {
        homePage.meta.layout = 'custom'
      }
    }
  }
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** hooks, layout, page, home, route

> **Found Context:** --- Search hits for: 'hooks' --- 2. **Changed plugin registration**: Vite plugins registered with `addVitePlugin()` and only targeting one environment (by passing `server: false` or `client: false`) will not have their `config` or `configResolved` hooks called. 3. **Shared configuration**: The `vite:extendConfig` and `vite:configResolved` hooks now work with a shared configuration rather than separate client/server configs.  #### Reasons for Change  The Vite Environment API provides:  - Better c...

**LLM output:**

```typescript
export default defineNuxtConfig({
  hooks: {
    'pages:extend': (pages) => {
      const page = pages.find(p => p.name === 'index')
      if (page) {
        page.layouts.default = 'custom'
      }
    }
  }
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
export default defineNuxtConfig({
  hooks: {
    'pages:resolved'(pages) {
      const homePage = pages.find(page => page.path === '/')
      homePage.meta ||= {}
      homePage.meta.layout = 'custom-layout'
    }
  }
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 66 | 77 | 143 |
| Simple DAG | 524 | 85 | 609 |
| Perfect Info | 343 | 74 | 417 |
