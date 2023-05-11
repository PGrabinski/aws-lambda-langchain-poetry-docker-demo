from aws_cdk import (
    asw_lambda as _lambda,
    aws_apigatewayv2 as apigw,
    aws_apigatewatv2_integrations as apigw_integrations,
    core
)

class MyStack(core.Stack):
    def __init__(self,
                 scope: core.Construct,
                 id: str,
                 **kwargs
                 ) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_function = _lambda.Function(
            self,
            "AWS-Langchain-Poetry-Docker-Demo",
            runtime=_lambda.Runtime.Python_3_8,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("src")
        )

        api = apigw.HttpApi(
            self,
            "AWS-Langchain-Poetry-Docker-Demo-API",
            default_integration=apigw_integrations.LambdaProxyIntegration(
                handler=lambda_function
            )
        )

        core.CfnOutput(
            self,
            "ApiUrl",
            value=api.url
        )