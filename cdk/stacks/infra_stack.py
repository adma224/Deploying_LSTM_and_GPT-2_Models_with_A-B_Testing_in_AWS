from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_iam as iam,
    RemovalPolicy,
)
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Named S3 bucket for model artifacts
        self.artifact_bucket = s3.Bucket(
            self, "ModelArtifactBucket",
            bucket_name="gpt2-artifacts-bucket",  # must be globally unique
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # IAM Role for SageMaker inference
        self.sagemaker_role = iam.Role(
            self, "SageMakerExecutionRole",
            assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess"),
            ]
        )
