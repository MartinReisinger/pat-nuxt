# Task 7

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments, unless absolutely necessary.

**Task Prompt:** write a composable that accepts a userId and returns their profile, auto-updating when the id changes

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#singleton-data-fetching-layer

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```js
// composables/useUserProfile.js
import { ref, watchEffect } from 'vue';

export function useUserProfile(userId) {
  const profile = ref(null);

  watchEffect(async () => {
    if (!userId.value) {
      profile.value = null;
      return;
    }
    const response = await fetch(`/api/users/${userId.value}`);
    profile.value = await response.json();
  });

  return profile;
}
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** composables, fetch, reactive, data, watch

> **Found Context:** --- Search hits for: 'composables' --- composables/   layouts/   middleware/   pages/   plugins/   utils/   app.config.ts   app.vue   router.options.ts content/ layers/ modules/ node_modules/ public/ shared/   types/   utils/ server/   api/   middleware/   plugins/   routes/   utils/ nuxt.config.ts ```  <note>  With this new structure, the `~` alias now points to the `app/` directory by default (your `srcDir`). This means `~/components` resolves to `app/components/`, `~/pages` to `app/pages/`, e...

**LLM output:**

```typescript
// ~/composables/useUserProfile.ts
import { ref, watchEffect } from 'vue'

export function useUserProfile(userId: Ref<number | string>) {
  const profile = ref(null)

  watchEffect(async () => {
    if (userId.value) {
      profile.value = await fetchUserProfile(userId.value)
    } else {
      profile.value = null
    }
  })

  return { profile }
}

async function fetchUserProfile(id: number | string) {
  // Replace with your actual API call
  return { id, name: `User ${id}` }
}
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
// app/composables/useUserProfile.ts
export function useUserProfile (userId: Ref<string> | string) {
  const id = computed(() => typeof userId === 'string' ? userId : userId.value)
  return useAsyncData(
    () => `user-profile-${id.value}`,
    () => $fetch(`/api/users/${id.value}/profile`),
  )
}
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 66 | 113 | 179 |
| Simple DAG | 597 | 156 | 753 |
| Perfect Info | 217 | 94 | 311 |
