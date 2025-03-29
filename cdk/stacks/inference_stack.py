from aws_cdk import (
    Stack,
    aws_sagemaker as sagemaker,
)
from constructs import Construct



class InferenceStack(Stack):

    def __init__(self, scope: Construct, id: str, artifact_bucket, sagemaker_role, **kwargs):
        super().__init__(scope, id, **kwargs)

        model = sagemaker.CfnModel(
            self, "Gpt2Model",
            execution_role_arn=sagemaker_role.role_arn,
            primary_container={
                "image": "763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:2.1.1-cpu-py310-ubuntu20.04",
                "modelDataUrl": f"s3://{artifact_bucket.bucket_name}/gpt2-v1/model.tar.gz"
            }
        )

        endpoint_config = sagemaker.CfnEndpointConfig(
            self, "Gpt2EndpointConfig",
            production_variants=[{
                "modelName": model.attr_model_name,
                "variantName": "AllTraffic",
                "serverlessConfig": {
                    "memorySizeInMb": 2048,
                    "maxConcurrency": 2
                }
            }]
        )

        sagemaker.CfnEndpoint(
            self, "Gpt2Endpoint",
            endpoint_config_name=endpoint_config.attr_endpoint_config_name
        )
