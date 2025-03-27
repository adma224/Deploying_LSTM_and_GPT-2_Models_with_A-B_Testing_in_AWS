#!/usr/bin/env python3
import aws_cdk as cdk
from infra_stack import InfraStack
from gpt2_inference_stack import Gpt2InferenceStack

app = cdk.App()

infra = InfraStack(app, "InfraStack")

InferenceStack(
    app,
    "InferenceStack",
    artifact_bucket=infra.artifact_bucket,
    sagemaker_role=infra.sagemaker_role
)

app.synth()
