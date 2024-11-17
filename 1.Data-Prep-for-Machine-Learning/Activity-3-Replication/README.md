# Replicating S3 Buckets to Meet Recovery Point Objectives
## Preparation
### Set a unique suffix to use for the S3 bucket name:
```
RANDOM_ID=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)

```

### Create S3 Destination bucket:

`aws s3api create-bucket --bucket awsml-dest-$RANDOM_ID  `

### Create S3 Source bucket:

`aws s3api create-bucket --bucket awsml-src-$RANDOM_ID  `

### Enable Versioning for the Source & Destination S3 bucket:
```
aws s3api put-bucket-versioning \
--bucket awsml-dest-$RANDOM_ID \
--versioning-configuration Status=Enabled 
 


aws s3api put-bucket-versioning \
--bucket awsml-src-$RANDOM_ID \
--versioning-configuration Status=Enabled 
 
```
### Create IAM Role
```ROLE_ARN=$(aws iam create-role --role-name AWSMLS3Role \
--assume-role-policy-document file://s3-assumption-role-policy.json \
--output text --query Role.Arn)```

### Attach the Policy to the Role created
```aws iam put-role-policy \
    --role-name AWSMLS3Role \
    --policy-document file://s3-perms-policy.json \
    --policy-name S3ReplicationPolicy 
     ```


## Configure the replication policy
```aws s3api put-bucket-replication \
 --replication-configuration file://s3-replication.json \
 --bucket awsml-src-${RANDOM_ID} 
  

aws s3api get-bucket-replication \
 --bucket awsml-src-${RANDOM_ID} 
  ```

Upload the file to AWS S3 Bucket
`aws s3 cp NLP.png s3://awsml-src-$RANDOM_ID  `

Checking the Replication status
```aws s3api head-object --bucket awsml-src-${RANDOM_ID} --key NLP.png  ```

## Clean up 

`aws s3 rm s3://awsml-$RANDOM_ID/NLP.png  `

### Delete the S3 bucket:
### Delete the IAM Policy from the role:
```
aws iam delete-role-policy \
--role-name AWSMLS3Role --policy-name S3ReplicationPolicy  
```

### Delete the IAM Role:

`aws iam delete-role --role-name AWSMLS3Role  `
