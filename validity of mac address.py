import re

with open('input_mac_file.txt') as inputfile:
    string = inputfile.readlines()

# pattern for MAC addresses

pattern = re.compile("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

valid = open("valid_mac.txt","w")
invalid = open("invalid_mac.txt","w")

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
