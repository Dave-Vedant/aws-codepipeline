#!/usr/bin/env python3
import os

import aws_cdk as cdk

from codepipeline_stack.codepipeline import AwsCodepipelineStack


app = cdk.App()
AwsCodepipelineStack(app, "AwsCodepipelineStack",
                     stack_name='codepipeline-stack')
cdk.Tags.of(app).add(key='feature', value='aws_resource_stack')
cdk.Tags.of(app).add(key='contact', value='vedantdave77@gmail.com')
app.synth()
