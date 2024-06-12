import subprocess
import os
import datetime
import re

# Get the actual IP address of the specified network interface
def get_interface_ip(interface_name):
    result = subprocess.run(['ip', 'a', 'show', interface_name], capture_output=True, text=True)
    if result.returncode != 0:
        return None

    ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', result.stdout)
    if ip_match:
        return ip_match.group(1)
    return None

# Run an aggressive Nmap scan to detect hosts in the network
def detect_hosts(ip_address):
    ip_range = '.'.join(ip_address.split('.')[:-1]) + '.0/24'  # Assuming a /24 network
    result = subprocess.run(['nmap', '-sn', ip_range], capture_output=True, text=True)
    hosts = []
    for line in result.stdout.split('\n'):
        if 'Nmap scan report for' in line:
            host_ip = line.split()[-1]
            if host_ip != ip_address:  # Exclude the host address
                hosts.append(host_ip)
    return hosts

# Create a directory to store XML results
def create_result_directory():
    today = datetime.date.today().strftime("%Y-%m-%d")
    directory_name = f"xml_result_{today}"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name

# Scan each detected host for vulnerabilities
def scan_hosts_for_vulns(hosts, result_directory):
    for host in hosts:
        result_file = os.path.join(result_directory, f"result_nmap_{host}.xml")
        subprocess.run(['nmap', '-sV', '--script', 'vulners', '--script-args', 'mincvss=5.0', host, '-oX', result_file, '-A'])

def main():
    interface_name = "eth0"
    ip_address = get_interface_ip(interface_name)
    if ip_address is None:
        print(f"Could not find IP address for interface {interface_name}.")
        return

    print(f"Actual IP address of the host ({interface_name}): {ip_address}")
    hosts = detect_hosts(ip_address)
    if not hosts:
        print("No hosts detected.")
        return
    result_directory = create_result_directory()
    scan_hosts_for_vulns(hosts, result_directory)
    print(f"Scanning completed. Results are saved in {result_directory}")

if __name__ == "__main__":
    main()