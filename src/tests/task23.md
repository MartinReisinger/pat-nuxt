---
id: 23
link: https://nuxt.com/docs/4.x/getting-started/upgrade#typescript-configuration-splitting
task: write a tsconfig.json that opts into separate type-checking contexts for a nuxt project
---

### TypeScript Configuration Splitting

🚦 **Impact Level**: Minimal

#### What Changed

Nuxt now generates separate TypeScript configurations for different contexts:

- `.nuxt/tsconfig.app.json` - For your app code (Vue components, composables, etc.)
- `.nuxt/tsconfig.server.json` - For your server-side code (Nitro/server directory)
- `.nuxt/tsconfig.node.json` - For your build-time code (modules, `nuxt.config.ts`, etc.)
- `.nuxt/tsconfig.shared.json` - For code shared between app and server contexts
- `.nuxt/tsconfig.json` - Legacy configuration for backward compatibility

#### Migration Steps

No migration is required. To opt in to improved type checking, update your root `tsconfig.json` to use project references:

**Note:** Remove `"extends": "./.nuxt/tsconfig.json"` if present — project references and extends are mutually exclusive.

```json
{
  "files": [],
  "references": [
    { "path": "./.nuxt/tsconfig.app.json" },
    { "path": "./.nuxt/tsconfig.server.json" },
    { "path": "./.nuxt/tsconfig.shared.json" },
    { "path": "./.nuxt/tsconfig.node.json" }
  ]
}
```

Update your type checking scripts:

```diff
- "typecheck": "nuxt prepare && vue-tsc --noEmit"
+ "typecheck": "nuxt prepare && vue-tsc -b --noEmit"
```
