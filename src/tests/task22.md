---
id: 22
link: https://nuxt.com/docs/4.x/getting-started/upgrade#respect-defaults-when-clearing-usestate
task: write a script setup block that resets a useState value to undefined
---

### Respect defaults when clearing `useState`

🚦 **Impact Level**: Minimal

#### What Changed

With `compatibilityVersion: 5`, `clearNuxtState` will reset state to its initial value (provided by the `init` function of `useState`) instead of setting it to `undefined`. This aligns `clearNuxtState` behavior with `clearNuxtData`, which already resets to defaults.

#### Reasons for Change

When `clearNuxtState` sets state to `undefined`, composables that depend on that state can crash because they expect the state to always have a valid shape. Resetting to the `init` value ensures state always has a usable default.

#### Migration Steps

If you rely on `clearNuxtState` setting state to `undefined`, you can explicitly pass `{ reset: false }`:

```diff
- clearNuxtState('myKey')
+ clearNuxtState('myKey', { reset: false })
```
