# Task 2

**Context Prompt:** You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments and imports, unless absolutely necessary.

**Task Prompt:** write a short vue-script for the client side, that reads the window's initial server payload and stores it in a new variable

Link to Guide: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-window__nuxt__-object

---

## 1. Baseline Result (task -> answer)
**LLM output:**

```vue
<script setup>
const serverPayload = window.__NUXT__;
</script>
```

## 2. Simple DAG Result (task -> search -> answer)
> **Keywords used:** window, payload, server, initial, state

> **Found Context:** --- Search hits for: 'window' --- ### Removal of `window.__NUXT__` object  #### What Changed  We are removing the global `window.__NUXT__` object after the app finishes hydration.  #### Reasons for Change  This opens the way to multi-app patterns ([#21635](https://github.com/nuxt/nuxt/issues/21635)) and enables us to focus on a single way to access Nuxt app data - `useNuxtApp()`.  #### Migration Steps  The data is still available, but can be accessed with `useNuxtApp().payload`:  ```diff - conso...

**LLM output:**

```vue
<script setup>
const initialPayload = useNuxtApp().payload
</script>
```

## 3. Prefect Result (task & docs -> answer)
**LLM output:**

```vue
<script setup>
const nuxtApp = useNuxtApp()
const initialPayload = nuxtApp.payload
</script>
```

## 4. Token Usage Comparison
| Condition | Input Tokens | Output Tokens | Total |
| :--- | :--- | :--- | :--- |
| Baseline | 75 | 25 | 100 |
| Simple DAG | 573 | 33 | 606 |
| Perfect Info | 247 | 34 | 281 |
