from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    Duration,
    aws_lambda as lambda_,
    aws_s3 as s3
)

from constructs import Construct

class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        queue  = sqs.Queue(
            self, "AWSCDKCodePipelineappDemoQueue",
            visibility_timeout = Duration.seconds(300),
            queue_name = "demo_queue"
        )

        function = lambda_.Function(self,
                                    "CdkLambda",
                                    runtime= lambda_.Runtime.PYTHON_3_9,
                                    code = lambda_.Code.from_asset('./lambda_code_stack'),
                                    handler = "lambda_function.lambda_handler")
        
        bucket = s3.Bucket(self, "S3_bucket", versioned=True,
                           bucket_name="cdk-bucket",
                           block_public_access = s3.BlockPublicAccess.BLOCK_ALL)