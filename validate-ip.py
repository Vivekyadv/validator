import requests
from bs4 import BeautifulSoup
import re

url = "http://127.0.0.1:8000/static/ip_file.txt"

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

# webpage_ip file to store the data from webpage
content = open("/root/Projects/TOC/input files/webpage_ip.txt", "w")
content.write(check_response(resp))
content.close()

with open("/root/Projects/TOC/input files/webpage_ip.txt") as webpage:
    string = webpage.readlines()

pattern = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

print("[+] Validating IP Address...")
valid = open("/root/Projects/TOC/output files/valid-ip.txt","w")
invalid = open("/root/Projects/TOC/output files/invalid-ip.txt","w")

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

print("[+] Program Run Successfully")
print("[+] Valid IP Addresses have been stored in 'output files' directory ")