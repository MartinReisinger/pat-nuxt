# DAG Experiment

## Conditions

1. Baseline. The LLM relies only on its internal training data.
2. Simple DAG. 1. search the docs via a dag for keywords, 2. then answer with the search results in context.
3. Perfect Information. The LLM is already provided with the correct documentation in the user prompt.

## Setup

1. making a python virtual environment (to avoid version conflicts)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. installing necessary imports

```bash
pip install google-genai
pip install python-dotenv
```