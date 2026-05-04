import glob
import os
import sys

from dotenv import load_dotenv  # to read the api key form a .env file
from google import genai  # to use google generative ai via api key in python
from google.genai import types  # to be able to disable tool calls

from conditions import basline_prompt, dag_prompt, perfect_prompt

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
context_prompt = "You are a Nuxt 4 developer. Respond with a simple answer, using as few lines of code as possible. Only use the official, stable, public API. No comments and no imports, unless absolutely necessary."

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

# loading the test cases from src/tests/task*.md
def parse_case(path):
    with open(path) as f:
        content = f.read()
    _, frontmatter, doc = content.split('---\n', 2)
    meta = {}
    for line in frontmatter.strip().splitlines():
        key, _, value = line.partition(': ')
        meta[key.strip()] = value.strip()
    return {'id': int(meta['id']), 'task': meta['task'], 'link': meta['link'], 'doc': doc.strip()}

test_cases = [parse_case(f) for f in sorted(glob.glob('src/tests/task*.md'))]

selected_ids = parse_task_ids(sys.argv[1:]) if sys.argv[1:] else {c['id'] for c in test_cases}
selected_cases = [c for c in test_cases if c['id'] in selected_ids]

os.makedirs("src/results", exist_ok=True)

print(f"\n--- Starting 3-condition Experiment ({len(selected_cases)} tasks)... ---\n")

i, case, current_result_path = 0, None, None
try:
    for i, case in enumerate(selected_cases, 1):
        print(f"Processing Task {case['id']} ({i}/{len(selected_cases)})")

        current_result_path = f"src/results/task{case['id']:02d}.md"

        # run all 3 conditions in memory first — only write if all succeed
        print("-> (1/3) Running Baseline Prompt...")
        baseline_response, baseline_total_input, baseline_total_output = basline_prompt.run(client, model_id, no_tools_config, context_prompt, case['task'])

        print("-> (2/3) Running Simple DAG Prompt...")
        dag_response, keywords, grep_context, dage_total_input, dag_total_output = dag_prompt.run(client, model_id, no_tools_config, context_prompt, case['task'])

        print("-> (3/3) Running Perfect Information Prompt...")
        perfect_response, perfect_total_input, perfect_total_output = perfect_prompt.run(client, model_id, no_tools_config, context_prompt, case['task'], case['doc'])

        # all 3 succeeded — write result file atomically
        with open(current_result_path, "w") as f:
            f.write(f"# Task {case['id']}\n\n")
            f.write(f"**Context Prompt:** {context_prompt}\n\n")
            f.write(f"**Task Prompt:** {case['task']}\n\n")
            f.write(f"Link to Guide: {case['link']}\n\n")
            f.write("---\n\n")
            f.write("## 1. Baseline Result (task -> answer)\n")
            f.write("**LLM output:**\n\n")
            f.write(baseline_response.text + "\n\n")
            f.write("## 2. Simple DAG Result (task -> search -> answer)\n")
            f.write(f"> **Keywords used:** {', '.join(keywords)}\n\n")
            f.write(f"> **Found Context:** {grep_context[:500].replace(chr(10), ' ')}...\n\n")
            f.write("**LLM output:**\n\n")
            f.write(dag_response.text + "\n\n")
            f.write("## 3. Prefect Result (task & docs -> answer)\n")
            f.write("**LLM output:**\n\n")
            f.write(perfect_response.text + "\n\n")
            f.write("## 4. Token Usage Comparison\n")
            f.write("| Condition | Input Tokens | Output Tokens | Total |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            f.write(f"| Baseline | {baseline_total_input} | {baseline_total_output} | {baseline_total_input + baseline_total_output} |\n")
            f.write(f"| Simple DAG | {dage_total_input} | {dag_total_output} | {dage_total_input + dag_total_output} |\n")
            f.write(f"| Perfect Info | {perfect_total_input} | {perfect_total_output} | {perfect_total_input + perfect_total_output} |\n")

        current_result_path = None  # mark as fully saved

except (KeyboardInterrupt, Exception) as e:
    if not isinstance(e, KeyboardInterrupt):
        print(f"\n\nError on Task {case['id'] if case else '?'}: {e}")
    else:
        print(f"\n\nInterrupted{'  during Task ' + str(case['id']) if case else ' before any task ran'}.")
    if case:
        print(f"Resume with: python3 src/experiment.py {case['id']}-{selected_cases[-1]['id']}")
    sys.exit(1 if not isinstance(e, KeyboardInterrupt) else 0)

print(f"\nDone! Written {len(selected_cases)} file(s) to {os.path.abspath('src/results')}/")
