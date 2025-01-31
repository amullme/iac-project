# iac-project > flask-hello Summary

The flask-hello branch launches a simple python/flask hello program on multiple platforms.


# Steps
1. Set up a Vagrant `testvm` and `prodvm` using `components/vagrant/README.md`
1. Prepare a Python hello service using `components/python/README.md`
1. Build and test a Docker image using `components/docker/README.md`
1. *Test the Docker image on a local Kubernetes cluster by following the README.md in the `components/kubernetes` folder of this repo.
1. *Test the Docker image on an AWS and an Azure Kubernetes cluster using Terraform by following the README.md in the `components/terraform` folder of this repo.
