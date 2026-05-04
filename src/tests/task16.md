---
id: 16
link: https://nuxt.com/docs/4.x/getting-started/upgrade#more-granular-inline-styles
task: write a nuxt.config.ts that inlines all css including global stylesheets into the html response
---

### More Granular Inline Styles

🚦 **Impact Level**: Moderate

Nuxt will now only inline styles for Vue components, not global CSS.

#### What Changed

Previously, Nuxt would inline all CSS, including global styles, and remove `<link>` elements to separate CSS files. Now, Nuxt will only do this for Vue components. This allows caching of a single global CSS file and reduces the document download size of the initial request.

#### Migration Steps

This feature is fully configurable and you can revert to the previous behavior by setting `inlineStyles: true` to inline global CSS as well as per-component CSS.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  features: {
    inlineStyles: true,
  },
})
```
