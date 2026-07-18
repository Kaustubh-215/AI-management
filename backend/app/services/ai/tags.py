def generate_tags(
    filename: str,
    content: str,
):

    tags = []

    filename = filename.lower()

    if ".csv" in filename:

        tags.extend(
            [
                "csv",
                "spreadsheet",
            ]
        )

    if ".pdf" in filename:

        tags.extend(
            [
                "pdf",
                "document",
            ]
        )

    if ".docx" in filename:

        tags.extend(
            [
                "word",
                "document",
            ]
        )

    content = content.lower()

    keywords = [
        "terraform",
        "aws",
        "docker",
        "kubernetes",
        "mysql",
        "nginx",
        "linux",
    ]

    for keyword in keywords:

        if keyword in content:

            tags.append(keyword)

    return list(set(tags))
