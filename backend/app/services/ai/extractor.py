from pathlib import Path

import fitz
import pandas as pd
from docx import Document


def extract_content(file_path: str) -> str:

    extension = Path(file_path).suffix.lower()

    try:

        # PDF

        if extension == ".pdf":

            document = fitz.open(file_path)

            text = ""

            for page in document:
                text += page.get_text()

            return text[:3000]

        # CSV

        if extension == ".csv":

            dataframe = pd.read_csv(file_path)

            return (
                "Columns: "
                + ", ".join(dataframe.columns)
            )

        # DOCX

        if extension == ".docx":

            document = Document(file_path)

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

            return text[:3000]

        # TXT

        if extension == ".txt":

            with open(
                file_path,
                "r",
                encoding="utf-8",
                errors="ignore",
            ) as file:

                return file.read()[:3000]

        return ""

    except Exception as error:

        print(
            f"AI extraction error: {error}"
        )

        return ""
