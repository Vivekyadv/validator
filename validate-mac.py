import requests
from bs4 import BeautifulSoup
import re

url = "http://127.0.0.1:8000/static/input_mac_file.txt"

print("[+] Connecting Server...")
resp = requests.get(url)

# http_respone 200 means OK status
def check_response(resp):
    if resp.status_code == 200:
        # we need a parser
        soup = BeautifulSoup(resp.text, 'html.parser')
        return (soup.prettify())
    else:
        print("Error! Unable to connect server")

# webpage_mac file to store the data from webpage
content = open("/root/Projects/TOC/input files/webpage_mac.txt", "w")
content.write(check_response(resp))
content.close()

with open('/root/Projects/TOC/input files/webpage_mac.txt') as webpage:
    string = webpage.readlines()

pattern = re.compile("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

print("[+] Validating MAC Address...")
valid = open("/root/Projects/TOC/output files/valid-mac.txt","w")
invalid = open("/root/Projects/TOC/output files/invalid-mac.txt","w")
# extracting the MAC addresses
for line in string:
    line = line.rstrip()
    result = re.search(pattern,line)

    # valid MAC addresses
    if result:
        valid.write(line)
        valid.write("\n")

    # invalid MAC addresses
    else:
        invalid.write(line)
        invalid.write("\n")

valid.close()
invalid.close()

print("[+] Program Run Successfully")
print("[+] Valid MAC Addresses have been stored in 'output files' directory")