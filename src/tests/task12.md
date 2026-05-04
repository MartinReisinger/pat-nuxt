---
id: 12
link: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-deprecated-boolean-values-for-dedupe-option-when-calling-refresh-in-useasyncdata-and-usefetch
task: write a button handler that refreshes fetched data and cancels any in-flight request first
---

### Removal of deprecated `boolean` values for `dedupe` option when calling `refresh` in `useAsyncData` and `useFetch`

🚦 **Impact Level**: Minimal

#### What Changed

Previously it was possible to pass `dedupe: boolean` to `refresh`. These were aliases of `cancel` (`true`) and `defer` (`false`).

#### Reasons for Change

These aliases were removed for greater clarity. `refresh({ dedupe: false })` meant **do not cancel existing requests** but `dedupe: true` in `useAsyncData` options means **do not make new requests if one is pending** — they were opposites.

#### Migration Steps

```diff
const { refresh } = await useAsyncData(async () => ({ message: 'Hello, Nuxt!' }))
  
async function refreshData () {
-   await refresh({ dedupe: true })
+   await refresh({ dedupe: 'cancel' })

-   await refresh({ dedupe: false })
+   await refresh({ dedupe: 'defer' })
}
```
