# Push the files to S3 Bucket
```
RANDOM_ID=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)

```

### Create S3 bucket:

`aws s3api create-bucket --bucket awsml-$RANDOM_ID `

Upload the file to AWS S3 Bucket
`aws s3 cp hepatitis.xlsx s3://awsml-$RANDOM_ID `