# Task 17

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write the data fetching logic for a dynamic blog post page

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#shared-prerender-data

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup lang="ts">
const route = useRoute()
const { data: post } = await useFetch(`/api/posts/${route.params.slug}`)
</script>

<template>
  <div>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
  </div>
</template>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** fetch, data, async, await, page

> **Found Context:** --- Search hits for: 'fetch' --- ### Singleton Data Fetching Layer  🚦 **Impact Level**: Moderate  #### What Changed  Nuxt's data fetching system (`useAsyncData` and `useFetch`) has been significantly reorganized for better performance and consistency:  1. **Shared refs for the same key**: All calls to `useAsyncData` or `useFetch` with the same key now share the same `data`, `error` and `status` refs. This means that it is important that all calls with an explicit key must not have conflicting `d...

**LLM output:**

```vue
<script setup lang="ts">
const route = useRoute()
const { data: post } = await useFetch(`/api/posts/${route.params.slug}`)
</script>

<template>
  <div>
    <h1 v-if="post">{{ post.title }}</h1>
    <p v-if="post">{{ post.content }}</p>
    <p v-else>Loading post...</p>
  </div>
</template>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup>
const route = useRoute()
const { data: post } = await useAsyncData(
  `post-${route.params.slug}`,
  () => queryContent('blog').where({ slug: route.params.slug }).findOne()
)
</script>

<template>
  <article v-if="post">
    <h1>{{ post.title }}</h1>
    <p>{{ post.description }}</p>
    <ContentRenderer :value="post" />
  </article>
</template>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 59 | 80 | 139 |
| Simple DAG | 13794 | 114 | 13908 |
| Perfect Info | 411 | 122 | 533 |
