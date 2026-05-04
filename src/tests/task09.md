---
id: 9
link: https://nuxt.com/docs/4.x/getting-started/upgrade#unhead-v2
task: write a vue component that sets a page title and meta description
---

### Unhead v2

🚦 **Impact Level**: Minimal

#### What Changed

[Unhead](https://unhead.unjs.io/), used to generate `<head>` tags, has been updated to version 2. While mostly compatible it includes several breaking changes for lower-level APIs.

- Removed props: `vmid`, `hid`, `children`, `body`.
- Promise input no longer supported.
- Tags are now sorted using Capo.js by default.

#### Migration Steps

Verify you're not using any of the removed props.

```diff
useHead({
  meta: [{ 
    name: 'description',
-   vmid: 'description'
-   hid: 'description'
  }]
})
```

While not required it's recommended to update any imports from `@unhead/vue` to `#imports` or `nuxt/app`.

```diff
-import { useHead } from '@unhead/vue'
+import { useHead } from '#imports'
```
