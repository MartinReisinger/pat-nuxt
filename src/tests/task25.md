---
id: 25
link: https://nuxt.com/docs/4.x/getting-started/upgrade#directory-index-scanning
task: list the project file structure for a nuxt app (like tree) with middleware grouped into named subfolders
---

### Directory index scanning

🚦 **Impact Level**: Medium

#### What Changed

Child folders in your `app/middleware/` folder are also scanned for `index` files and these are now also registered as middleware in your project.

#### Reasons for Change

Nuxt scans a number of folders automatically, including `app/middleware/` and `app/plugins/`.

Child folders in your `app/plugins/` folder are scanned for `index` files and we wanted to make this behavior consistent between scanned directories.

#### Migration Steps

Probably no migration is necessary but if you wish to revert to previous behavior you can add a hook to filter out these middleware:

```ts
export default defineNuxtConfig({
  hooks: {
    'app:resolve' (app) {
      app.middleware = app.middleware.filter(mw => !/\/index\.[^/]+$/.test(mw.path))
    },
  },
})
```
