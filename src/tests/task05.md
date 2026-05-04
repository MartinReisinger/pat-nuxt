---
id: 5
link: https://nuxt.com/docs/4.x/getting-started/upgrade#default-typescript-configuration-changes
task: write a nuxt.config.ts that disables strict undefined checks on array index access
---

### Default TypeScript Configuration Changes

🚦 **Impact Level**: Minimal

#### What Changed

`compilerOptions.noUncheckedIndexedAccess` is now `true` instead of `false`.

#### Reasons for Change

This change is a follow up to a prior [3.12 config update](https://github.com/nuxt/nuxt/pull/27485) where we improved our defaults, mostly adhering to [TotalTypeScript's recommendations](https://www.totaltypescript.com/tsconfig-cheat-sheet).

#### Migration Steps

There are two approaches:

1. Run a typecheck on your app and fix any new errors (recommended).
2. Override the new default in your `nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  typescript: {
    tsConfig: {
      compilerOptions: {
        noUncheckedIndexedAccess: false,
      },
    },
  },
})
```
