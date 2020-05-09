# csc496MainProject

## Team Members
Sarah Fondots
Wyatt Greenman

## Project Description
Per the slides presented in class on Installation and Deployment
Install and deploy a multi-node computing service on CloudLab’s OpenStack Cloud or on Docker’s Kubernetes

### Project Primary Task: 
Select a computing service consisting of at least two service nodes (i.e., a web server with a backend SQL server OR a Single-Sign-On LDAP server that supports a networked file system server …) and deploy the corresponding VMs/containers inside CloudLab’s Openstack infrastructure or Kubernetes infrastructure. 
### Project Subtasks:
Able to setup VM nodes (possibly on local computers) that work together to provide a unified computing service to users. 
Able to move these VM nodes into the Cloud, setup proper network environment, and link them together. 
Able to setup at least 2-3 security groups/Docker subnet (DO NOT use the default security groups (Openstack) or Docker default network)

### Deployment
If a user wants to launch the webserver used in this project they need to follow these steps. To start with, the user should find a service that they want to use to launch the server. If the service does not already have docker installed, then the user should use the install_docker.sh file from the github repository to install docker. After this the user should ensure they know the ip address for their instance on their service of choice and then run the command docker-compose up to launch the image stored in the docker-compose.yml from the github repository. This docker-compose.yml launches an image of Jupyter/Spark and provides the user with a link to follow to access the Jupyter notebook. The user will want to use the last link and replace the local ip address (127.0.0.1) with the ip address for the user’s instance on the service they are using. This will allow the user to load up the files for the word cloud generator into a fresh instance of Jupyter notebook or it can be used for anything else you might want to use Spark and Jupyter for.
