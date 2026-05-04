# Task 24

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a nuxt module that generates a plugin file at build time based on module options

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#template-compilation-changes

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```javascript
// nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    ['./module', { message: 'Hello from Nuxt Module!' }],
  ],
})
```

```javascript
// module.ts
import { defineNuxtModule, addPlugin } from 'nuxt/kit'
import { fileURLToPath } from 'url'
import { dirname, resolve } from 'pathe'

export default defineNuxtModule(({ options }) => {
  const currentDir = dirname(fileURLToPath(import.meta.url))
  const pluginPath = resolve(currentDir, 'runtime/my-plugin.ts')

  addPlugin({
    src: pluginPath,
    mode: 'client',
    options: {
      message: options.message || 'Default Message',
    },
  })
})
```

```typescript
// runtime/my-plugin.ts
import { defineNuxtPlugin } from '#app'

export default defineNuxtPlugin((nuxtApp) => {
  const message = __my_plugin_options__.message

  console.log(message)

  return {
    provide: {
      myModuleGreeting: message,
    },
  }
})
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** nuxt, module, plugin, build, generate

> **Found Context:** --- Search hits for: 'nuxt' --- > Learn how to upgrade to the latest Nuxt version.  ## Upgrading Nuxt  ### Latest release  To upgrade Nuxt to the [latest release](https://github.com/nuxt/nuxt/releases), use the `nuxt upgrade` command.  <code-group sync="pm">  ```bash [npm] npx nuxt upgrade ```  ```bash [yarn] yarn nuxt upgrade ```  ```bash [pnpm] pnpm nuxt upgrade ```  ```bash [bun] bun x nuxt upgrade ```  ```bash [deno] deno x nuxt upgrade ```  </code-group>  ### Nightly Release Channel  To use...

**LLM output:**

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    './modules/my-module',
  ],
  myModule: {
    message: 'Hello from my module!',
  },
})

// modules/my-module.ts
import { defineNuxtModule, addPlugin, createResolver } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
  },
  setup(options) {
    const resolver = createResolver(import.meta.url)

    addPlugin({
      src: resolver.resolve('./runtime/plugin.ts'),
      mode: 'client',
    })

    this.nuxt.options.build.transpile.push(resolver.resolve('./runtime'))
  },
})

// modules/runtime/plugin.ts
import { defineNuxtPlugin } from '#app'

export default defineNuxtPlugin((nuxtApp) => {
  console.log('My module plugin is running!')
  console.log('Options:', nuxtApp.options.public.myModule)
})
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```typescript
import { defineNuxtModule, addPlugin, createResolver } from '@nuxt/kit'
import { readFileSync } from 'node:fs'
import { template } from 'es-toolkit/compat'

export default defineNuxtModule({
  meta: {
    name: 'my-generator-module',
    configKey: 'myGenerator',
  },
  setup(options, nuxt) {
    const resolver = createResolver(import.meta.url)

    nuxt.hook('ready', () => {
      addPlugin({
        fileName: 'my-generated-plugin.js',
        getContents({ options: pluginOptions }) {
          const templateContent = readFileSync(resolver.resolve('./runtime/plugin.template.ejs'), 'utf-8')
          return template(templateContent)({ pluginOptions })
        },
        options,
      })
    })
  },
})
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 63 | 278 | 341 |
| Simple DAG | 595 | 267 | 862 |
| Perfect Info | 378 | 205 | 583 |
