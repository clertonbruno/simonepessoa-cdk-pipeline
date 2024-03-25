import aws_cdk as cdk
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as lambda_
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

from helpers.env_config import EnvConfig


class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        account_id = self.account

        env_configs = EnvConfig(account_id).env_configs

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="MyPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub(
                    "clertonbruno/simonepessoa-cdk-pipeline", env_configs.get("branch")
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )

        # Define Lambda
        helloworld_lambda = lambda_.Function(
            self,
            "HelloWorldFunction",
            runtime=lambda_.Runtime.PYTHON_3_11,
            code=lambda_.Code.from_asset("helpers/lambda"),
            handler="hello_world.lambda_handler",
            timeout=cdk.Duration.seconds(60),
        )

        # API Gateway REST API with Lambda integration
        api = apigw.LambdaRestApi(
            self,
            "HelloWorldAPI",
            handler=helloworld_lambda,
            proxy=True,
        )
