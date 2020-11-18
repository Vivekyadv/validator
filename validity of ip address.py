import re

with open('input_ip_file.txt') as inputfile:
    string = inputfile.readlines()

# pattern for IP addresses

pattern = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

valid = open("valid_ip.txt","w")
invalid = open("invalid_ip.txt","w")
# extracting the IP addresses
for line in string:
    line = line.rstrip()
    result = re.search(pattern,line)

    # valid IP addresses
    if result:
        valid.write(line)
        valid.write("\n")

    # invalid IP addresses
    else:
        invalid.write(line)
        invalid.write("\n")

valid.close()
invalid.close()