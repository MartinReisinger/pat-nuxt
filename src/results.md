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
├── components/
│   ├── Footer.vue
│   └── Header.vue
├── middleware/
│   └── auth.global.ts
├── pages/
│   └── index.vue
├── app.vue
└── nuxt.config.ts
```

### 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** pages, components, middleware, nuxt.config.ts, plugins

> **Found Context:** --- Search hits for: 'pages' --- Nuxt now defaults to a new directory structure, with backwards compatibility (so if Nuxt detects you are using the old structure, such as with a top-level `app/pages/` directory, this new structure will not apply).  👉 [See full RFC](https://github.com/nuxt/nuxt/issues/26444)  #### What Changed  - the new Nuxt default `srcDir` is `app/` by default, and most things are resolved from there. - `serverDir` now defaults to `<rootDir>/server` rather than `<srcDir>/serve...

**LLM output:**

```
.
├── app/
│   ├── components/
│   │   ├── Footer.vue
│   │   └── Header.vue
│   ├── middleware/
│   │   └── google-auth.global.ts
│   └── pages/
│       └── index.vue
└── nuxt.config.ts
```

### 3. Prefect Result (task & docs -> answer)
**LLM output:**

```
.
├── app/
│   ├── components/
│   │   ├── Header.vue
│   │   └── Footer.vue
│   ├── middleware/
│   │   └── googleAuth.ts
│   ├── pages/
│   │   └── index.vue
│   └── app.vue
├── nuxt.config.ts
└── package.json
```

### 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 76 | 60 | 136 |
| Simple DAG | 610 | 88 | 698 |
| Perfect Info | 1299 | 84 | 1383 |

---

## Task 2
Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-window__nuxt__-object

**Task Prompt:** write a short vue-script for the client side, that reads the initial server payload and stores it in a new variable

### 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup>
const payload = JSON.parse(import.meta.env.SSR ? window.__NUXT__.payload : '{}');
</script>
```

### 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** client, payload, data, server, read

> **Found Context:** --- Search hits for: 'client' --- - **Comment node placeholders**: Client-only components use [comment nodes instead of `<div>`](/dag_content/4.x/getting-started/upgrade#client-only-comment-placeholders) as SSR placeholders, fixing a scoped styles hydration issue - Other Nuxt 5 improvements and changes as they become available  <note>  This section is subject to change until the final release, so please check back here regularly if you are testing Nuxt 5 using `future.compatibilityVersion: 5`.  ...

**LLM output:**

```vue
<script setup lang="ts">
const clientPayload = usePayload()
</script>
```

### 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup>
import { useNuxtApp } from '#app'

const initialPayload = useNuxtApp().payload
</script>
```

### 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 70 | 39 | 109 |
| Simple DAG | 522 | 33 | 555 |
| Perfect Info | 242 | 36 | 278 |

---

