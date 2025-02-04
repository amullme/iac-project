# iac-project/kubernetes/ Objective
Run the docker container on 5 pods on a local Kubernetes cluster and access it as a service.

# Steps
## Clone the repo
- Thanks to our friends at [Techiescamp](https://github.com/techiescamp), you can clone their repo and save time. First change to the dir below.
```
cd <repo root>/components/kubernetes/local-kubeadm
```
- Clone the repo
```
git clone https://github.com/techiescamp/vagrant-kubeadm-kubernetes
```
- Change dir to the new repo
```
cd vagrant-kubeadm-kubernetes
```
- Edit lines 29 to 31 of `settings.yaml` to map to map the `/vagrant` folder on each VM to the `local-kubeadm` folder on your host machine
```
shared_folders:
  - host_path: ../
    vm_path: /vagrant
```
- Start the K8s cluster on vagrant
```
vagrant up
```
- After all nodes come up, ssh to controlplane
```
vagrant ssh controlplane
```
- Make sure the 3 nodes in the cluster are ready
```
kubectl get nodes
```
- Apply the resources file [^1]
```
kubectl apply -f /vagrant/resources.yaml
```
- Check on the deployment
```
kubectl get pods
```
- Check on the service. Note the `EXTERNAL-IP`
```
kubectl get svc
```
- Open `10.0.0.10:32000` in a web browser on your host machine and refresh a few times. The container/hostname should change as the nginx service sends traffic to different containers.
- You can now move on to the next step `components/?/README.md`
### Footnotes
[^1] Feel free to edit the `resources.yaml` file to point to your own Dockerhub image 

