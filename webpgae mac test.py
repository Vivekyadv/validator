import requests
from bs4 import BeautifulSoup
import re

url = "http://127.0.0.1:8000/static/input_mac_file.txt"

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

content = open("webpage_mac.txt", "w")
content.write(check_response(resp))
content.close()

with open('webpage_mac.txt') as webpage:
    string = webpage.readlines()

pattern = re.compile("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

valid = open("valid_webpage_mac.txt","w")
invalid = open("invalid_webpage_mac.txt","w")
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