# Task 11

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a vue component that fetches data on button click and shows a loading spinner while waiting

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#alignment-of-pending-value-in-useasyncdata-and-usefetch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <div>
    <button @click="fetchData" :disabled="loading">
      {{ loading ? 'Loading...' : 'Fetch Data' }}
    </button>
    <div v-if="data">{{ data }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const data = ref(null)
const loading = ref(false)

const fetchData = async () => {
  loading.value = true
  try {
    // Replace with your actual API call
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1')
    data.value = await response.json()
  } catch (error) {
    console.error('Error fetching data:', error)
  } finally {
    loading.value = false
  }
}
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** fetch, data, button, click, loading

> **Found Context:** --- Search hits for: 'fetch' --- ### Singleton Data Fetching Layer  🚦 **Impact Level**: Moderate  #### What Changed  Nuxt's data fetching system (`useAsyncData` and `useFetch`) has been significantly reorganized for better performance and consistency:  1. **Shared refs for the same key**: All calls to `useAsyncData` or `useFetch` with the same key now share the same `data`, `error` and `status` refs. This means that it is important that all calls with an explicit key must not have conflicting `d...

**LLM output:**

```vue
<script setup lang="ts">
const data = ref(null)
const loading = ref(false)

async function fetchData() {
  loading.value = true
  try {
    data.value = await $fetch('/api/my-data')
  } catch (error) {
    console.error('Error fetching data:', error)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <button @click="fetchData" :disabled="loading">
    {{ loading ? 'Loading...' : 'Fetch Data' }}
  </button>
  <div v-if="data">
    {{ data }}
  </div>
</template>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <button @click="execute" :disabled="status === 'pending'">
    Fetch Data
  </button>
  <div v-if="status === 'pending'">
    Loading...
  </div>
  <div v-else-if="status === 'success'">
    Data: {{ data }}
  </div>
</template>

<script setup lang="ts">
const { data, execute, status } = await useAsyncData(() => Promise.resolve('My Data'), {
  immediate: false
})
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 65 | 195 | 260 |
| Simple DAG | 16344 | 173 | 16517 |
| Perfect Info | 347 | 126 | 473 |
