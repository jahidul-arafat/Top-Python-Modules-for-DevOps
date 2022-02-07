# Python DevOps Module: Paramiko
## 1. Installing Paramiko
```bash
pip3 install paramiko

# if you have already installed rich package then,
pip3 install --upgrade --force-reinstall rich
# else try
pip3 install rich 

# ---------------- EXCEPTION------------------------------------
# if you ever face trouble to load inspect package from rich, 
# in my case earlier installation of ciphey was conflicting with the rich version and thereby inspect module from rich was generating import error
# So I had to uninstall that ciphey module for now and reinstall the rich again
pip3 uninstall ciphey
pip3 install --upgrade --force-reinstall rich
#----------------------------------------------------------------

```

## 2. Lab environment Setup
Find the necessary configuration file [Here](lab_environment_setup) .
- [x] Vagrant file
- [x] inventory-test.yaml
- [x] playbook.yml

This will setup 6x VMs with necessary configurations of SSHD, Firewalld for each of the VMs.
- [x] servera.lab.example.com
- [x] serverb.lab.example.com
- [x] serverc.lab.example.com
- [x] serverd.lab.example.com
- [x] workstation.lab.example.com
- [x] bastion.lab.example.com

> Make sure you have `vagrant` installed in your local machine.

> This lab setting can also be used for your `ANSIBLE` exam preparation and practices at home. 


```bash
vagrant status
vagrant up
vagrant status

# to suspend the running VMs use,
vagrant suspend 

# to destroy the full lab setting
vagrant destroy
```

## My Labs
#### Lab-01: Using Python Module Paramiko try to get the hostname, uname of a single server
Get the [Lab-01 Source Code](lab-1.py)

#### Lab-02: Get the hostname, uname of all the servers at your organization or you can execute any other commands in those servers as you wish
Get the [Lab-02 Source Code](lab-2.py)

#### Lab-03: A Details one
Get the [Lab-03 Source Code](lab-3.py)
- [x] A. Get the hostname of the server 
- [x] B. list all files using SFTPClient of paramiko and identify file/folders separately 
- [x] C. Put a file from local machine to remote server using SFTP Client. Here in this case we will put a simple test.txt file to all the servers
- [x] D. Download a file from remote machine to local host using SFTP Client. Here in this case we are trying to investigate the commands executed at each of the remote server and we want to have a backup of these bash_history file into our local machine.

```
About Author
Jahidul Arafat
Cloud, Security and DevSecOps Architect
https://www.linkedin.com/in/jahidul-arafat-791a7490/
```
