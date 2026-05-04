# Task 13

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a template that renders a fetched post list with a fallback for when no data has loaded

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#default-data-and-error-values-in-useasyncdata-and-usefetch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <div>
    <div v-if="pending">Loading...</div>
    <div v-else-if="error">Error loading posts.</div>
    <ul v-else-if="posts && posts.length">
      <li v-for="post in posts" :key="post.id">
        {{ post.title }}
      </li>
    </ul>
    <div v-else>No posts found.</div>
  </div>
</template>

<script setup lang="ts">
const { pending, data: posts, error } = await useFetch('/api/posts')
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** fetch, suspense, async, data, list

> **Found Context:** --- Search hits for: 'fetch' --- ### Singleton Data Fetching Layer  🚦 **Impact Level**: Moderate  #### What Changed  Nuxt's data fetching system (`useAsyncData` and `useFetch`) has been significantly reorganized for better performance and consistency:  1. **Shared refs for the same key**: All calls to `useAsyncData` or `useFetch` with the same key now share the same `data`, `error` and `status` refs. This means that it is important that all calls with an explicit key must not have conflicting `d...

**LLM output:**

```vue
<template>
  <ul>
    <li v-for="post in posts" :key="post.id">
      {{ post.title }}
    </li>
    <li v-if="!posts">Loading posts...</li>
  </ul>
</template>

<script setup lang="ts">
const { data: posts } = await useFetch('/api/posts')
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    <ul v-if="data?.posts">
      <li v-for="post in data.posts" :key="post.id">
        {{ post.title }}
      </li>
    </ul>
    <div v-else-if="error">
      Error loading posts: {{ error.message }}
    </div>
    <div v-else>
      Loading posts...
    </div>
  </div>
</template>

<script setup lang="ts">
const { data, error } = await useFetch('/api/posts')
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 64 | 141 | 205 |
| Simple DAG | 522 | 99 | 621 |
| Perfect Info | 249 | 134 | 383 |
