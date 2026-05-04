---
id: 11
link: https://nuxt.com/docs/4.x/getting-started/upgrade#alignment-of-pending-value-in-useasyncdata-and-usefetch
task: write a vue component that fetches data on button click and shows a loading spinner while waiting
---

### Alignment of `pending` value in `useAsyncData` and `useFetch`

🚦 **Impact Level**: Medium

The `pending` object returned from `useAsyncData`, `useFetch`, `useLazyAsyncData` and `useLazyFetch` is now a computed property that is `true` only when `status` is also pending.

#### What Changed

Now, when `immediate: false` is passed, `pending` will be `false` until the first request is made. This is a change from the previous behavior, where `pending` was always `true` until the first request was made.

#### Migration Steps

```diff
<template>
-   <div v-if="!pending">
+   <div v-if="status === 'success'">
      <p>Data: {{ data }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </template>
  <script setup lang="ts">
  const { data, pending, execute, status } = await useAsyncData(() => fetch('/api/data'), {
    immediate: false
  })
  onMounted(() => execute())
  </script>
```
