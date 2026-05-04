---
id: 24
link: https://nuxt.com/docs/4.x/getting-started/upgrade#template-compilation-changes
task: write a nuxt module that generates a plugin file at build time based on module options
---

### Template Compilation Changes

🚦 **Impact Level**: Minimal

#### What Changed

Previously, Nuxt used `lodash/template` to compile templates located on the file system using the `.ejs` file format/syntax.

In addition, we provided some template utilities (`serialize`, `importName`, `importSources`) which could be used for code-generation within these templates, which are now being removed.

#### Reasons for Change

In Nuxt v3 we moved to a 'virtual' syntax with a `getContents()` function which is much more flexible and performant. In addition, `lodash/template` has had a succession of security issues and is a hefty dependency unused by most projects.

#### Migration Steps

```diff
+ import { readFileSync } from 'node:fs'
+ import { template } from 'es-toolkit/compat'
  addTemplate({
    fileName: 'my-plugin.js',
    options: { /* some options */ },
-   src: resolver.resolve('./runtime/plugin.ejs'),
+   getContents({ options }) {
+     const contents = readFileSync(resolver.resolve('./runtime/plugin.ejs'), 'utf-8')
+     return template(contents)({ options })
+   },
  })
```

You can automate this step by running `npx codemod@latest nuxt/4/template-compilation-changes`
