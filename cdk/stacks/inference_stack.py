from aws_cdk import (
    Stack,
    aws_sagemaker as sagemaker,
    aws_ssm as ssm
)
from constructs import Construct

class InferenceStack(Stack):

    def __init__(self, scope: Construct, id: str, artifact_bucket, sagemaker_role, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Load latest model path from SSM
        model_path_param = ssm.StringParameter.from_string_parameter_name(
            self, "LatestModelPathParam",
            string_parameter_name="/ml-pipeline/s3/latest-model-path"
        )
        # This creates a SageMaker model from your uploaded artifact.
        model = sagemaker.CfnModel(
            self, "Gpt2Model",
            execution_role_arn=sagemaker_role.role_arn,
            primary_container={
                "image": "763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:2.1.1-cpu-py310-ubuntu20.04",
                "modelDataUrl": f"s3://{artifact_bucket.bucket_name}/{model_path_param.string_value}"
            }
        )
        # This defines the configuration for the endpoint — including memory and concurrency.
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
        # This actually deploys the endpoint, using the model + config above.
        sagemaker.CfnEndpoint(
            self, "Gpt2Endpoint",
            endpoint_config_name=endpoint_config.attr_endpoint_config_name
        )

