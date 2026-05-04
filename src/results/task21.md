# Task 21

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a vue component with a dropdown that loads items for the selected option only after the first selection

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#key-change-behavior-in-useasyncdata-and-usefetch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup>
const options = ['Option A', 'Option B'];
const selectedOption = ref(null);
const loadedItems = ref([]);

const loadItems = async (option) => {
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 500));
  loadedItems.value = [`Item 1 for ${option}`, `Item 2 for ${option}`];
};

watch(selectedOption, async (newOption) => {
  if (newOption) {
    await loadItems(newOption);
  }
}, { immediate: true });
</script>

<template>
  <div>
    <select v-model="selectedOption">
      <option disabled value="">Please select one</option>
      <option v-for="option in options" :key="option" :value="option">{{ option }}</option>
    </select>

    <ul v-if="loadedItems.length">
      <li v-for="(item, index) in loadedItems" :key="index">{{ item }}</li>
    </ul>
  </div>
</template>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** dropdown, select, change, lazy, load

> **Found Context:** --- Search hits for: 'select' --- This command will execute all codemods in sequence, with the option to deselect any that you do not wish to run. Each codemod is also listed below alongside its respective change and can be executed independently.  ### New Directory Structure  🚦 **Impact Level**: Significant  Nuxt now defaults to a new directory structure, with backwards compatibility (so if Nuxt detects you are using the old structure, such as with a top-level `app/pages/` directory, this new s...

**LLM output:**

```vue
<template>
  <div>
    <select id="locale-chooser" v-model="selectedLocale" @change="loadItemsForLocale">
      <option v-for="loc of locales" :key="loc" :value="loc">
        {{ loc }}
      </option>
    </select>

    <div v-if="loadedItems">
      <p v-for="item in loadedItems" :key="item">{{ item }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
const locales = ['en', 'fr', 'es']
const selectedLocale = ref(locales[0])
const loadedItems = ref<string[] | null>(null)

const loadItemsForLocale = async () => {
  if (selectedLocale.value) {
    // Simulate fetching items based on the selected locale
    await new Promise(resolve => setTimeout(resolve, 500))
    loadedItems.value = [`Items for ${selectedLocale.value}`]
  }
}

onMounted(() => {
  // Load items for the initial selected locale if needed, or wait for first user interaction
  // For this example, we wait for user interaction.
})
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <select v-model="selectedOption">
    <option value="posts">Posts</option>
    <option value="users">Users</option>
  </select>
  <div v-if="data">{{ data }}</div>
</template>

<script setup>
const selectedOption = ref('')
const { data, execute } = await useAsyncData(
  () => selectedOption.value ? `/api/${selectedOption.value}` : null,
  { immediate: false }
)

watch(selectedOption, () => execute(), { immediate: false })
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 67 | 251 | 318 |
| Simple DAG | 15591 | 288 | 15879 |
| Perfect Info | 335 | 138 | 473 |
