# Task 20

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a nuxt module that registers a build hook only after all other modules have finished setup

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#corrected-module-loading-order-in-layers

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```js
// nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    './modules/my-module',
  ],
})

// modules/my-module.ts
export default defineNuxtModule({
  async setup(options, nuxt) {
    nuxt.hook('modules:done', () => {
      console.log('My module setup is complete and running after others!');
    })
  },
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** modules, setup, hooks, build, plugins

> **Found Context:** --- Search hits for: 'modules' --- This affects both build-time Nuxt hooks (used by Nuxt modules) and runtime Nuxt hooks (which you might use in your application code).  </tip>  #### Reasons for Change  Hookable v6's `callHook` is 20-40x faster because it avoids creating a `Promise` when one is not needed. This benefits applications with many hook call sites.  #### Migration Steps  If you or your modules use `callHook` with `.then()` or `.catch()` chaining, switch to `await`:  ```diff - nuxtApp....

**LLM output:**

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  hooks: {
    'modules:done': async (nuxt) => {
      nuxt.hook('my:build:hook', () => {
        console.log('My build hook ran after all other modules.')
      })
    }
  }
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```js
// nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    '~/modules/my-module',
  ],
})

// modules/my-module.ts
export default defineNuxtModule({
  setup(options, nuxt) {
    nuxt.hook('modules:done', async () => {
      await nuxt.callHook('my-build-hook', options)
    })
  },
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 64 | 105 | 169 |
| Simple DAG | 594 | 88 | 682 |
| Perfect Info | 317 | 106 | 423 |
