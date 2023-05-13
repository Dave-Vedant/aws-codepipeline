from aws_cdk import (
    Stack,
    Stage,
    Environment,
    pipelines,
    aws_codepipeline as codepipeline
)
from constructs import Construct
from resource_stack.resource_stack import ResourceStack

class DeployStage(Stage):
    def __init__(self, scope: Construct, id:str, **kwargs):
        super().__init__(scope, id, **kwargs)
        ResourceStack(self, 'ResourceStack', stack_name="resource-stack-deploy")

class AwsCodepipelineStack(Stack):

    def __init__(self, scope:Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        commit_input = pipelines.CodePipelineSource.connection(
            repo_string = "https://github.com/vedantdave77/aws-codepipeline.git",
            branch = "main",
            connection_arn = "arn:aws:codestar-connections:us-east-1:398081196462:connection/4adcd83a-f671-416b-b60f-e87a0fbae1a2",
        )

        code_pipeline = codepipeline.Pipeline(
            self, "Pipeline",
            pipeline_name = "cdk-pipeline",
            cross_account_keys=False,
        )

        synth_step = pipelines.ShellStep(
            id = "Synth",
            install_commands=[
                'pip install -r requirements.txt'
            ],
            commands = [
                'npx cdk synth'
            ],
            input = commit_input,
        )

        pipeline = pipelines.CodePipeline(
            self, "CodePipeline",
            self_mutation = True,
            code_pipeline = code_pipeline,
            synth =synth_step,
        )

        deployment_wave = pipeline.add_wave("DeploymentWave")

        deployment_wave.add_stage(DeployStage(
            self, "DeployStage",
        ))

