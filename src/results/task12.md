# Task 12

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a button handler that refreshes fetched data and cancels any in-flight request first

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-deprecated-boolean-values-for-dedupe-option-when-calling-refresh-in-useasyncdata-and-usefetch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup lang="ts">
import { useFetch } from '#app'

const { data, refresh, pending, error } = useFetch('/api/items')

const handleRefresh = async () => {
  if (pending.value) {
    // Cancel in-flight request (useFetch automatically handles cancellation viaAbortController)
  }
  await refresh()
}
</script>

<template>
  <button @click="handleRefresh" :disabled="pending">
    {{ pending ? 'Refreshing...' : 'Refresh Data' }}
  </button>
</template>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** refetch, abort, cancel, refresh, retry

> **Found Context:** --- Search hits for: 'refetch' --- 2. **More control over getCachedData**: The `getCachedData` function is now called every time data is fetched, even if this is caused by a watcher or calling `refreshNuxtData`. (Previously, new data was always fetched and this function was not called in these cases.) To allow more control over when to use cached data and when to refetch, the function now receives a context object with the cause of the request. 3. **Reactive key support**: You can now use comput...

**LLM output:**

```vue
<template>
  <button @click="handleRefresh">Refresh Data</button>
</template>

<script setup>
import { refreshNuxtData } from '#app'

const handleRefresh = () => {
  refreshNuxtData('your-data-key')
}
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup>
const { refresh } = await useAsyncData('data', () => $fetch('/api/data'))

async function refreshAndCancel () {
  await refresh({ dedupe: 'cancel' })
}
</script>

<template>
  <button @click="refreshAndCancel">Refresh and Cancel</button>
</template>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 63 | 133 | 196 |
| Simple DAG | 505 | 81 | 586 |
| Perfect Info | 309 | 82 | 391 |
