def run(client, model_id, config, context_prompt, task):
    """
    Condition 1: Baseline. The LLM relies only on its internal training data.
    """
    prompt = f"{context_prompt}\n\nTask: {task}"
    response = client.models.generate_content(
        model=model_id,
        contents=prompt,
        config=config
    )

    meta = response.usage_metadata
    total_input = meta.prompt_token_count
    total_output = meta.candidates_token_count

    return response, total_input, total_output