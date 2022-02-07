from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect

pretty.install()

host_list = [
    "172.25.250.10",
    "172.25.250.11",
    "172.25.250.12",
    "172.25.250.13",
    "172.25.250.9",
    "172.25.250.254"
]

print("Listing the hostname of all servers")
for host in host_list:
    client = SSHClient()
    client.load_host_keys("/home/jarotball/.ssh/known_hosts")
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(host, username="vagrant", password="vagrant")

    # Run a command
    stdin, stdout, stderr = client.exec_command('hostname')
    #stdin, stdout, stderr = client.exec_command('uname -a')
    #stdin, stdout, stderr = client.exec_command('ls -la')

    if stdout.channel.recv_exit_status() == 0:  # 0--> Success
        print(f"{stdout.read().decode('utf-8')}")
    else:
        print(f"STDERR: {stderr.read().decode('utf-8')}")

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    # Close the client itself
    client.close()
