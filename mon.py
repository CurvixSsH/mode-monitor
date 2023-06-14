import subprocess

def change_network_mode():
    network_name = input("Please enter the name of the network: ")

    result = subprocess.run(["sudo", "ip", "link", "set", network_name, "down"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return

    new_name = network_name + "mon"
    result = subprocess.run(["sudo", "ip", "link", "set", network_name, "name", new_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return

    result = subprocess.run(["sudo", "ip", "link", "set", new_name, "up"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return

    result = subprocess.run(["sudo", "iwconfig", new_name, "mode", "monitor"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return

    subprocess.run(["iwconfig"])

change_network_mode()
