# Task 24

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a nuxt module that generates a plugin file at build time based on module options

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#template-compilation-changes

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```js
export default defineNuxtModule({
  setup(options, nuxt) {
    nuxt.hook('build:before', () => {
      nuxt.options.plugins.push({
        src: resolve(__dirname, 'runtime/plugin.ts'),
        options
      })
    })
  }
})

// runtime/plugin.ts
export default defineNuxtPlugin((nuxtApp) => {
  const { $config } = nuxtApp
  console.log('Module options:', $config.public.myModuleOptions)
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** module, plugin, generate, build, options

> **Found Context:** --- Search hits for: 'module' --- This affects both build-time Nuxt hooks (used by Nuxt modules) and runtime Nuxt hooks (which you might use in your application code).  </tip>  #### Reasons for Change  Hookable v6's `callHook` is 20-40x faster because it avoids creating a `Promise` when one is not needed. This benefits applications with many hook call sites.  #### Migration Steps  If you or your modules use `callHook` with `.then()` or `.catch()` chaining, switch to `await`:  ```diff - nuxtApp.c...

**LLM output:**

```ts
import { defineNuxtModule, createResolver } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-generator-module',
  },
  setup (options, nuxt) {
    const resolver = createResolver(import.meta.url)

    nuxt.hook('build:before', async () => {
      const pluginContent = `export default defineNuxtPlugin((nuxtApp) => {
        console.log('Hello from generated plugin with option:', ${JSON.stringify(options.message || 'default')})
      })`

      const pluginPath = resolver.resolve('./runtime/generated-plugin.ts')
      await nuxt.callHook('prepare:virtual', {
        '#generated-plugin': pluginContent,
      })
      nuxt.options.plugins.push({ src: '#generated-plugin', mode: 'client' })
      nuxt.options.plugins.push({ src: '#generated-plugin', mode: 'server' })
    })
  },
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```js
export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule'
  },
  setup(options, nuxt) {
    const { resolve } = nuxt.options.alias
    nuxt.options.build.templates.push({
      fileName: 'my-plugin.js',
      getContents({ options }) {
        const contents = readFileSync(resolve('./runtime/plugin.ejs'), 'utf-8')
        return template(contents)({ options })
      },
      options
    })
  }
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 65 | 125 | 190 |
| Simple DAG | 16247 | 244 | 16491 |
| Perfect Info | 380 | 137 | 517 |
