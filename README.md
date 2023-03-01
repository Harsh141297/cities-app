# Implementation of the application in Python using Flask and Elasticsearch as the database
Requisite : Docker, kubernetes cluster, helm chart, python

# Here are the general steps to create an Elasticsearch domain in AWS:
1] Log in to the AWS Management Console and navigate to the OpenSearch Service.

2] Click the "Create domain" button.

3] Choose a domain name and specify the cluster configuration, such as the number of nodes, instance type, and storage type.

4] Choose a VPC and subnets for the Elasticsearch domain. You can create a new VPC or choose an existing one.

5] Choose the access policy for the Elasticsearch domain. You can use a predefined policy or create a custom one.

6] Review the configuration and click the "Create" button to create the Elasticsearch domain.

7] Once the Elasticsearch domain is created, you can access it using the endpoint specified in the AWS Management Console.

# Use the Elasticsearch endpoint and replace it in python script.

# Build docker image and use it in helm chart 
1] Build Docker Image with the help of Dockerfile:
```
docker build -t cities-app .
```
2] Image will get created in Local. You can check it with command
```
docker images cities-app
```
2] Image is created then you can push it to any of Artifactory - DockerHub, Nexus, ECR

3] Update image repository and tag in cities-app/values.yaml. Where is already set to 5000

4] Deploy helm chart
```
helm install cities-app cities-app/
```
5] Run command to view the pods
```
kubectl get pods
```
6] Run command to view the service
```
kubectl get service
```

# Test the application and its endpoints to make sure it works as expected.
i) Health endpoint:
```
curl http://<service-url>:<port>/
```
ii) Insert/update city endpoint:
```
curl -X POST http://<service-url>:<port>/city -d '{"city": "India", "population": 8336697}'
```
iii) Retrieve city population endpoint:
```
curl http://<service-url>:<port>/city/India
```

Note: Replace service-url and port with the actual values for your Kubernetes cluster.

