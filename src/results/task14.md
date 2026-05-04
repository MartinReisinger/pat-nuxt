# Task 14

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a settings page that fetches user preferences and lets the user toggle individual boolean options

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#shallow-data-reactivity-in-useasyncdata-and-usefetch

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<template>
  <div>
    <h2>Settings</h2>
    <div v-for="setting in settings" :key="setting.key">
      <label>
        {{ setting.label }}
        <input type="checkbox" v-model="setting.value" @change="saveSetting(setting)" />
      </label>
    </div>
  </div>
</template>

<script setup>
const settings = ref([
  { key: 'notifications', label: 'Enable Notifications', value: false },
  { key: 'darkMode', label: 'Dark Mode', value: false },
]);

onMounted(async () => {
  const savedSettings = await fetch('/api/user/settings').then(res => res.json());
  settings.value = settings.value.map(s => ({ ...s, value: savedSettings[s.key] ?? s.value }));
});

const saveSetting = async (setting) => {
  await fetch('/api/user/settings', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ [setting.key]: setting.value }),
  });
};
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** settings, preferences, user, options, toggle

> **Found Context:** --- Search hits for: 'settings' --- For example, if your site requires a `useFetch` call for every page (for example, to get navigation data for a menu, or site settings from a CMS), this data would only be fetched once when prerendering the first page that uses it, and then cached for use when prerendering other pages.  #### Migration Steps  Make sure that any unique key of your data is always resolvable to the same data. For example, if you are using `useAsyncData` to fetch data related to a p...

**LLM output:**

```vue
<script setup lang="ts">
const { data: preferences, refresh } = await useFetch('/api/preferences')

const savePreferences = async () => {
  await $fetch('/api/preferences', {
    method: 'POST',
    body: preferences.value,
  })
  await refresh()
}
</script>

<template>
  <div>
    <h1>Preferences</h1>
    <div v-if="preferences">
      <div v-for="(value, key) in preferences" :key="key" class="preference-item">
        <label :for="key">{{ key }}</label>
        <input type="checkbox" :id="key" v-model="preferences[key]" @change="savePreferences" />
      </div>
    </div>
    <p v-else>Loading preferences...</p>
  </div>
</template>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<template>
  <div>
    <label>
      <input type="checkbox" v-model="settings.notificationsEnabled" />
      Enable Notifications
    </label>
    <label>
      <input type="checkbox" v-model="settings.darkMode" />
      Dark Mode
    </label>
  </div>
</template>

<script setup lang="ts">
const { data: settings } = useFetch('/api/user-settings', { deep: true })
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 64 | 273 | 337 |
| Simple DAG | 16003 | 204 | 16207 |
| Perfect Info | 379 | 115 | 494 |
