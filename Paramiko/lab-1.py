from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()

client = SSHClient()

#Load Host Keys
client.load_host_keys("/home/jarotball/.ssh/known_hosts")
client.load_system_host_keys()

#Known host policy
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect("172.25.250.10", username="vagrant", password="vagrant")

#Run a command
stdin,stdout,stderr=client.exec_command('hostname')
print(type(stdin))
print(type(stdout))
print(type(stderr))

# Print output of command. Will wait for command to finish
print(f"STDOUT: {stdout.read().decode('utf-8')}")   #human readable format
print(f"STDERR: {stderr.read().decode('utf-8')}")   #human readable format

# Get return code from command (0 is default for success)
print(f"Return Code: {stdout.channel.recv_exit_status()}")

# Because they are file objects, they need to be closed
stdin.close()
stdout.close()
stderr.close()

# Close the client itself
client.close()
