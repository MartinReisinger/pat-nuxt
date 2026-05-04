---
id: 1
link: https://nuxt.com/docs/4.x/getting-started/upgrade#new-directory-structure
task: list the project file structure for a nuxt app (like tree) with one index page, a footer and header component as well as google auth middleware
---

### New Directory Structure

🚦 **Impact Level**: Significant

Nuxt now defaults to a new directory structure, with backwards compatibility (so if Nuxt detects you are using the old structure, such as with a top-level `app/pages/` directory, this new structure will not apply).

👉 [See full RFC](https://github.com/nuxt/nuxt/issues/26444)

#### What Changed

- the new Nuxt default `srcDir` is `app/` by default, and most things are resolved from there.
- `serverDir` now defaults to `<rootDir>/server` rather than `<srcDir>/server`
- `layers/`, `modules/` and `public/` are resolved relative to `<rootDir>` by default
- if using [Nuxt Content v2.13+](https://github.com/nuxt/content/pull/2649), `content/` is resolved relative to `<rootDir>`
- a new `dir.app` is added, which is the directory we look for `router.options.ts` and `spa-loading-template.html` - this defaults to `<srcDir>/`
- a new `shared/` directory is available for code shared between the Vue app and the Nitro server, with auto-imports for `shared/utils/` and `shared/types/`

An example v4 folder structure:

```sh
.output/
.nuxt/
app/
  assets/
  components/
  composables/
  layouts/
  middleware/
  pages/
  plugins/
  utils/
  app.config.ts
  app.vue
  router.options.ts
content/
layers/
modules/
node_modules/
public/
shared/
  types/
  utils/
server/
  api/
  middleware/
  plugins/
  routes/
  utils/
nuxt.config.ts
```

With this new structure, the `~` alias now points to the `app/` directory by default (your `srcDir`). This means `~/components` resolves to `app/components/`, `~/pages` to `app/pages/`, etc.

#### Migration Steps

1. Create a new directory called `app/`.
2. Move your `assets/`, `components/`, `composables/`, `app/layouts/`, `app/middleware/`, `app/pages/`, `app/plugins/` and `utils/` folders under it, as well as `app.vue`, `error.vue`, `app.config.ts`.
3. Make sure your `nuxt.config.ts`, `content/`, `layers/`, `modules/`, `public/`, `shared/` and `server/` folders remain outside the `app/` folder, in the root of your project.

You can also force a v3 folder structure with the following configuration:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  srcDir: '.',
  dir: {
    app: 'app',
  },
})
```
