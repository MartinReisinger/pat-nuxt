# DAG Experiment

## Conditions

1. Baseline. The LLM relies only on its internal training data.
2. Simple DAG. Search the docs via a dag for keywords, then answer with the search results in context.
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

3. set your free GEMINI_API_KEY in the .env file
    - go to https://aistudio.google.com/app/api-keys
    - create a project & api key
    - paste it in the [.env.example](.env.example) and remove the '.example'

4. run the experiment.py

```bash
python3 src/experiment.py
```

## Credits & Attribution

This project utilizes documentation from [Nuxt.js](https://github.com/nuxt/nuxt), licensed under the **MIT License**.

* **Data Path:** `dag_content/docs/`
* **Original Source:** [Nuxt GitHub Docs](https://github.com/nuxt/nuxt/tree/main/docs)
* **Copyright:** (c) Nuxt.js Contributors
