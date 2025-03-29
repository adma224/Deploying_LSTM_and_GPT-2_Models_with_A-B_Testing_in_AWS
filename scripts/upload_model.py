import os
import tarfile
import boto3
import datetime

# Load bucket name from SSM
ssm = boto3.client("ssm")
param = ssm.get_parameter(Name="/ml-pipeline/s3/model-artifact-bucket", WithDecryption=False)
BUCKET_NAME = param["Parameter"]["Value"]

# Define paths
MODEL_DIR = "models/gpt2-v1/gpt2_finetuned"
VERSION_TAG = datetime.datetime.now().strftime("v%Y%m%d-%H%M%S")
S3_KEY = f"gpt2-v1/{VERSION_TAG}/model.tar.gz"
TARBALL = "/tmp/model.tar.gz"

# Tar model directory
with tarfile.open(TARBALL, "w:gz") as tar:
    tar.add(MODEL_DIR, arcname=".")

print(f"✅ Created tarball: {TARBALL}")

# Upload to S3
s3 = boto3.client("s3")
s3.upload_file(TARBALL, BUCKET_NAME, S3_KEY)
print(f"🚀 Uploaded to s3://{BUCKET_NAME}/{S3_KEY}")

# Save latest model path to SSM
ssm.put_parameter(
    Name="/ml-pipeline/s3/latest-model-path",
    Value=S3_KEY,
    Type="String",
    Overwrite=True
)
print(f"🧠 Updated latest model path in SSM: {S3_KEY}")

