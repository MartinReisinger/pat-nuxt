from src import dag_api # the ripgrep dag


def run(client, model_id, config, context_prompt, task):
    """
    Condition 2: Simple DAG.
    1. Prompts LLM for search keywords.
    2. Uses dag.py to search the local documentation using ripgrep.
    3. Prompts LLM again with the found context to solve the task.
    """

    # 1. extracting keywords form llm response
    keyword_prompt = (
        f"{context_prompt}\n\n"
        "You are a technical search expert. Your task is to extract search anchors "
        "to find relevant sections in the framework's documentation and upgrade guide.\n\n"
        "RULES:\n"
        "1. Search for the requested thing, general concept or the most likely API names relevant to this task.\n"
        "2. Each phrase shall be at only 1 word.\n"
        "3. Provide up to 5 keywords, separated ONLY by commas.\n"
        "4. Include synonyms or alternative technical phrasings to ensure greater coverage in a literal string search.\n\n"
        f"Task: {task}"
    )

    keyword_res = client.models.generate_content(
        model=model_id,
        contents=keyword_prompt,
        config=config
    )

    meta1 = keyword_res.usage_metadata

    # converting the response to a array
    raw_keywords = keyword_res.text.replace('\n', '').strip()
    keywords = [kw.strip() for kw in raw_keywords.split(',') if kw.strip()]

    # limit to 5 searches
    keywords = keywords[:5]

    # 2. search via the dag_api
    grep_results = dag_api.run_search(keywords)

    # 3. reprompt with the search results as context
    final_prompt = (
        f"{context_prompt}\n\n"
        "Use the following documentation context to solve the task. "
        "If the documentation does not contain the exact answer, rely on your best knowledge.\n\n"
        f"--- DOCUMENTATION CONTEXT ---\n{grep_results}\n-----------------------------\n\n"
        f"Task: {task}"
    )

    final_res = client.models.generate_content(
        model=model_id,
        contents=final_prompt,
        config=config
    )

    meta2 = final_res.usage_metadata

    total_input = meta1.prompt_token_count + meta2.prompt_token_count
    total_output = meta1.candidates_token_count + meta2.candidates_token_count

    # returning all 3 results, to visualize it in the results.md
    return final_res, keywords, grep_results, total_input, total_output
