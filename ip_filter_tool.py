# Python Security Tool: Authorized Access via IP Allow-List
# Author: [Angelo Ayton]
# Description:
# This script enforces access control by removing unauthorized IPs from a sensitive allow list.

# Assign 'import_file' to the name of the file
import_file = "allow_list.txt"

# Assign 'remove_list' to a list of IP addresses that are no longer allowed to access restricted information
remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# Open the allow list file in read-only mode and read contents
with open(import_file, "r") as file:
    ip_addresses = file.read()
    print(ip_addresses)  # Confirm successful read

# Convert the read string of IPs into a list for processing
ip_addresses = ip_addresses.split()

# Iterate through the list and remove any IPs that match the remove list
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

# Convert the updated list back into a single string for rewriting the file
ip_addresses = " ".join(ip_addresses)

# Open the original file in write mode and overwrite with updated IPs
with open(import_file, "w") as file:
    file.write(ip_addresses)
