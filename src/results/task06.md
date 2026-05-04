# Task 6

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a composable that caches fetched data but always retrieves fresh data on manual refresh

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#singleton-data-fetching-layer

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```js
import { ref, onMounted, onUnmounted } from 'vue'

export function useCachedFetch(url) {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)
  let controller = null

  const fetchData = async (forceRefresh = false) => {
    if (data.value && !forceRefresh) {
      return
    }
    loading.value = true
    error.value = null
    if (controller) {
      controller.abort()
    }
    controller = new AbortController()
    try {
      const response = await fetch(url, { signal: controller.signal })
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      data.value = await response.json()
    } catch (err) {
      if (err.name !== 'AbortError') {
        error.value = err
      }
    } finally {
      loading.value = false
    }
  }

  onMounted(() => {
    fetchData()
  })

  onUnmounted(() => {
    if (controller) {
      controller.abort()
    }
  })

  const refresh = () => fetchData(true)

  return { data, loading, error, refresh }
}
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** composable, cache, fetch, refresh, override

> **Found Context:** --- Search hits for: 'composable' --- composables/   layouts/   middleware/   pages/   plugins/   utils/   app.config.ts   app.vue   router.options.ts content/ layers/ modules/ node_modules/ public/ shared/   types/   utils/ server/   api/   middleware/   plugins/   routes/   utils/ nuxt.config.ts ```  <note>  With this new structure, the `~` alias now points to the `app/` directory by default (your `srcDir`). This means `~/components` resolves to `app/components/`, `~/pages` to `app/pages/`, et...

**LLM output:**

```ts
export function useCachedFetch<T>(key: string, fn: () => Promise<T>) {
  return useAsyncData(key, fn, {
    getCachedData: (key, nuxtApp, ctx) => {
      if (ctx.cause === 'refresh:manual') {
        return undefined
      }
      return nuxtApp.payload.data[key]
    },
  })
}
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```javascript
export const useMyComposable = (key, fetchFn) => {
  const cachedData = {}

  return useAsyncData(key, fetchFn, {
    getCachedData: (key, nuxtApp, ctx) => {
      if (ctx.cause === 'refresh:manual') return undefined
      return cachedData[key]
    },
    onResponse({ data }) {
      cachedData[key] = data.value
    }
  })
}
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 64 | 311 | 375 |
| Simple DAG | 16461 | 106 | 16567 |
| Perfect Info | 282 | 109 | 391 |
