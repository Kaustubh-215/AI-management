from PIL import Image


def extract_metadata(file):
    image = Image.open(file.file)

    metadata = {
        "width": image.width,
        "height": image.height,
        "format": image.format,
    }

    file.file.seek(0)

    return metadata
