---
id: 15
link: https://nuxt.com/docs/4.x/getting-started/upgrade#absolute-watch-paths-in-builderwatch
task: write a nuxt module that logs the path of every changed file during development
---

### Absolute Watch Paths in `builder:watch`

🚦 **Impact Level**: Minimal

#### What Changed

The Nuxt `builder:watch` hook now emits a path which is absolute rather than relative to your project `srcDir`.

#### Reasons for Change

This allows us to support watching paths which are outside your `srcDir`, and offers better support for layers and other more complex patterns.

#### Migration Steps

```diff
+ import { relative, resolve } from 'node:fs'
  // ...
  nuxt.hook('builder:watch', async (event, path) => {
+   path = relative(nuxt.options.srcDir, resolve(nuxt.options.srcDir, path))
    // ...
  })
```
