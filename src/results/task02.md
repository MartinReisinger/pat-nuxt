# Task 2

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a short vue-script for the client side, that reads the initial server payload and stores it in a new variable

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-window__nuxt__-object

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup lang="ts">
import { inject } from 'vue'

const serverPayload = inject<any>('nuxt-payload')
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** payload, server, initial, state, data

> **Found Context:** --- Search hits for: 'payload' --- This feature automatically shares payload *data* between pages that are prerendered. This can result in a significant performance improvement when prerendering sites that use `useAsyncData` or `useFetch` and fetch the same data in different pages.  For example, if your site requires a `useFetch` call for every page (for example, to get navigation data for a menu, or site settings from a CMS), this data would only be fetched once when prerendering the first page...

**LLM output:**

```vue
<script setup>
const payload = useState('payload', () => nuxtApp.payload.data)
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup>
const nuxtApp = useNuxtApp()
const initialPayload = nuxtApp.payload
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 70 | 39 | 109 |
| Simple DAG | 537 | 40 | 577 |
| Perfect Info | 242 | 34 | 276 |
