import boto3
import json

# Load endpoint name from SSM
ssm = boto3.client("ssm")
param = ssm.get_parameter(Name="/ml-pipeline/sagemaker/endpoint-name", WithDecryption=False)
endpoint_name = param["Parameter"]["Value"]

# Prompt input
payload = {"inputs": "Once upon a time,"}

# Invoke endpoint
sm = boto3.client("sagemaker-runtime")
response = sm.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="application/json",
    Body=json.dumps(payload)
)

# Read and print result
result = json.loads(response["Body"].read())
print("📜 Generated text:", result[0]["generated_text"])

