# Task 25

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** list the project file structure for a nuxt app (like tree) with middleware grouped into named subfolders

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#directory-index-scanning

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```
.nuxt/
assets/
components/
composables/
content/
layouts/
middleware/
  auth/
  page/
  api/
  shared/
pages/
plugins/
public/
server/
  api/
  middleware/
  plugins/
  routes/
  utils/
nuxt.config.ts
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** structure, file, tree, middleware, folders

> **Found Context:** --- Search hits for: 'structure' --- ### New Directory Structure  🚦 **Impact Level**: Significant  Nuxt now defaults to a new directory structure, with backwards compatibility (so if Nuxt detects you are using the old structure, such as with a top-level `app/pages/` directory, this new structure will not apply).  👉 [See full RFC](https://github.com/nuxt/nuxt/issues/26444)  #### What Changed  - the new Nuxt default `srcDir` is `app/` by default, and most things are resolved from there. - `serverD...

**LLM output:**

```
.
├── app/
│   ├── components/
│   │   └── ui/
│   │       └── Button.vue
│   ├── layouts/
│   │   └── default.vue
│   ├── middleware/
│   │   ├── auth/
│   │   │   └── guest.global.ts
│   │   └── admin/
│   │       └── admin.global.ts
│   ├── pages/
│   │   ├── index.vue
│   │   └── about.vue
│   └── server/
│       └── api/
│           └── hello.ts
├── assets/
│   └── css/
│       └── main.css
├── public/
│   └── favicon.ico
├── nuxt.config.ts
└── package.json
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```
.
├── app
│   ├── middleware
│   │   ├── auth
│   │   │   └── index.ts
│   │   ├── logging
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── plugins
│   └── ...
├── pages
│   └── ...
├── nuxt.config.ts
└── ...
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 67 | 80 | 147 |
| Simple DAG | 579 | 186 | 765 |
| Perfect Info | 287 | 87 | 374 |
