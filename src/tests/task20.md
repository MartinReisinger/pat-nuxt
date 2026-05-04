---
id: 20
link: https://nuxt.com/docs/4.x/getting-started/upgrade#corrected-module-loading-order-in-layers
task: write a nuxt module that registers a build hook only after all other modules have finished setup
---

### Corrected Module Loading Order in Layers

🚦 **Impact Level**: Minimal

#### What Changed

The order in which modules are loaded when using Nuxt layers has been corrected. Previously, modules from the project root were loaded before modules from extended layers, which was the reverse of the expected behavior.

Now modules are loaded in the correct order:

1. **Layer modules first** (in extend order - deeper layers first)
2. **Project modules last** (highest priority)

#### Migration Steps

If you encounter issues with module order dependencies due to needing to register a hook, consider using the `modules:done` hook for modules that need to call a hook. This is run after all other modules have been loaded, which means it is safe to use.

👉 See [PR #31507](https://github.com/nuxt/nuxt/pull/31507) and [issue #25719](https://github.com/nuxt/nuxt/issues/25719) for more details.
