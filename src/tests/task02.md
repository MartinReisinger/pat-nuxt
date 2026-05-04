---
id: 2
link: https://nuxt.com/docs/4.x/getting-started/upgrade#removal-of-window__nuxt__-object
task: write a short vue-script for the client side, that reads the window's initial server payload and stores it in a new variable
---

### Removal of `window.__NUXT__` object

#### What Changed

We are removing the global `window.__NUXT__` object after the app finishes hydration.

#### Reasons for Change

This opens the way to multi-app patterns ([#21635](https://github.com/nuxt/nuxt/issues/21635)) and enables us to focus on a single way to access Nuxt app data - `useNuxtApp()`.

#### Migration Steps

The data is still available, but can be accessed with `useNuxtApp().payload`:

```diff
- console.log(window.__NUXT__)
+ console.log(useNuxtApp().payload)
```
