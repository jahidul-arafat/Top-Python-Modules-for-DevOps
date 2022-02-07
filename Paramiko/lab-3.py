# My Check List
# 1. Get the hostname of the server
# 2. list all files using SFTPClient of paramiko and identify file/folders separately
# 3. Put a file from local machine to remote server using SFTP Client
# 4. Download a file from remote machine to local host using SFTP Client

from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
from models import color

pretty.install()

#--------- CUSTOM VARIABLES ---------------------------------
host_list = [
    "172.25.250.10",
    "172.25.250.11",
    "172.25.250.12",
    "172.25.250.13",
    "172.25.250.9",
    "172.25.250.254"
]

local_file_path_upload = "/home/jarotball/study/MyDevSecOps_Community/Top-Python-Modules-for-DevOps/Paramiko/files_to_be_uploaded_in_remote_machine"
local_file_path_download = "/home/jarotball/study/MyDevSecOps_Community/Top-Python-Modules-for-DevOps/Paramiko/files_downloaded_from_remote_machine"
remote_file_path = "/home/vagrant"
#-----------------------------------------------------------

print(color.BOLD+"Operation Begins| A Demo by Jahidul Arafat"+color.END)
for host in host_list:
    print(color.BOLD+ f"Remote Host: {host}\n-------------------------------"+color.END)
    client = SSHClient()
    client.load_host_keys("/home/jarotball/.ssh/known_hosts")
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(host, username="vagrant", password="vagrant")

    # Get the hostname of the server
    stdin, stdout, stderr = client.exec_command('hostname')


    if stdout.channel.recv_exit_status() == 0:  # 0--> Success
        hostname = stdout.read().decode('utf-8')
        print(f"=>HOSTNAME: {hostname}")
    else:
        print(f"STDERR: {stderr.read().decode('utf-8')}")

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()


    # SFTP
    sftp_client = client.open_sftp()
    file_list = []
    dir_list = []
    # list all files using SFTPClient of paramiko and identify file/folders separately
    print(color.BOLD+"Listing all files using SFTPClient of paramiko and identify file/folders separately"+color.END)
    for file in sftp_client.listdir():
        lstatout=str(sftp_client.lstat(file)).split()[0]
        if 'd' not in lstatout:
            file_list.append(file)
        else:
            dir_list.append(file)
    print(f"=>Files  : {file_list}")
    print(f"=>Folders: {dir_list}\n")

    # Put a file from local machine to remote server using SFTPClient
    print(f"=>Putting a file from local machine to {hostname}/{host} using SFTPClient")
    sftp_client.put(f"{local_file_path_upload}/test.txt",f"{remote_file_path}/test.txt")

    # Download a file from remote machine to local host using SFTPClient
    print(f"=>Downloading a file from {hostname}/{host} to local host using SFTPClient")
    sftp_client.get(f"{remote_file_path}/.bash_history",f"{local_file_path_download}/{hostname}_bash_history")
    print()

    # Close the SFTP connection
    print("...(X) Closing the SFTP Connection")
    sftp_client.close()

    # Close the client itself
    print("...(X) Closing the Client itself\n")
    client.close()
