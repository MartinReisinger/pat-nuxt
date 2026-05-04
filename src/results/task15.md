# Task 15

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a nuxt module that logs the path of every changed file during development

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#absolute-watch-paths-in-builderwatch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```javascript
export default defineNuxtModule({
  setup(options, nuxt) {
    nuxt.hook('builder:watch', (event, path) => {
      console.log(`${event}: ${path}`);
    });
  }
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** module, hooks, server, dev, file

> **Found Context:** --- Search hits for: 'module' --- This affects both build-time Nuxt hooks (used by Nuxt modules) and runtime Nuxt hooks (which you might use in your application code).  </tip>  #### Reasons for Change  Hookable v6's `callHook` is 20-40x faster because it avoids creating a `Promise` when one is not needed. This benefits applications with many hook call sites.  #### Migration Steps  If you or your modules use `callHook` with `.then()` or `.catch()` chaining, switch to `await`:  ```diff - nuxtApp.c...

**LLM output:**

```js
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    nuxt.hook('watcher:change', (event, path) => {
      console.log(`File changed: ${path}`)
    })
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```js
export default defineNuxtModule({
  setup(options, nuxt) {
    nuxt.hook('builder:watch', async (event, path) => {
      console.log(`File changed: ${path}`)
    })
  }
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 63 | 58 | 121 |
| Simple DAG | 16689 | 84 | 16773 |
| Perfect Info | 238 | 60 | 298 |
