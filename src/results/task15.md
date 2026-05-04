# Task 15

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a nuxt module that logs the path of every changed file during development

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#absolute-watch-paths-in-builderwatch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    './modules/file-logger'
  ]
})
```

```ts
// modules/file-logger.ts
import { defineNuxtModule } from '@nuxt/kit';

export default defineNuxtModule(() => {
  if (process.dev) {
    return {
      hooks: {
        'file:changed'({ filePath }) {
          console.log(`File changed: ${filePath}`);
        },
      },
    };
  }
});
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** dev, module, hook, server, files

> **Found Context:** --- Search hits for: 'dev' --- Nuxt 5 is **currently in development**. Until the release, it is possible to test many of Nuxt 5's breaking changes from Nuxt version 4.2+.  ### Opting in to Nuxt 5  First, upgrade Nuxt to the [latest release](https://github.com/nuxt/nuxt/releases).  Then you can set your `future.compatibilityVersion` to match Nuxt 5 behavior:  ```ts [nuxt.config.ts]twoslash export default defineNuxtConfig({   future: {     compatibilityVersion: 5,   }, }) ```  When you set your `f...

**LLM output:**

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  hooks: {
    'vite:beforeUpdate': (ctx) => {
      ctx.updates.forEach(update => {
        console.log(`File changed: ${update.path}`)
      })
    },
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
import { defineNuxtModule } from 'nuxt/kit'

export default defineNuxtModule({
  setup() {
    nuxt.hook('builder:watch', async (event, path) => {
      console.log(`${event}: ${path}`)
    })
  }
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 61 | 133 | 194 |
| Simple DAG | 555 | 85 | 640 |
| Perfect Info | 236 | 68 | 304 |
