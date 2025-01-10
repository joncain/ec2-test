#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack


app = cdk.App()
CdkStack(
    app,
     "CdkStack",
     env=cdk.Environment(account="000000000000", region="us-east-1")
)

app.synth()
