# iac-project > flask-hello Summary

The flask-hello branch launches a simple python/flask hello program on multiple platforms.


# Steps
1. Set up a Vagrant `testvm` and `prodvm` using `components/vagrant/README.md`
1. Prepare a Python hello service using `components/python/README.md`
1. Build and test a Docker image using `components/docker/README.md`
1. Test the Docker image on a local Kubernetes cluster using `components/kubernetes/local-kubeadm/README.md`
1. Build a K8s cluster to run the Docker image on AWS using `components/aws/README.md`
