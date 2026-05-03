# INTERNAL.md

## File Logic

### experiment/

- **[experiment.py](src/experiment.py)**: Main entrypoint. Runs all three conditions for each task in `experiment.json` and logs output to
  `results.md`.
- **[dag_api.py](src/dag_api.py)**: Search engine using `ripgrep` to query `dag_content/` and return search results.
- **[experiment.py](src/experiment.py)**: Dataset containing the `task` prompts and the ground-truth `doc` snippets.

### experiment/prompt/

- **[basline_prompt.py](src/prompt/basline_prompt.py)**: Implementation of Condition 1.
  1. just the task, no further docs or instructions
- **[dag_prompt.py](src/prompt/dag_prompt.py)**: Implementation of Condition 2.
  1. prompt with search instruction
  2. call [dag_api.py](src/dag_api.py)
  3. re-prompt with the search results
- **[perfect_prompt.py](src/prompt/perfect_prompt.py)**: Implementation of Condition 3.
  1. the task and the correct documentation of the relevant api change

## Output

### [results.md](src/results.md)

The final "report" containing:

- LLM responses for each condition to compare accuracy.
- Keywords and documentation hits used in the DAG process.
- Token usage tables for cost and efficiency analysis.

---

*For setup and attribution, see [README.md](README.md).*