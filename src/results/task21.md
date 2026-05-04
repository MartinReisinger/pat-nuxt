# Task 21

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a vue component with a dropdown that loads items for the selected option only after the first selection

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#key-change-behavior-in-useasyncdata-and-usefetch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <div>
    <select v-model="selectedOption" @change="loadItems">
      <option value="">Select an option</option>
      <option value="option1">Option 1</option>
      <option value="option2">Option 2</option>
    </select>

    <select v-if="items.length" v-model="selectedItem">
      <option value="">Select an item</option>
      <option v-for="item in items" :key="item.id" :value="item.id">
        {{ item.name }}
      </option>
    </select>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const selectedOption = ref('');
const items = ref([]);
const selectedItem = ref('');

const loadItems = async () => {
  if (selectedOption.value) {
    items.value = []; // Clear previous items
    selectedItem.value = ''; // Reset item selection
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 500));
    if (selectedOption.value === 'option1') {
      items.value = [{ id: 1, name: 'Item A' }, { id: 2, name: 'Item B' }];
    } else if (selectedOption.value === 'option2') {
      items.value = [{ id: 3, name: 'Item C' }, { id: 4, name: 'Item D' }];
    }
  }
};
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** dropdown, select, option, lazy, load

> **Found Context:** --- Search hits for: 'select' --- This command will execute all codemods in sequence, with the option to deselect any that you do not wish to run. Each codemod is also listed below alongside its respective change and can be executed independently.  ### New Directory Structure  🚦 **Impact Level**: Significant  Nuxt now defaults to a new directory structure, with backwards compatibility (so if Nuxt detects you are using the old structure, such as with a top-level `app/pages/` directory, this new s...

**LLM output:**

```vue
<template>
  <div>
    <select v-model="selectedOption" @change="loadItemsForSelected">
      <option disabled value="">Please select one</option>
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.text }}
      </option>
    </select>

    <div v-if="items.length">
      <h2>Items for {{ selectedOption }}:</h2>
      <ul>
        <li v-for="item in items" :key="item">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

const options = ref([
  { value: 'option1', text: 'Option 1' },
  { value: 'option2', text: 'Option 2' },
]);
const selectedOption = ref('');
const items = ref([]);
let hasSelected = false;

const loadItemsForSelected = async () => {
  if (selectedOption.value && !hasSelected) {
    hasSelected = true;
    // Simulate fetching items
    items.value = await fetchItems(selectedOption.value);
  }
};

const fetchItems = async (option: string) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve([`Item A for ${option}`, `Item B for ${option}`]);
    }, 500);
  });
};

// This watcher ensures items are loaded if an option is pre-selected or the component mounts with a value
watch(selectedOption, async (newValue) => {
  if (newValue && !hasSelected) {
    hasSelected = true;
    items.value = await fetchItems(newValue);
  }
});
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    <select v-model="selectedOption">
      <option value="">Select an option</option>
      <option value="option1">Option 1</option>
      <option value="option2">Option 2</option>
    </select>

    <div v-if="data">
      {{ data }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useFetch } from '#imports';

const selectedOption = ref('');

const { data, execute } = await useFetch('/api/items', {
  query: { option: selectedOption },
  immediate: false,
});

watch(selectedOption, () => execute());
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 65 | 361 | 426 |
| Simple DAG | 564 | 429 | 993 |
| Perfect Info | 333 | 174 | 507 |
