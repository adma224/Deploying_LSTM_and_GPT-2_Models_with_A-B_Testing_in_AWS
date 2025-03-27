import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk.inference_stack import Gpt2InferenceStack
from cdk.infra_stack import InfraStack


# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_ml_pipeline/cdk_ml_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkMlPipelineStack(app, "cdk-ml-pipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
