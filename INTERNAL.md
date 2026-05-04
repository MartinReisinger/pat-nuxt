# INTERNAL.md

## File Logic

### [src](src)

- **[experiment.py](src/experiment.py)**: Main entrypoint. Reads task cases from `src/tests/task*.md`, runs all three conditions for each, and writes results to `src/results/task**.md`.
- **[dag_api.py](src/dag_api.py)**: Search engine using `ripgrep` to query `dag_content/` and return search results.

### [src/tests](src/tests)

- **task01.md … task25.md**: One file per test case. Each file contains YAML frontmatter (`id`, `link`, `task`) and a markdown body with the relevant Nuxt 4 documentation snippet (`doc`).

### [src/condition](src/condition)

- **[basline_prompt.py](src/condition/basline_prompt.py)**: Condition 1 — task only, no docs or search.
- **[dag_prompt.py](src/condition/dag_prompt.py)**: Condition 2 — prompt for keywords → search via `dag_api.py` → re-prompt with results.
- **[perfect_prompt.py](src/condition/perfect_prompt.py)**: Condition 3 — task plus the correct documentation snippet injected directly.

## Output

### [src/results](src/results)

One file per task (`task01.md` … `task25.md`), each containing:

- LLM responses for all three conditions.
- Keywords and documentation hits used in the DAG process.
- Token usage table for cost and efficiency analysis.

---

*For setup and attribution, see [README.md](README.md).*
