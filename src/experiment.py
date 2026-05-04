import json
import os
import sys

from dotenv import load_dotenv  # to read the api key form a .env file
from google import genai  # to use google generative ai via api key in python
from google.genai import types  # to be able to disable tool calls

from prompt import basline_prompt, dag_prompt, perfect_prompt

# setup
load_dotenv()
client = genai.Client()
model_id = 'gemini-2.5-flash-lite'  # free model with knowledge cutoff Jan. 2025

# disable tool colling (aka. websearch) so it can ONLY use our local DAG
no_tools_config = types.GenerateContentConfig(
    tools=[],  # disables all tools and web search
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)  # disables automatic function calling
)

# context (prompt injected before every task prompt)
context_prompt = "You are a Nuxt 4 developer. Respond with a simple answer, using as view lines of code as possible. Only use the official, stable, and public API. No comments and imports, unless absolutely necessary."

# parse task selection from CLI args
# usage: python experiment.py          -> all tasks
#        python experiment.py 1 3 5    -> tasks 1, 3, 5
#        python experiment.py 1-5      -> tasks 1 through 5
#        python experiment.py 1-3 7    -> tasks 1,2,3 and 7
def parse_task_ids(args):
    ids = set()
    for token in args:
        if '-' in token:
            start, end = token.split('-', 1)
            ids.update(range(int(start), int(end) + 1))
        else:
            ids.add(int(token))
    return ids

# loading the test cases
with open("src/experiment.json", "r") as f:
    test_cases = json.load(f)

selected_ids = parse_task_ids(sys.argv[1:]) if sys.argv[1:] else {c['id'] for c in test_cases}
selected_cases = [c for c in test_cases if c['id'] in selected_ids]

os.makedirs("src/results", exist_ok=True)

print(f"\n--- Starting 3-condition Experiment ({len(selected_cases)} tasks)... ---\n")

for i, case in enumerate(selected_cases, 1):
    print(f"Processing Task {case['id']} ({i}/{len(selected_cases)})")

    result_path = f"src/results/task{case['id']:02d}.md"
    with open(result_path, "w") as f:
        f.write(f"# Task {case['id']}\n\n")
        f.write(f"**Context Prompt:** {context_prompt}\n\n")
        f.write(f"**Task Prompt:** {case['task']}\n\n")
        f.write(f"Link to Guide: {case['link']}\n\n")
        f.write("---\n\n")

        # 1. baseline (no docs, no search)
        print("-> (1/3) Running Baseline Prompt...")
        baseline_response, baseline_total_input, baseline_total_output = basline_prompt.run(client, model_id, no_tools_config, context_prompt, case['task'])
        f.write("## 1. Baseline Result (task -> answer)\n")
        f.write("**LLM output:**\n\n")
        f.write(baseline_response.text + "\n\n")

        # 2. simple dag (task + dag_api: 1. search, 2. answer)
        print("-> (2/3) Running Simple DAG Prompt...")
        dag_response, keywords, grep_context, dage_total_input, dag_total_output = dag_prompt.run(client, model_id, no_tools_config, context_prompt, case['task'])
        f.write("## 2. Simple DAG Result (task -> search -> answer)\n")
        f.write(f"> **Keywords used:** {', '.join(keywords)}\n\n")
        f.write(f"> **Found Context:** {grep_context[:500].replace(chr(10), ' ')}...\n\n")
        f.write("**LLM output:**\n\n")
        f.write(dag_response.text + "\n\n")

        # 3. perfect information (task + docs provided)
        print("-> (3/3) Running Perfect Information Prompt...")
        perfect_response, perfect_total_input, perfect_total_output = perfect_prompt.run(client, model_id, no_tools_config, context_prompt, case['task'], case['doc'])
        f.write("## 3. Prefect Result (task & docs -> answer)\n")
        f.write("**LLM output:**\n\n")
        f.write(perfect_response.text + "\n\n")

        f.write("## 4. Token Usage Comparison\n")
        f.write("| Condition | Input Tokens | Output Tokens | Total |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        f.write(f"| Baseline | {baseline_total_input} | {baseline_total_output} | {baseline_total_input + baseline_total_output} |\n")
        f.write(f"| Simple DAG | {dage_total_input} | {dag_total_output} | {dage_total_input + dag_total_output} |\n")
        f.write(f"| Perfect Info | {perfect_total_input} | {perfect_total_output} | {perfect_total_input + perfect_total_output} |\n")
        f.flush()


print(f"\nDone! Written {len(selected_cases)} file(s) to {os.path.abspath('src/results')}/")