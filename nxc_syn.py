import subprocess

# User credentials
username = 'bob'
password = '!P@$$W0rD!123'
target_ip = '10.10.51.100'

# Define the commands with placeholders for username and password
commands = [
    f"nxc smb {target_ip} -u '{username}' -p '{password}' --shares",
    f"nxc rdp {target_ip} -u '{username}' -p '{password}'",
    f"nxc winrm {target_ip} -u '{username}' -p '{password}'"
]

# Execute each command and check for open ports
for command in commands:
    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}\n{e.stderr}")

# If you want to save the outputs to a file, uncomment the following lines
# with open('output.log', 'w') as f:
#     for command in commands:
#         try:
#             result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
#             f.write(f"Output of {command}:\n{result.stdout}\n")
#         except subprocess.CalledProcessError as e:
#             f.write(f"Command failed: {command}\nError: {e.stderr}\n")
