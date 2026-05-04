---
id: 17
link: https://nuxt.com/docs/4.x/getting-started/upgrade#shared-prerender-data
task: write the data fetching logic for a dynamic blog post page
---

### Shared Prerender Data

🚦 **Impact Level**: Medium

#### What Changed

We enabled a previously experimental feature to share data from `useAsyncData` and `useFetch` calls, across different pages.

#### Reasons for Change

This feature automatically shares payload *data* between pages that are prerendered. This can result in a significant performance improvement when prerendering sites that use `useAsyncData` or `useFetch` and fetch the same data in different pages.

#### Migration Steps

Make sure that any unique key of your data is always resolvable to the same data. For example, if you are using `useAsyncData` to fetch data related to a particular page, you should provide a key that uniquely matches that data. (`useFetch` should do this automatically for you.)

```ts [app/pages/test/[slug].vue]
// This would be unsafe in a dynamic page (e.g. `[slug].vue`) because the route slug makes a difference
// to the data fetched, but Nuxt can't know that because it's not reflected in the key.
const route = useRoute()
const { data } = await useAsyncData(async () => {
  return await $fetch(`/api/my-page/${route.params.slug}`)
})
// Instead, you should use a key that uniquely identifies the data fetched.
const { data } = await useAsyncData(route.params.slug, async () => {
  return await $fetch(`/api/my-page/${route.params.slug}`)
})
```
