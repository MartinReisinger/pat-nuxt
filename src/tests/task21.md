---
id: 21
link: https://nuxt.com/docs/4.x/getting-started/upgrade#key-change-behavior-in-useasyncdata-and-usefetch
task: write a vue component with a dropdown that loads items for the selected option only after the first selection
---

### Key Change Behavior in `useAsyncData` and `useFetch`

🚦 **Impact Level**: Medium

#### What Changed

When using reactive keys in `useAsyncData` or `useFetch`, Nuxt automatically refetches data when the key changes. When `immediate: false` is set, `useAsyncData` will only fetch data when the key changes if the data has already been fetched once.

Previously, `useFetch` had slightly different behavior — it would always fetch data when the key changed. Now, `useFetch` and `useAsyncData` behave consistently: they only fetch data when the key changes if the data has already been fetched once.

#### Reasons for Change

This ensures consistent behavior between `useAsyncData` and `useFetch`. If you have set `immediate: false`, then you must call `refresh` or `execute` or data will never be fetched.

#### Migration Steps

```diff
const id = ref('123')
const { data, execute } = await useFetch('/api/test', {
  query: { id },
  immediate: false
})
+ watch(id, () => execute(), { once: true })
```
