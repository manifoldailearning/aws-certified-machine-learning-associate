# Using S3 Intelligent Tiering


Help Document:  https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html

```
RANDOM_ID=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)

```

### Create S3 bucket:

`aws s3api create-bucket --bucket awsml-$RANDOM_ID `

Apply Intelligent Tiering Config:
```aws s3api put-bucket-intelligent-tiering-configuration \
    --bucket awsml-$RANDOM_ID \
    --id awsml \
    --intelligent-tiering-configuration "$(cat tiering.json)" 
```

Validation:
```aws s3api get-bucket-intelligent-tiering-configuration \
    --bucket awsml-$RANDOM_ID \
    --id awsml ``

Upload the file to AWS S3 Bucket
`aws s3 cp NLP.png s3://awsml-$RANDOM_ID `

Display Storage class
`aws s3api list-objects-v2 --bucket awsml-$RANDOM_ID `

## Clean up 
### Delete the file you copied to your S3 bucket:

`aws s3 rm s3://awsml-$RANDOM_ID/NLP.png `

### Delete the S3 bucket:

`aws s3api delete-bucket --bucket awsml-$RANDOM_ID`

### Unset the environment variable that you created manually:

`unset RANDOM_STRING`
