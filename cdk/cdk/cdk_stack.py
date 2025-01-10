from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC with outbound internet access
        vpc = ec2.Vpc(self, "Vpc", max_azs=3, vpc_name="my-vpc")

        # Create an ec2 instance
        ec2.Instance(
            self,
             "Instance",
            vpc=vpc,
            instance_type=ec2.InstanceType("t3.nano"),
            instance_name="my-instance",
            machine_image=ec2.MachineImage.lookup(
                name="amazonlinux-2023"
            ),
            key_name="my-key"
        )
