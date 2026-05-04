# Task 8

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a script setup block that reads and logs the name of the current route

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#deduplication-of-route-metadata

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup>
const route = useRoute()
console.log(route.name)
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** route, params, query, name

> **Found Context:** --- Search hits for: 'route' --- - **Normalized Page Names**: Page component names will [match their route names](/dag_content/4.x/getting-started/upgrade#normalized-page-component-names) for consistent `<KeepAlive>` behavior - **clearNuxtState resets to defaults**: `clearNuxtState` will [reset state to its initial value](/dag_content/4.x/getting-started/upgrade#respect-defaults-when-clearing-usestate) instead of setting it to `undefined` - **Non-async callHook**: [`callHook` may return `void`](...

**LLM output:**

```vue
<script setup lang="ts">
const route = useRoute()
console.log(route.name)
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup>
const route = useRoute()
console.log(route.name)
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 63 | 29 | 92 |
| Simple DAG | 16143 | 39 | 16182 |
| Perfect Info | 235 | 29 | 264 |
