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
- cd to the new repo
```
cd vagrant-kubeadm-kubernetes
```

## Start the cluster
- Edit lines 29 to 31 of `settings.yaml` to map to map the `/vagrant` folder on each VM to the `local-kubeadm` folder on your host machine
```
shared_folders:
  - host_path: ../../../
    vm_path: /components
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
kubectl apply -f /components/kubernetes/local-kubeadm/resources.yaml
```

## Confirm the cluster
- Check on the deployment
```
kubectl get pods
```
- Check on the service
```
kubectl get svc
```
- When on or more pods are ready, open [http://10.0.0.10:32000](http://10.0.0.10:32000) in a web browser on your host machine and refresh a few times. The `container or host` should change as the nginx service sends traffic to different containers.
- Exit ssh sessions and cd back to `local-kubeadm`
```
exit
cd ..
```

## Try to break the cluster
- Add load by running `curlbomb.py` 3 times in 3 different terminal windows
```
python curlbomb.py 10.0.0.10
python curlbomb.py 10.0.0.11
python curlbomb.py 10.0.0.12
```
- Add as many `curlbomb.py` terminal windows and you want and see if you can break the cluster, lol
- If break it see if you can figure out how to fix it
- Ctrl+c in each terminal window to stop all the `curlbomb.py` terminals
- You can now move on to the next step `components/aws/README.md`
### Footnotes
[^1]: Feel free to edit the `resources.yaml` file to point to your own Dockerhub image 

