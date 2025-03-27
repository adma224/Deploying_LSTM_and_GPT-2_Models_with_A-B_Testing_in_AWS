#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_stack import CdkStack

app = cdk.App()
CdkStack(app, "cdk_ml_pipeline_stack.py")
app.synth()

