
## Preparing

Get the model file:

```
wget https://www.dropbox.com/s/kqimgk1x6gs3aq0/resnet_v1_07_0.973.h5

wget https://www.dropbox.com/s/1n4unj5daj4mwoq/catdog-model.tflite
```

Build the image:
```
docker build -t tf-lite-lambda .
```

## Running locally

To run locally

```
docker run --rm -p 8080:8080 tf-lite-lambda
```

Test it

```
wget https://github.com/manifoldailearning/awsml-certification-content/raw/main/1366.jpg
14. Testing the Deployment.ipynb
```


## Publishing

Create an ECR repo:

```
aws ecr create-repository --repository-name lambda-catdog
```

Login to ECR & Publish to ECR:

```

```

## Create a lambda function

* Go to Lambda, create a new function, select "container image"
* Put the image we just created there
* Go to basic settings and adjust timeout (60 sec) and memory (1GB)
* Test it with the following payload:

```json
{
    "url": "https://github.com/manifoldailearning/awsml-certification-content/raw/main/1366.jpg"
}
```
```
