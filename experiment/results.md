# Nuxt 4 DAG Experiment Results

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

---

## Task 1
Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#new-directory-structure

**Task Prompt:** list the project file structure for a nuxt app (like tree) with one index page, a footer and header component as well as google auth middleware

### 1. Baseline Result (task -> answer)
**LLM output:**

```
.
├── app.vue
├── components/
│   ├── TheFooter.vue
│   └── TheHeader.vue
├── middleware/
│   └── auth.global.ts
├── pages/
│   └── index.vue
├── nuxt.config.ts
└── package.json
```

### 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** pages, components, middleware, plugins, server

> **Found Context:** --- Search hits for: 'pages' --- Nuxt now defaults to a new directory structure, with backwards compatibility (so if Nuxt detects you are using the old structure, such as with a top-level `app/pages/` directory, this new structure will not apply).  👉 [See full RFC](https://github.com/nuxt/nuxt/issues/26444)  #### What Changed  - the new Nuxt default `srcDir` is `app/` by default, and most things are resolved from there. - `serverDir` now defaults to `<rootDir>/server` rather than `<srcDir>/serve...

**LLM output:**

```
.
├── app/
│   ├── components/
│   │   ├── Footer.vue
│   │   └── Header.vue
│   ├── middleware/
│   │   └── googleAuth.ts
│   └── pages/
│       └── index.vue
└── nuxt.config.ts
```

### 3. Prefect Result (task & docs -> answer)
**LLM output:**

```
.
├── app
│   ├── app.vue
│   ├── components
│   │   ├── Header.vue
│   │   └── Footer.vue
│   ├── middleware
│   │   └── google-auth.ts
│   └── pages
│       └── index.vue
└── nuxt.config.ts
```

### 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 76 | 67 | 143 |
| Simple DAG | 610 | 91 | 701 |
| Perfect Info | 1299 | 74 | 1373 |

---

## Task 2
Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-window__nuxt__-object

**Task Prompt:** write a short vue-script for the client side, that reads the initial server payload and stores it in a new variable

### 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup>
const payload = useNuxtApp().payload.data
</script>
```

### 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** server, state, payload, restore, initial

> **Found Context:** --- Search hits for: 'server' --- Previously, Nuxt used separate client and server Vite configurations. Now, Nuxt uses a shared Vite configuration with environment-specific plugins that use the `applyToEnvironment()` method to target specific environments.  <tip>  You can test this feature early by setting `future.compatibilityVersion: 5` (see [Testing Nuxt 5](/dag_content/4.x/getting-started/upgrade#testing-nuxt-5)) or by enabling it explicitly with `experimental.viteEnvironmentApi: true`.  </t...

**LLM output:**

```vue
<script setup lang="ts">
import { useNuxtApp } from '#app'

const nuxtApp = useNuxtApp()
const serverPayload = nuxtApp.payload.data
</script>
```

### 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup>
import { useNuxtApp } from '#app'

const nuxtApp = useNuxtApp()
const initialPayload = nuxtApp.payload
</script>
```

### 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 70 | 25 | 95 |
| Simple DAG | 537 | 60 | 597 |
| Perfect Info | 242 | 46 | 288 |

---

