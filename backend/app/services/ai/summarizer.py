def summarize_content(
    content: str,
    filename: str,
) -> str:

    if not content:

        return f"{filename} uploaded."

    words = content.split()

    preview = " ".join(words[:40])

    return preview
