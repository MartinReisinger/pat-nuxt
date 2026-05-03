import subprocess
import os


def run_search(keywords, search_dir="dag_content"):
    """
    Takes an array of keywords and runs a ripgrep (rg) command for each.
    Returns the search results as a string.
    """
    if not os.path.exists(search_dir):
        return f"Error: Directory '{search_dir}' not found."

    combined_results = []

    for kw in keywords:
        # Sanitize keyword to prevent shell injection issues with quotes
        clean_kw = kw.replace('"', '').replace("'", "")
        if not clean_kw:
            continue

        # ripgrep-command:
        # -max-count 4: stop after 4 matches
        # -A 50: get 50 lines of context AFTER the match
        # capture_output=True: grabs the text into Python
        command = f'rg -i "{clean_kw}" {search_dir} --max-count 4 -A 50 --no-filename --no-heading'

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # if ripgrep found something, add it to the context pool
            if result.stdout.strip():
                combined_results.append(f"--- Search hits for: '{clean_kw}' ---\n{result.stdout.strip()}")

        except Exception as e:
            print(f"Error running rg for '{clean_kw}': {e}")
            continue

    if not combined_results:
        return "No relevant documentation found in the local DAG."

    # join all results together
    final_context = "\n\n".join(combined_results)

    # hard limit on the context size
    # if rg grabs 5 keywords * 4 matches * 50 lines = max of 1000 lines + 100 lines buffer
    # so the prompt does not get too long for the llm
    return final_context[:1100]
