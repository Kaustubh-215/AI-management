from pathlib import Path


def analyze_file(
    filename: str,
    mime_type: str,
) -> dict:

    extension = Path(filename).suffix.lower()

    category = mime_type.split("/")[0]

    tags = []

    summary = ""

    # Images

    if category == "image":

        summary = "Image uploaded by user"

        tags.append("image")

        if extension == ".png":
            tags.append("png")

        if extension in [".jpg", ".jpeg"]:
            tags.append("jpeg")

        if extension == ".webp":
            tags.append("webp")

    # Videos

    elif category == "video":

        summary = "Video uploaded by user"

        tags.extend(
            [
                "video",
                "media",
            ]
        )

    # Audio

    elif category == "audio":

        summary = "Audio file uploaded by user"

        tags.extend(
            [
                "audio",
                "music",
            ]
        )

    # Documents

    elif mime_type in [

        "application/pdf",

        "application/msword",

        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",

        "application/vnd.ms-excel",

        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

        "text/plain",

    ]:

        category = "document"

        summary = "Document uploaded by user"

        tags.extend(
            [
                "document",
            ]
        )

        if extension == ".pdf":
            tags.append("pdf")

        if extension == ".docx":
            tags.append("word")

        if extension == ".xlsx":
            tags.append("excel")

    # Archives

    elif mime_type == "application/zip":

        category = "archive"

        summary = "Compressed archive uploaded by user"

        tags.extend(
            [
                "zip",
                "archive",
            ]
        )

    else:

        summary = "Unknown file"

        tags.append(
            "unknown"
        )

    return {
        "file_category": category,
        "ai_status": "completed",
        "ai_summary": summary,
        "ai_tags": ",".join(tags),
    }
