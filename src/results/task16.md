# Task 16

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a nuxt.config.ts that inlines all css including global stylesheets into the html response

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#more-granular-inline-styles

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```typescript
export default {
  css: ['~/assets/css/global.css'],
  experimental: {
    inlineCSS: true,
  },
}
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** inline, css, global, stylesheets, html

> **Found Context:** --- Search hits for: 'inline' --- ### More Granular Inline Styles  🚦 **Impact Level**: Moderate  Nuxt will now only inline styles for Vue components, not global CSS.  #### What Changed  Previously, Nuxt would inline all CSS, including global styles, and remove `<link>` elements to separate CSS files. Now, Nuxt will only do this for Vue components (which previously produced separate chunks of CSS). We think this is a better balance of reducing separate network requests (just as before, there will...

**LLM output:**

```ts
export default defineNuxtConfig({
  features: {
    inlineStyles: true,
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
export default defineNuxtConfig({
  features: {
    inlineStyles: true,
  },
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 68 | 39 | 107 |
| Simple DAG | 15071 | 38 | 15109 |
| Perfect Info | 250 | 29 | 279 |
