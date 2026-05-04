---
id: 8
link: https://nuxt.com/docs/4.x/getting-started/upgrade#deduplication-of-route-metadata
task: write a script setup block that reads and logs the name of the current route
---

### Deduplication of Route Metadata

🚦 **Impact Level**: Minimal

#### What Changed

It's possible to set some route metadata using `definePageMeta`, such as the `name`, `path`, and so on. Previously these were available both on the route and on route metadata (for example, `route.name` and `route.meta.name`).

Now, they are only accessible on the route object.

#### Reasons for Change

This is a result of enabling `experimental.scanPageMeta` by default, and is a performance optimization.

#### Migration Steps

```diff
const route = useRoute()
  
- console.log(route.meta.name)
+ console.log(route.name)
```
