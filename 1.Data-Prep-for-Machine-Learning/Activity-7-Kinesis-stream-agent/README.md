# Install Web app in EC2

```
cd  /var/www/html

sudo wget https://www.dropbox.com/s/nw5bqgym23n93lf/css-template.zip

sudo unzip css-template.zip

ls

http://<ip-address>/html

sudo su
cd /var/log/httpd/
tail -10 access_log

groupadd httpd
usermod -a -G httpd ec2-user
exit

groups
sudo chown -R root:httpd /var/log/httpd
sudo chmod 2775 /var/log/httpd
find /var/log/httpd -type d -exec sudo chmod 2775 {} +
```

# Configure Kinesis Agent
```
sudo yum install –y https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-agent-latest.amzn2.noarch.rpm

sudo nano /etc/aws-kinesis/agent.json
```

## Remove all the content and add the below content with Access Key and Access id

```

{
  "cloudwatch.emitMetrics": true,
  "kinesis.endpoint": "",
  "firehose.endpoint": "",
  "awsAccessKeyId": "xxxxxxxx",
  "awsSecretAccessKey": "xxxxxxxxxxxx",
  "flows": [
    {
      "filePattern": "/var/log/httpd/access_log",
      "kinesisStream": "aws-ml-stream",
      "partitionKeyOption": "RANDOM"
    }
  ]
}

```
`cat /etc/aws-kinesis/agent.json`

## Stop and Start agent
```
sudo service aws-kinesis-agent stop
sudo service aws-kinesis-agent start
cd /var/log/aws-kinesis-agent/
ls -ltr
head -10 aws-kinesis-agent.log
```


