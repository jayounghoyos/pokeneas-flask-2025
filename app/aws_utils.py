import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Crear cliente S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
    region_name=os.getenv('AWS_REGION')
)

S3_BUCKET = os.getenv('S3_BUCKET')

def get_image_url(image_name):
    """Construye la URL pública de una imagen en S3"""
    return f"https://{S3_BUCKET}.s3.amazonaws.com/{image_name}"