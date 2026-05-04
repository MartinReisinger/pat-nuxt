---
id: 18
link: https://nuxt.com/docs/4.x/getting-started/upgrade#parsed-errordata
task: write a custom error.vue that displays extra details attached to the thrown error
---

### Parsed `error.data`

🚦 **Impact Level**: Minimal

It was possible to throw an error with a `data` property, but this was not parsed. Now, it is parsed and made available in the `error` object. Although a fix, this is technically a breaking change if you were relying on the previous behavior and parsing it manually.

#### Migration Steps

Update your custom `error.vue` to remove any additional parsing of `error.data`:

```diff
<script setup lang="ts">
  import type { NuxtError } from '#app'

  const props = defineProps({
    error: Object as () => NuxtError
  })

- const data = JSON.parse(error.data)
+ const data = error.data
  </script>
```
