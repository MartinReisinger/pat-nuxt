# Task 14

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a settings page that fetches user preferences and lets the user toggle individual boolean options

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#shallow-data-reactivity-in-useasyncdata-and-usefetch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <div>
    <h2>Settings</h2>
    <div v-if="preferences">
      <label v-for="(value, key) in preferences" :key="key">
        {{ key }}:
        <input type="checkbox" :checked="value" @change="togglePreference(key, $event.target.checked)">
      </label>
    </div>
    <p v-else>Loading preferences...</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface UserPreferences {
  [key: string]: boolean;
}

const preferences = ref<UserPreferences | null>(null);

// In a real app, you'd fetch this from an API
const fetchPreferences = async () => {
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 500));
  preferences.value = {
    darkMode: false,
    notifications: true,
    analytics: false,
  };
};

const togglePreference = (key: string, newValue: boolean) => {
  if (preferences.value) {
    preferences.value[key] = newValue;
    // In a real app, you'd save this to an API
    console.log(`Preference "${key}" updated to: ${newValue}`);
  }
};

fetchPreferences();
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** settings, preferences, user, toggle, options

> **Found Context:** --- Search hits for: 'settings' --- For example, if your site requires a `useFetch` call for every page (for example, to get navigation data for a menu, or site settings from a CMS), this data would only be fetched once when prerendering the first page that uses it, and then cached for use when prerendering other pages.  #### Migration Steps  Make sure that any unique key of your data is always resolvable to the same data. For example, if you are using `useAsyncData` to fetch data related to a p...

**LLM output:**

```vue
<template>
  <div>
    <h2>Settings</h2>
    <label v-for="(value, key) in preferences" :key="key">
      {{ key }}:
      <input type="checkbox" :checked="value" @change="togglePreference(key)">
    </label>
  </div>
</template>

<script setup lang="ts">
const { data: preferences, pending } = await useFetch('/api/user-preferences')

const togglePreference = async (key: string) => {
  if (!preferences.value) return

  preferences.value[key] = !preferences.value[key]
  await $fetch('/api/update-user-preferences', {
    method: 'POST',
    body: preferences.value,
  })
}
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    <label>
      Enable Feature A:
      <input type="checkbox" v-model="settings.featureA" />
    </label>
    <label>
      Enable Feature B:
      <input type="checkbox" v-model="settings.featureB" />
    </label>
  </div>
</template>

<script setup lang="ts">
const { data: settings } = await useFetch('/api/user-settings', {
  deep: true
})

if (!settings.value) {
  settings.value = { featureA: false, featureB: false }
}
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 62 | 312 | 374 |
| Simple DAG | 540 | 189 | 729 |
| Perfect Info | 377 | 151 | 528 |
