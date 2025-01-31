# iac-project/vagrant/ Objective

Create 2 local VMs using Vagrant for building and testing a Docker container

# Pre-reqs
Vagrant and Virtualbox must be installed. Use a package manager based on your OS or here is a tutorial: https://medium.com/@AnnaJS15/getting-started-with-virtualbox-and-vagrant-8d98aa271d2a

# Steps
- Open the BASH of your choice and change to directory `components/vagrant` in this repo
- Use the following command to create and launch the 2 VMs defined in the `Vagrantfile` [^1] [^2] [^3]:
```
vagrant up
```
- You can now move on to the next step `components/python/README.md`

### Footnotes
[^1]: If you want to edit the `Vagrantfile` to better fit your needs, feel free
[^2]: For Windows, if you have issues with Vagrant coming up due to a network adapter error, try disabling and re-enabling all the Virtual Network Adapters.
[^3]: To stop the VMs use `vagrant halt` and to delete the VMs, use `vagrant destroy --force`
