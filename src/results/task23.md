# Task 23

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a tsconfig.json that opts into separate type-checking contexts for a nuxt project

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#typescript-configuration-splitting

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```json
{
  "extends": "./.nuxt/tsconfig.json",
  "compilerOptions": {
    "composite": true,
    "moduleResolution": "bundler"
  }
}
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** tsconfig, type, checking, separate, context

> **Found Context:** --- Search hits for: 'tsconfig' --- This change is a follow up to a prior [3.12 config update](https://github.com/nuxt/nuxt/pull/27485) where we improved our defaults, mostly adhering to [TotalTypeScript's recommendations](https://www.totaltypescript.com/tsconfig-cheat-sheet).  #### Migration Steps  There are two approaches:  1. Run a typecheck on your app and fix any new errors (recommended). 2. Override the new default in your `nuxt.config.ts`:```ts export default defineNuxtConfig({   typescri...

**LLM output:**

```json
{
  "files": [],
  "references": [
    {
      "path": "./.nuxt/tsconfig.app.json"
    },
    {
      "path": "./.nuxt/tsconfig.server.json"
    },
    {
      "path": "./.nuxt/tsconfig.shared.json"
    },
    {
      "path": "./.nuxt/tsconfig.node.json"
    }
  ]
}
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

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

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 67 | 48 | 115 |
| Simple DAG | 14730 | 116 | 14846 |
| Perfect Info | 424 | 91 | 515 |
