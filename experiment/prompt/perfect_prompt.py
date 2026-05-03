def run(client, model_id, config, context_prompt, task, doc):
    """
    Condition 3: Perfect Information. The LLM is already provided with the correct documentation in the user prompt.
    """
    prompt = f"{context_prompt}\n\nYou must strictly follow this Nuxt 4 documentation to solve the task:\n{doc}\n\nTask: {task}"

    response = client.models.generate_content(
        model=model_id,
        contents=prompt,
        config=config
    )

    meta = response.usage_metadata
    total_input = meta.prompt_token_count
    total_output = meta.candidates_token_count

    return response, total_input, total_output