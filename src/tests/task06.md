---
id: 6
link: https://nuxt.com/docs/4.x/getting-started/upgrade#singleton-data-fetching-layer
task: write a composable that caches fetched data but always retrieves fresh data on manual refresh
---

### Singleton Data Fetching Layer

🚦 **Impact Level**: Moderate

#### What Changed

2. **More control over getCachedData**: The `getCachedData` function is now called every time data is fetched, even if this is caused by a watcher or calling `refreshNuxtData`. The function now receives a context object with the cause of the request.

#### Migration Steps

```diff
useAsyncData('key', fetchFunction, {
-  getCachedData: (key, nuxtApp) => {
-    return cachedData[key]
-  }
+  getCachedData: (key, nuxtApp, ctx) => {
+    // ctx.cause - can be 'initial' | 'refresh:hook' | 'refresh:manual' | 'watch'
+    if (ctx.cause === 'refresh:manual') return undefined
+    return cachedData[key]
+  }
})
```
