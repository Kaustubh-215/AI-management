import uuid

import boto3

from app.core.config import settings


s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.aws_region,
)


def upload_file_to_s3(file):
    """
    Upload an image to Amazon S3 and return
    the generated filename and public URL.
    """

    extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{extension}"

    s3_client.upload_fileobj(
        Fileobj=file.file,
        Bucket=settings.aws_s3_bucket,
        Key=filename,
        ExtraArgs={
            "ContentType": file.content_type,
        },
    )

    location = s3_client.get_bucket_location(
        Bucket=settings.aws_s3_bucket
    )["LocationConstraint"]

    if location:
        file_url = (
            f"https://{settings.aws_s3_bucket}.s3."
            f"{location}.amazonaws.com/{filename}"
        )
    else:
        # us-east-1 buckets don't include the region
        file_url = (
            f"https://{settings.aws_s3_bucket}.s3.amazonaws.com/{filename}"
        )

    return filename, file_url


def generate_presigned_url(
    filename: str,
    expiration: int = 3600,
):
    """
    Generate a temporary download URL.
    """

    return s3_client.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": settings.aws_s3_bucket,
            "Key": filename,
        },
        ExpiresIn=expiration,
    )


def delete_file_from_s3(filename: str):
    """
    Delete a file from Amazon S3.
    """

    s3_client.delete_object(
        Bucket=settings.aws_s3_bucket,
        Key=filename,
    )
