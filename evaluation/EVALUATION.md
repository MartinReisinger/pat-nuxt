# Experiment Evaluation

## Pass Rates

| Condition    | Correct | Total | Pass Rate |
|:-------------|:-------:|:-----:|:---------:|
| Baseline     |    4    |  25   |  **16%**  |
| Simple DAG   |   15    |  25   |  **60%**  |
| Perfect Info |   23    |  25   |  **92%**  |

---

## Key Findings

### Baseline (16%)

Here, the model has to rely entirely on its training data. When looking at the examples, one can notice that it
constantly regresses to Nuxt 3 patterns. This also makes sense because its training data can't contain large amounts of
Nuxt 4-specific API information, since Nuxt v4 came out on Jul 16, 2025, and the model's knowledge-cutoff date is Jan. 2025.

The correct answers for tasks 8, 15, 18, and 20 were only achieved where the Nuxt 4 answer is the logical one. In task
eight, it chose `route.name` over the removed `route.meta.name` and no JSON.parse-ing of `error.data`.

In short, the baseline without any extra information only passes tasks where the change simply removed a more
complex action, which already had a simpler alternative.

### Simple DAG (60%)

With the simple retrieval algorithm, we improved the accuracy by more than 350%. By first asking the LLM to come up with
relevant keywords to search the documentation and then injecting the search results into a new prompt, the resulting
output was much less error-prone.

For instance, the first task shows that it came up with keywords like `window` and `payload`, which made the first
result the DAG retrieved the section about the removal of `window.__NUXT__` and the correct replacement
`useNuxtApp().payload` being used in the output. However, it still fails in two obvious ways:

1. **Wrong section retrieved** When searching for generic words like `hooks`, `layout`, and `page`, multiple irrelevant
   sections were matched (for example, Vite plugin hook documentation), pushing the relevant ones (`pages:resolved` in
   this case) outside the retrieval window. This could probably be improved by:
    1. A larger retrieval window and a re-ranking algorithm, so relevant parts do not get pushed out of the retrieval.
    2. Using semantic vector embeddings instead of a simple grep search, better encoding the relevant concept.
2. **Conceptual shortfalls** Tasks where one would have to know the name of the API before searching for it. Like task
   3 (using normalised component names for `KeepAlive`), task 5 (`noUncheckedIndexedAccess`), or 19 (`spaLoaderAttrs`).
   But these all involve configuration keys or behavioral changes, so even a developer would not know about them unless
   they already knew about the change.

### Perfect Info (92%)

Here, the exact documentation about the relevant change from the official Nuxt v4 Upgrade Guide was injected into every
prompt, resulting in only two failures:

1. **Task 24** The correct solution calls `addTemplate()` from `@nuxt/kit` with a `getContents` callback to
   dynamically generate the virtual module. Even with the exact documentation snippet, the model correctly used
   `getContents` but choose `nuxt.options.build.templates.push` instead. All three conditions failed on this task. The
   correct output would have been:
   ```js
   addTemplate({
     fileName: 'my-plugin.js',
     options: { /* module options */ },
     getContents({ options }) {
       const contents = readFileSync(resolver.resolve('./runtime/plugin.ejs'), 'utf-8')
       return template(contents)({ options })
     },
   })
   ```
2. **Task 25** The correct output is the complete `app/` directory tree, with middleware grouped into named subfolders, 
   each containing an `index.ts`. The "Perfect Info" model produced only a small middleware snippet without the `app/`
   root or the `index.ts` files inside each subfolder. This may be due to the non-deterministic characteristics of LLMs 
   or the openness of the task. The expected result would have been:
   ```
   .
   ├── app/
   │   ├── middleware/
   │   │   ├── auth/
   │   │   │   └── index.ts
   │   │   └── guest/
   │   │       └── index.ts
   │   ├── pages/
   │   └── ...
   ├── nuxt.config.ts
   └── package.json
   ```

---

## Failure Patterns

| Pattern                                         | Tasks            | Conditions affected            |
|:------------------------------------------------|:-----------------|:-------------------------------|
| Nuxt 3 hook used instead of Nuxt 4 equivalent   | 1, 4, 25         | Baseline, DAG                  |
| Wrong / invented config key                     | 5, 16, 19        | Baseline, DAG                  |
| Ignores Nuxt composables — uses raw fetch/watch | 6, 7, 11, 14, 21 | Baseline, (DAG for 11, 14, 21) |
| DAG retrieves wrong documentation section       | 4, 3, 5, 19      | Simple DAG                     |
| API does not exist in training data (all fail)  | 24               | All three                      |

---

## Conclusion

Our simple ripgrep-based DAG with keyword search closes most of the gap between baseline and perfect information,
improving pass rate from 16% to 60% (more than tripling accuracy!). Yet the 92% ceiling provided perfect information
shows that there still is a lot of room for improvement. The two main failure types in the Simple DAG section have the
same root cause: keyword search cannot properly represent semantic meaning. Tasks where the developer does not already
know the up-to-date API name (the very cases where documentation lookup is needed the most) are exactly where keyword
search fails.

An embedding-based retrieval approach would address this best, matching the intent of a query against documentation way
better than this surface-level string-overlap. And then, by combining it with a larger retrieval window and a re-ranking
step to prevent relevant sections from being "displaced", this could push accuracy significantly closer to the
perfect-information condition.

---

## Limitations

- **Non-determinism.** Because LLMs are stochastic by nature, re-running the exact same experiment would probably
  produce a different outcome. The results and evaluation only represent a single run per condition and task,
  so one shouldn’t place too much weight on small differences in the pass rate.
- **Small sample size.** Our experiment has only 25 tasks, meaning each percentage point amounts to 0.25 tasks. Or, to
  put it differently: a single answer being different could swing the pass rate by 4%.
- **Single framework.** We consciously scoped our experiment to Nuxt (a Vue-based full-stack framework), specifically
  the
  breaking changes from v3 to v4. So whether the findings generalize to other domains (backend, mobile, embedded, etc.),
  ecosystems (React, Angular, Svelte, etc.), or even other version upgrades (v4 to v5) warrants further investigation.
- **Single LLM.** Our tasks and conditions were all evaluated using the same large language model ( gemini-2.5-flash-lite),
  so we cannot make statements about how a different model with a later knowledge cutoff or better instruction-following
  behavior would behave under these circumstances.
- **Task design.** All tasks were specifically chosen so that Nuxt v4-specific APIs and configurations had to be used,
  while being fully aware that the large language model we are testing can have no more than experimental notes about
  Nuxt 4 in its training data. In fact, that was the goal. So the task set does not represent a variety of problems one
  might solve on a day-to-day basis, but rather a handpicked assortment of extreme edge cases, showcasing the problems
  caused by knowledge cutoff.