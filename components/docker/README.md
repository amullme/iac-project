# iac-project/docker/ Objective
Build a Docker image and push it to Dockerhub. Then pull, run, and test it on `prodvm`.

# Pre-reqs
Sign up for you own Dockerhub account as you will not be able to push to my account

# Steps
## Build and push [^1]
- If not already ssh to `testvm`:
```
vagrant ssh testvm
```
- Change to `root` user.
```
sudo -i
```
- Change directory: [^2].
```
cd /vagrant/docker
```
- Copy the required Python files to the context of the `docker` folder:
```
mkdir resources
cp /vagrant/python/flask-hello/hello.py ./resources/hello.py
cp /vagrant/python/flask-hello/requirements.txt ./resources/requirements.txt
```
- Build the docker image. Use your own Dockerhub username.
```
docker build -t YOUR_USER_NAME/flask-hello .
```
- Check to see if the image exists:
```
docker image ls
```
- Login to Dockerhub from your terminal window:
```
docker login
```
- Push the image to your own Dockerhub:
```
docker push YOUR_USER_NAME/flask-hello
```
- Delete the `resources` dir:
```
rm -rf ./resources
```
## Pull, run, and test
- Exit `testvm` ssh:
```
exit
exit
```
- Login to `prodvm`:
```
vagrant ssh prodvm
```
- Change to `root` user.
```
sudo -i
```
- Pull/run the image with port forwarding from host. Feel free to pull it from my account or use your own.
```
docker run -p 5000:5000 amullme/flask-hello
```
- On your host machine open `http://10.0.0.11:5000` in a web browser to test
- If successful, clean up by exiting all ssh sessions and running the command below from `components/vagrant/`
```
vagrant destroy --force
```
- You can now move on to the next step `components/kubernetes/local-kubeadm/README.md`
### Footnotes
[^1]: You can skip building and pushing if you want to just pull and run it from my account.
[^2]: You must be in the same directory as the `Dockerfile`

