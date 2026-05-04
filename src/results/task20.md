# Task 20

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a nuxt module that registers a build hook only after all other modules have finished setup

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#corrected-module-loading-order-in-layers

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```javascript
export default defineNuxtModule({
  setup(options, nuxt) {
    nuxt.hook('modules:done', () => {
      nuxt.addHooks({
        'build:done': async () => {
          console.log('Build hook fired after all modules are done!')
        }
      })
    })
  }
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** build, hook, module, setup, done

> **Found Context:** --- Search hits for: 'build' --- To use the latest Nuxt build and test features before their release, read about the [nightly release channel](/dag_content/4.x/guide/going-further/nightly-release-channel) guide.  ## Testing Nuxt 5  Nuxt 5 is **currently in development**. Until the release, it is possible to test many of Nuxt 5's breaking changes from Nuxt version 4.2+.  ### Opting in to Nuxt 5  First, upgrade Nuxt to the [latest release](https://github.com/nuxt/nuxt/releases).  Then you can set ...

**LLM output:**

```ts
export default defineNuxtModule({
  async setup(options, nuxt) {
    await nuxt.ready()
    nuxt.hook('modules:done', async () => {
      console.log('All modules finished setup!')
    })
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```js
export default defineNuxtModule({
  setup(options, nuxt) {
    nuxt.hook('modules:done', async () => {
      await nuxt.callHook('build:before')
    })
  }
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 66 | 82 | 148 |
| Simple DAG | 15983 | 73 | 16056 |
| Perfect Info | 302 | 57 | 359 |
