# Task 16

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a nuxt.config.ts that inlines all css including global stylesheets into the html response

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#more-granular-inline-styles

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```ts
export default defineNuxtConfig({
  css: [
    '~/assets/css/global.css'
  ],
  experimental: {
    inlineSSRStyles: true,
  },
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** build, vite, css, inline, html

> **Found Context:** --- Search hits for: 'build' --- To use the latest Nuxt build and test features before their release, read about the [nightly release channel](/dag_content/4.x/guide/going-further/nightly-release-channel) guide.  ## Testing Nuxt 5  Nuxt 5 is **currently in development**. Until the release, it is possible to test many of Nuxt 5's breaking changes from Nuxt version 4.2+.  ### Opting in to Nuxt 5  First, upgrade Nuxt to the [latest release](https://github.com/nuxt/nuxt/releases).  Then you can set ...

**LLM output:**

```ts
export default defineNuxtConfig({
  css: {
    inline: true,
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
| Baseline | 66 | 50 | 116 |
| Simple DAG | 566 | 37 | 603 |
| Perfect Info | 248 | 29 | 277 |
