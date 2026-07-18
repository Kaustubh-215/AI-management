from app.services.ai.categorizer import categorize_file
from app.services.ai.extractor import extract_content
from app.services.ai.summarizer import summarize_content
from app.services.ai.tags import generate_tags


def analyze_file(
    file_path: str,
    filename: str,
    mime_type: str,
):

    category = categorize_file(
        mime_type
    )

    content = extract_content(
        file_path
    )

    summary = summarize_content(
        content,
        filename,
    )

    tags = generate_tags(
        filename,
        content,
    )

    return {
        "file_category": category,
        "ai_status": "completed",
        "ai_summary": summary,
        "ai_tags": ",".join(tags),
    }
