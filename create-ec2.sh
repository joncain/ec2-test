#! /bin/bash

awslocal ec2 create-key-pair \
    --key-name my-key \
    --query 'KeyMaterial' \
    --output text | tee key.pem

chmod 400 key.pem

awslocal ec2 authorize-security-group-ingress \
    --group-id default \
    --protocol tcp \
    --port 8000 \
    --cidr 0.0.0.0/0

SGID=`awslocal ec2 describe-security-groups | jq -r '.SecurityGroups.[0].GroupId'`
echo "SGID: ${SGID}"
awslocal ec2 run-instances \
    --image-id ami-df5de72bdb3b \
    --count 1 \
    --instance-type t3.nano \
    --key-name my-key \
    --security-group-ids $SGID
