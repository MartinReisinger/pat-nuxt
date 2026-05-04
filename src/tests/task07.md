---
id: 7
link: https://nuxt.com/docs/4.x/getting-started/upgrade#singleton-data-fetching-layer
task: write a composable that accepts a userId and returns their profile, auto-updating when the id changes
---

### Singleton Data Fetching Layer

🚦 **Impact Level**: Moderate

#### What Changed

3. **Reactive key support**: You can now use computed refs, plain refs or getter functions as keys, which enables automatic data refetching (and stores data separately).

It may be beneficial to extract any calls to `useAsyncData` that share an explicit key into their own composable:

```ts [app/composables/useUserData.ts]
export function useUserData (userId: string) {
  return useAsyncData(
    `user-${userId}`,
    () => fetchUser(userId),
  )
}
```
