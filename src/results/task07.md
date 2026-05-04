# Task 7

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary.

**Task Prompt:** write a composable that accepts a userId and returns their profile, auto-updating when the id changes

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#singleton-data-fetching-layer

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```js
import { ref, watch } from 'vue';

export function useUserProfile(userId) {
  const profile = ref(null);

  watch(userId, async (newId) => {
    if (newId) {
      const response = await fetch(`/api/users/${newId}`);
      profile.value = await response.json();
    } else {
      profile.value = null;
    }
  }, { immediate: true });

  return profile;
}
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** composable, reactivity, watch, ref, asyncData

> **Found Context:** --- Search hits for: 'composable' --- composables/   layouts/   middleware/   pages/   plugins/   utils/   app.config.ts   app.vue   router.options.ts content/ layers/ modules/ node_modules/ public/ shared/   types/   utils/ server/   api/   middleware/   plugins/   routes/   utils/ nuxt.config.ts ```  <note>  With this new structure, the `~` alias now points to the `app/` directory by default (your `srcDir`). This means `~/components` resolves to `app/components/`, `~/pages` to `app/pages/`, et...

**LLM output:**

```typescript
// app/composables/useUserProfile.ts
export function useUserProfile(userId: Ref<string>) {
  return useAsyncData(
    () => `user-profile-${userId.value}`,
    () => $fetch(`/api/users/${userId.value}/profile`)
  )
}
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```ts
export function useUserProfile (userId: Ref<string>) {
  return useAsyncData(
    () => `user-profile-${userId.value}`,
    () => $fetch(`/api/users/${userId.value}/profile`)
  )
}
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 68 | 111 | 179 |
| Simple DAG | 16434 | 80 | 16514 |
| Perfect Info | 219 | 59 | 278 |
