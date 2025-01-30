# iac-project/vagrant/ Objective

Create 2 local VMs using Vagrant for building and testing a Docker container

# Pre-reqs
Vagrant and Virtualbox must be installed

# Steps
1. Open the BASH of your choice and change to the directory in which this README.md file is located
1. Use the following command to launch the 2 VMs defined in the `Vagrantfile` [^1] [^2]:
```
vagrant up
```

[^1]: If you want to edit the `Vagrantfile` to better fit your needs, feel free
[^2]: For Windows, if you have issues with Vagrant coming up due to a network adapter error, try disabling and re-enabling all the Virtual Network Adapters.
