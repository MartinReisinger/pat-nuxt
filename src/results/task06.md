# Task 6

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a composable that caches fetched data but always retrieves fresh data on manual refresh

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#singleton-data-fetching-layer

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```js
import { ref, watch, onUnmounted } from 'vue';

export function useCachedFetch(fetchFn, options = {}) {
  const data = ref(null);
  const error = ref(null);
  const loading = ref(false);

  const fetchData = async (forceRefresh = false) => {
    if (data.value && !forceRefresh) {
      return;
    }
    loading.value = true;
    error.value = null;
    try {
      data.value = await fetchFn();
    } catch (err) {
      error.value = err;
    } finally {
      loading.value = false;
    }
  };

  fetchData();

  onUnmounted(() => {
    // Optional: Cleanup logic if needed
  });

  return {
    data,
    error,
    loading,
    refresh: () => fetchData(true),
  };
}
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** composable, caching, fetch, refresh, data

> **Found Context:** --- Search hits for: 'composable' --- composables/   layouts/   middleware/   pages/   plugins/   utils/   app.config.ts   app.vue   router.options.ts content/ layers/ modules/ node_modules/ public/ shared/   types/   utils/ server/   api/   middleware/   plugins/   routes/   utils/ nuxt.config.ts ```  <note>  With this new structure, the `~` alias now points to the `app/` directory by default (your `srcDir`). This means `~/components` resolves to `app/components/`, `~/pages` to `app/pages/`, et...

**LLM output:**

```ts
// composables/useCachedFetch.ts
import { ref, readonly } from 'vue'
import { $fetch } from 'ofetch'

export function useCachedFetch<T>(url: string, options: Parameters<typeof $fetch>[1] = {}) {
  const data = ref<T | null>(null)
  const loading = ref(false)
  const error = ref<any>(null)

  const fetchData = async () => {
    loading.value = true
    error.value = null
    try {
      data.value = await $fetch<T>(url, options)
    } catch (err) {
      error.value = err
    } finally {
      loading.value = false
    }
  }

  const refresh = () => {
    fetchData()
  }

  // Fetch on initial load if not disabled
  if (options.immediate !== false) {
    fetchData()
  }

  return {
    data: readonly(data),
    loading: readonly(loading),
    error: readonly(error),
    refresh,
  }
}
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
export function useFetchWithManualRefresh<T>(
  key: string,
  fetchFn: () => Promise<T>,
  options: { server?: boolean; lazy?: boolean } = {}
) {
  const cachedData: Record<string, T> = {}

  return useAsyncData<T>(key, fetchFn, {
    getCachedData: (key, nuxtApp, ctx) => {
      if (ctx.cause === 'refresh:manual') {
        return undefined
      }
      return cachedData[key]
    },
    onFetchError: ({ data }) => {
      throw data
    },
    ...options,
  })
}
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 62 | 215 | 277 |
| Simple DAG | 589 | 262 | 851 |
| Perfect Info | 280 | 156 | 436 |
