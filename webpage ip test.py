import requests
from bs4 import BeautifulSoup
import re

url = "http://127.0.0.1:8000/static/input_ip_file.txt"

# open with GET method
resp = requests.get(url)

# http_respone 200 means OK status
def check_response(resp):
    if resp.status_code == 200:
        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')
        return (soup.prettify())
    else:
        print("Error! Unable to connect server")

content = open("webpage_ip.txt", "w")
content.write(check_response(resp))
content.close()

with open('webpage_ip.txt') as webpage:
    string = webpage.readlines()

pattern = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

valid = open("valid_webpage_ip.txt","w")
invalid = open("invalid_webpage_ip.txt","w")
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