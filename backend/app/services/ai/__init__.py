from pathlib import Path


def analyze_file(
    filename: str,
    mime_type: str,
) -> dict:

    extension = Path(filename).suffix.lower().replace(".", "")

    summary = ""

    tags = [extension]

    if mime_type.startswith("image/"):

        summary = f"{extension.upper()} image uploaded"

        tags.append("image")

    elif mime_type.startswith("video/"):

        summary = f"{extension.upper()} video uploaded"

        tags.extend(
            [
                "video",
                "media",
            ]
        )

    elif mime_type.startswith("audio/"):

        summary = f"{extension.upper()} audio uploaded"

        tags.extend(
            [
                "audio",
                "music",
            ]
        )

    elif mime_type in [

        "application/pdf",

        "application/msword",

        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",

        "application/vnd.ms-excel",

        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

        "text/plain",

        "text/csv",

        "text/tab-separated-values",

    ]:

        summary = f"{extension.upper()} document uploaded"

        tags.append("document")

    elif mime_type in [

        "application/zip",

        "application/x-zip-compressed",

        "application/x-rar-compressed",

    ]:

        summary = f"{extension.upper()} archive uploaded"

        tags.append("archive")

    else:

        summary = "Unknown file uploaded"

        tags.append("unknown")

    return {
        "file_category": extension,
        "ai_status": "completed",
        "ai_summary": summary,
        "ai_tags": ",".join(tags),
    }
