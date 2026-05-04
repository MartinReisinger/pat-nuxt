---
id: 10
link: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-top-level-generate-configuration
task: write a nuxt.config.ts that configures which routes to prerender and which to exclude
---

### Removal of Top-Level `generate` Configuration

🚦 **Impact Level**: Minimal

#### What Changed

The top-level `generate` configuration option is no longer available in Nuxt 4. This includes all of its properties:

- `generate.exclude` - for excluding routes from prerendering
- `generate.routes` - for specifying routes to prerender

#### Reasons for Change

The top level `generate` configuration was a holdover from Nuxt 2. We've supported `nitro.prerender` for a while now, and it is the preferred way to configure prerendering in Nuxt 3+.

#### Migration Steps

Replace `generate` configuration with the corresponding `nitro.prerender` options:

```diff
export default defineNuxtConfig({
- generate: {
-   exclude: ['/admin', '/private'],
-   routes: ['/sitemap.xml', '/robots.txt']
- }
+ nitro: {
+   prerender: {
+     ignore: ['/admin', '/private'],
+     routes: ['/sitemap.xml', '/robots.txt']
+   }
+ }
})
```
