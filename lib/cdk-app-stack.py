from aws_cdk import core
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_event_sources as lambda_event_sources
from aws_cdk import aws_dynamodb as dynamodb

image_bucket = "cdk-rekn-imagebucket"

class CdkAppStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ========================================
        # Bucket for storing images
        # ========================================
        bucket = s3.Bucket(self, image_bucket, removal_policy=core.RemovalPolicy.DESTROY)
        core.CfnOutput(self, "Bucket", value=bucket.bucket_name)

        # ========================================
        # Role for AWS Lambda
        # ========================================
        role = iam.Role(self, "cdk-rekn-lambdarole", assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "rekognition:*",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                ],
                resources=["*"],
            )
        )

        # ========================================
        # DynamoDB table for storing image labels
        # ========================================
        table = dynamodb.Table(
            self,
            "cdk-rekn-imagetable",
            partition_key=dynamodb.Attribute(name="Image", type=dynamodb.AttributeType.STRING),
            removal_policy=core.RemovalPolicy.DESTROY,
        )
        core.CfnOutput(self, "Table", value=table.table_name)

        # ========================================
        # AWS Lambda function
        # ========================================
        lambda_fn = _lambda.Function(
            self,
            "cdk-rekn-function",
            code=_lambda.AssetCode.from_asset("lambda"),
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            role=role,
            environment={
                "TABLE": table.table_name,
                "BUCKET": bucket.bucket_name,
            },
        )
        lambda_fn.add_event_source(lambda_event_sources.S3EventSource(bucket, events=[s3.EventType.OBJECT_CREATED]))

        bucket.grant_read_write(lambda_fn)
        table.grant_full_access(lambda_fn)

app = core.App()
CdkAppStack(app, "CdkAppStack")
app.synth()