---
id: 3
link: https://nuxt.com/docs/4.x/getting-started/upgrade#normalized-component-names
task: set up KeepAlive on NuxtPage so a 'user-id' component inside a subfolder stays mounted between navigations
---

### Normalized Component Names

🚦 **Impact Level**: Moderate

Vue will now generate component names that match the Nuxt pattern for component naming.

#### What Changed

By default, if you haven't set it manually, Vue will assign a component name that matches the filename of the component.

```bash [Directory structure]
├─ components/
├─── SomeFolder/
├───── MyComponent.vue
```

In this case, the component name would be `MyComponent`, as far as Vue is concerned. If you wanted to use `<KeepAlive>` with it, or identify it in the Vue DevTools, you would need to use this name.

But in order to auto-import it, you would need to use `SomeFolderMyComponent`.

With this change, these two values will match, and Vue will generate a component name that matches the Nuxt pattern for component naming.

#### Migration Steps

Ensure that you use the updated name in any tests which use `findComponent` from `@vue/test-utils` and in any `<KeepAlive>` which depends on the name of your component.

```diff
- <NuxtPage :keepalive="{ include: ['MyComponent'] }" />
+ <NuxtPage :keepalive="{ include: ['SomeFolderMyComponent'] }" />
```

Alternatively, for now, you can disable this behaviour with:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  experimental: {
    normalizeComponentNames: false,
  },
})
```
