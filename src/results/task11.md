# Task 11

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

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
    <div v-if="data">
      {{ data }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const data = ref(null);
const loading = ref(false);

const fetchData = async () => {
  loading.value = true;
  try {
    await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate API call
    data.value = 'Data fetched successfully!';
  } catch (error) {
    console.error('Error fetching data:', error);
    data.value = 'Error loading data.';
  } finally {
    loading.value = false;
  }
};
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** fetch, data, button, click, loading

> **Found Context:** --- Search hits for: 'fetch' --- ### Singleton Data Fetching Layer  🚦 **Impact Level**: Moderate  #### What Changed  Nuxt's data fetching system (`useAsyncData` and `useFetch`) has been significantly reorganized for better performance and consistency:  1. **Shared refs for the same key**: All calls to `useAsyncData` or `useFetch` with the same key now share the same `data`, `error` and `status` refs. This means that it is important that all calls with an explicit key must not have conflicting `d...

**LLM output:**

```vue
<template>
  <div>
    <button @click="fetchData" :disabled="loading">Fetch Data</button>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error.message }}</div>
    <pre v-else>{{ data }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { $fetch } from 'nitropack' // Assuming $fetch is available globally or imported

const data = ref(null)
const loading = ref(false)
const error = ref(null)

const fetchData = async () => {
  loading.value = true
  error.value = null
  try {
    data.value = await $fetch('/api/your-endpoint')
  } catch (e) {
    error.value = e
  } finally {
    loading.value = false
  }
}
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    <button @click="execute" :disabled="status === 'pending'">Fetch Data</button>
    <div v-if="status === 'pending'">Loading...</div>
    <div v-else-if="status === 'success'">Data: {{ data }}</div>
    <div v-else>Error fetching data</div>
  </div>
</template>

<script setup lang="ts">
const { data, execute, status } = await useAsyncData('myData', () => $fetch('/api/data'), {
  immediate: false
})
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 63 | 206 | 269 |
| Simple DAG | 520 | 229 | 749 |
| Perfect Info | 345 | 135 | 480 |
