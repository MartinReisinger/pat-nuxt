---
id: 14
link: https://nuxt.com/docs/4.x/getting-started/upgrade#shallow-data-reactivity-in-useasyncdata-and-usefetch
task: write a settings page that fetches user preferences and lets the user toggle individual boolean options
---

### Shallow Data Reactivity in `useAsyncData` and `useFetch`

🚦 **Impact Level**: Minimal

The `data` object returned from `useAsyncData`, `useFetch`, `useLazyAsyncData` and `useLazyFetch` is now a `shallowRef` rather than a `ref`.

#### What Changed

When new data is fetched, anything depending on `data` will still be reactive because the entire object is replaced. But if your code changes a property *within* that data structure, this will not trigger any reactivity in your app.

#### Reasons for Change

This brings a **significant** performance improvement for deeply nested objects and arrays because Vue does not need to watch every single property/array for modification. In most cases, `data` should also be immutable.

#### Migration Steps

1. You can granularly opt in to deep reactivity on a per-composable basis:

```diff
- const { data } = useFetch('/api/test')
+ const { data } = useFetch('/api/test', { deep: true })
```

2. You can change the default behavior on a project-wide basis (not recommended):

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  experimental: {
    defaults: {
      useAsyncData: {
        deep: true,
      },
    },
  },
})
```
