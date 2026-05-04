# Task 17

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write the data fetching logic for a dynamic blog post page

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#shared-prerender-data

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string

const { data: post } = await useFetch(`/api/posts/${slug}`)
</script>

<template>
  <article v-if="post">
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
  </article>
</template>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** fetch, async, data, api, composables

> **Found Context:** --- Search hits for: 'fetch' --- ### Singleton Data Fetching Layer  🚦 **Impact Level**: Moderate  #### What Changed  Nuxt's data fetching system (`useAsyncData` and `useFetch`) has been significantly reorganized for better performance and consistency:  1. **Shared refs for the same key**: All calls to `useAsyncData` or `useFetch` with the same key now share the same `data`, `error` and `status` refs. This means that it is important that all calls with an explicit key must not have conflicting `d...

**LLM output:**

```vue
<template>
  <div>
    <h1>{{ post.title }}</h1>
    <p>{{ post.body }}</p>
  </div>
</template>

<script setup>
const route = useRoute();
const { data: post } = await useFetch(`/api/posts/${route.params.id}`);
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    <h1>{{ post.title }}</h1>
    <p>{{ post.body }}</p>
  </div>
</template>

<script setup>
const route = useRoute()
const { data: post } = await useAsyncData(route.params.slug, () =>
  queryContent(`posts/${route.params.slug}`).findOne()
)
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 57 | 96 | 153 |
| Simple DAG | 508 | 87 | 595 |
| Perfect Info | 409 | 93 | 502 |
