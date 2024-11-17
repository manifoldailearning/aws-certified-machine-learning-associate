# Create S3 Bucket

```
RANDOM_ID=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```
`aws s3api create-bucket --bucket awsml-$RANDOM_ID`

# Create S3 Bucket for data
```
aws s3 mb s3://awsml-$RANDOM_ID/results/ 
aws s3 mb s3://awsml-$RANDOM_ID/data/ 
```

# Copy the files
`aws s3 cp titanic_data.csv s3://awsml-$RANDOM_ID/data/ `

# Validate the Crawlers
`aws glue get-crawler --name awsml-crawler`

# Display table
`aws glue get-table --database-name awsml --name data  `

# Cleanup
- Delete the Crawler:
    Select the crawler from the AWS Glue Console, select Actions, and choose Delete.
- Empty and delete the Bucket