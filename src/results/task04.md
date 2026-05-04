# Task 4

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a nuxt.config.ts hook that sets a custom layout on the home page

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#scan-page-meta-after-resolution

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```typescript
// nuxt.config.ts
export default defineNuxtConfig({
  hooks: {
    'pages:extend': (pages) => {
      const homePage = pages.find(page => page.name === 'index')
      if (homePage) {
        homePage.layouts.custom = 'homeLayout'
      }
    }
  }
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** Nuxt, config, hooks, layout, page

> **Found Context:** --- Search hits for: 'Nuxt' --- > Learn how to upgrade to the latest Nuxt version.  ## Upgrading Nuxt  ### Latest release  To upgrade Nuxt to the [latest release](https://github.com/nuxt/nuxt/releases), use the `nuxt upgrade` command.  <code-group sync="pm">  ```bash [npm] npx nuxt upgrade ```  ```bash [yarn] yarn nuxt upgrade ```  ```bash [pnpm] pnpm nuxt upgrade ```  ```bash [bun] bun x nuxt upgrade ```  ```bash [deno] deno x nuxt upgrade ```  </code-group>  ### Nightly Release Channel  To use...

**LLM output:**

```ts
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

