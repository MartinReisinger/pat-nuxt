---
id: 19
link: https://nuxt.com/docs/4.x/getting-started/upgrade#new-dom-location-for-spa-loading-screen
task: write a nuxt.config.ts that adds a custom attribute to the spa loading screen element
---

### New DOM Location for SPA Loading Screen

🚦 **Impact Level**: Minimal

#### What Changed

When rendering a client-only page (with `ssr: false`), we now default to rendering the loading screen alongside the Nuxt app root rather than inside it:

```html
<div id="__nuxt"></div>
<!-- spa loading template -->
```

#### Reasons for Change

This allows the spa loading template to remain in the DOM until the Vue app suspense resolves, preventing a flash of white.

#### Migration Steps

If you were targeting the spa loading template with CSS or `document.queryElement` you will need to update your selectors. For this purpose you can use the new `app.spaLoaderTag` and `app.spaLoaderAttrs` configuration options.

Alternatively, you can revert to the previous behaviour with:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  experimental: {
    spaLoadingTemplateLocation: 'within',
  },
})
```
