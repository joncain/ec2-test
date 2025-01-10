`docker-compose up -d`

`localstack config validate`

`./create-key.sh`

`cd cdk`

`source .venv/bin/activate`

`pip install -r requirements.txt`

`cdklocal bootstrap --profile local`

`cdklocal deploy --profile local`

# This produces an error:
```
CdkStack | 33/42 | 8:31:51 AM | CREATE_FAILED        | AWS::CloudFormation::Stack            | CdkStack 'PublicIpAddress'
CdkStack | 33/42 | 8:31:51 AM | CREATE_FAILED        | AWS::EC2::Instance                    | Instance (InstanceC1063A87) 'PublicIpAddress'
```

# From the localstack logs:
```
2025-01-10 08:31:51 localstack-main  | 2025-01-10T15:31:51.197 DEBUG --- [-functhread8] l.s.c.e.template_deployer  : Error applying changes for CloudFormation stack "CdkStack": 'PublicIpAddress' Traceback (most recent call last):
2025-01-10 08:31:51 localstack-main  |   File "/opt/code/localstack/.venv/lib/python3.11/site-packages/localstack/services/cloudformation/engine/template_deployer.py", line 1203, in _run
2025-01-10 08:31:51 localstack-main  |     self.do_apply_changes_in_loop(changes, stack)
2025-01-10 08:31:51 localstack-main  |   File "/opt/code/localstack/.venv/lib/python3.11/site-packages/localstack/services/cloudformation/engine/template_deployer.py", line 1539, in do_apply_changes_in_loop
2025-01-10 08:31:51 localstack-main  |     self.apply_change(change, stack=stack)
2025-01-10 08:31:51 localstack-main  |   File "/opt/code/localstack/.venv/lib/python3.11/site-packages/localstack/services/cloudformation/engine/template_deployer.py", line 1316, in apply_change
2025-01-10 08:31:51 localstack-main  |     progress_event = executor.deploy_loop(
2025-01-10 08:31:51 localstack-main  |                      ^^^^^^^^^^^^^^^^^^^^^
2025-01-10 08:31:51 localstack-main  |   File "/opt/code/localstack/.venv/lib/python3.11/site-packages/localstack/services/cloudformation/resource_provider.py", line 453, in deploy_loop
2025-01-10 08:31:51 localstack-main  |     event = self.execute_action(resource_provider, payload)
2025-01-10 08:31:51 localstack-main  |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-01-10 08:31:51 localstack-main  |   File "/opt/code/localstack/.venv/lib/python3.11/site-packages/localstack/services/cloudformation/resource_provider.py", line 519, in execute_action
2025-01-10 08:31:51 localstack-main  |     return resource_provider.create(request)
2025-01-10 08:31:51 localstack-main  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-01-10 08:31:51 localstack-main  |   File "/opt/code/localstack/.venv/lib/python3.11/site-packages/localstack/services/ec2/resource_providers/aws_ec2_instance.py", line 255, in create
2025-01-10 08:31:51 localstack-main  |     model["PublicIp"] = instance["PublicIpAddress"]
2025-01-10 08:31:51 localstack-main  |                         ~~~~~~~~^^^^^^^^^^^^^^^^^^^
2025-01-10 08:31:51 localstack-main  | KeyError: 'PublicIpAddress'
2025-01-10 08:31:51 localstack-main  | 
2025-01-10 08:31:51 localstack-main  | 2025-01-10T15:31:51.197  WARN --- [-functhread8] l.s.c.engine.entities      : CFn resource failed to deploy: InstanceC1063A87 ('PublicIpAddress')
```

# However, the ec2 instance is created and accessible.


`ssh -i ../key.pem root@127.0.0.1`

# From inside the ec2 container:

`curl google.com`
