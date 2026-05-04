---
id: 4
link: https://nuxt.com/docs/4.x/getting-started/upgrade#scan-page-meta-after-resolution
task: write a nuxt.config.ts hook that sets a custom layout on the home page
---

### Scan Page Meta After Resolution

🚦 **Impact Level**: Minimal

#### What Changed

We now scan page metadata (defined in `definePageMeta`) *after* calling the `pages:extend` hook rather than before.

#### Reasons for Change

This was to allow scanning metadata for pages that users wanted to add in `pages:extend`. We still offer an opportunity to change or override page metadata in a new `pages:resolved` hook.

#### Migration Steps

If you want to override page metadata, do that in `pages:resolved` rather than in `pages:extend`.

```diff
export default defineNuxtConfig({
    hooks: {
-     'pages:extend'(pages) {
+     'pages:resolved'(pages) {
        const myPage = pages.find(page => page.path === '/')
        myPage.meta ||= {}
        myPage.meta.layout = 'overridden-layout'
      }
    }
  })
```

Alternatively, you can revert to the previous behaviour with:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  experimental: {
    scanPageMeta: true,
  },
})
```
