---
id: 13
link: https://nuxt.com/docs/4.x/getting-started/upgrade#default-data-and-error-values-in-useasyncdata-and-usefetch
task: write a template that renders a fetched post list with a fallback for when no data has loaded
---

### Default `data` and `error` values in `useAsyncData` and `useFetch`

🚦 **Impact Level**: Minimal

#### What Changed

`data` and `error` objects returned from `useAsyncData` will now default to `undefined`.

#### Reasons for Change

Previously `data` was initialized to `null` but reset in `clearNuxtData` to `undefined`. `error` was initialized to `null`. This change is to bring greater consistency.

#### Migration Steps

If you were checking if `data.value` or `error.value` were `null`, you can update these checks to check for `undefined` instead.

You can automate this step by running `npx codemod@latest nuxt/4/default-data-error-value`
