def categorize_file(
    mime_type: str,
):

    if mime_type.startswith("image/"):

        return "image"

    if mime_type.startswith("video/"):

        return "video"

    if mime_type.startswith("audio/"):

        return "audio"

    if "pdf" in mime_type:

        return "document"

    if "csv" in mime_type:

        return "spreadsheet"

    if "word" in mime_type:

        return "document"

    if "zip" in mime_type:

        return "archive"

    return "other"
