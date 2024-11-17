# Query Files on S3 Using Amazon Athena

# Create S3 Bucket

```
RANDOM_ID=$(aws secretsmanager get-random-password \
--exclude-punctuation --exclude-uppercase \
--password-length 6 --require-each-included-type \
--output text \
--query RandomPassword)
```
### Create a S3 bucket for data:
`aws s3api create-bucket --bucket awsml-$RANDOM_ID  `

### Create S3 prefixes for results and data:
```
aws s3 mb s3://awsml-$RANDOM_ID/results/  
aws s3 mb s3://awsml-$RANDOM_ID/data/  
```

### Copy the titles.csv file to your S3 bucket
```
aws s3 cp Case.csv s3://awsml-$RANDOM_ID/data/  
```

## Commands
```
CREATE DATABASE awsml ;

CREATE EXTERNAL TABLE IF NOT EXISTS awsml.`awsmltable`(
    `case_id` integer,
    `province` string,
    `city` string,
    `group` string,
    `infection_case` integer,
    `confirmed` string,
    `latitude` float,
    `longitude` float)

ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format'= ',',
    'field.delim' = ','
) LOCATION 's3://awsml-80koqw/data/'
TBLPROPERTIES ('has_encrypted_data' = 'false');
```

```
SELECT * FROM awsmltable WHERE province='Seoul' LIMIT 100;

SELECT * FROM awsmltable LIMIT 100;
```

## Clean up 

```
Open the Query Editor and run the following two SQL statements:

DROP TABLE `awsmltable`;

DROP DATABASE `awsmldb`;

Delete the contents of the S3 bucket you created and delete the bucket. The S3 Console provides an easy way to empty the bucket with the “Empty” button.

```