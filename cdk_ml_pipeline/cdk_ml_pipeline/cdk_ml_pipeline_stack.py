from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 Bucket for model artifacts
        self.model_artifact_bucket = s3.Bucket(
            self, "ModelArtifactsBucket",
            versioned=True,
            removal_policy=s3.RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # IAM Role for SageMaker Inference
        self.sagemaker_execution_role = iam.Role(
            self, "SageMakerExecutionRole",
            assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess"),
            ]
        )
