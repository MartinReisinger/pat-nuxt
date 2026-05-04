# Task 25

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** list the project file structure for a nuxt app (like tree) with middleware grouped into named subfolders

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#directory-index-scanning

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```
.
├── app.vue
├── components/
├── layouts/
├── middleware/
│   ├── auth/
│   │   └── index.ts
│   ├── guest/
│   │   └── index.ts
│   └── index.ts
├── pages/
├── plugins/
├── public/
├── server/
├── utils/
├── nuxt.config.ts
└── package.json
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** structure, tree, middleware, folder, grouping

> **Found Context:** --- Search hits for: 'structure' --- ### New Directory Structure  🚦 **Impact Level**: Significant  Nuxt now defaults to a new directory structure, with backwards compatibility (so if Nuxt detects you are using the old structure, such as with a top-level `app/pages/` directory, this new structure will not apply).  👉 [See full RFC](https://github.com/nuxt/nuxt/issues/26444)  #### What Changed  - the new Nuxt default `srcDir` is `app/` by default, and most things are resolved from there. - `serverD...

**LLM output:**

```bash
.
├── app/
│   ├── components/
│   ├── composables/
│   ├── layouts/
│   ├── middleware/
│   │   ├── auth/
│   │   ├── guest/
│   │   └── index.ts
│   ├── pages/
│   ├── plugins/
│   └── utils/
├── assets/
├── public/
├── server/
│   ├── api/
│   ├── middleware/
│   ├── plugins/
│   └── routes/
├── nuxt.config.ts
├── package.json
└── tsconfig.json
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```
pages/
  index.vue
middleware/
  auth/
    index.global.ts
  guest/
    index.global.ts
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 69 | 92 | 161 |
| Simple DAG | 15902 | 143 | 16045 |
| Perfect Info | 289 | 36 | 325 |
