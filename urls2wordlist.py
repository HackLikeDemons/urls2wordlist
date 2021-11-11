#!/usr/local/bin/python3
''' 
urls2wordlist

A simple tool that use a file containing a lits of URLs to generate wordlists for URL-parts and URL-parameters.  
Author: Andreas Wienes - Hack Like Demons - https://twitter.com/AndreasWienes

First draft: 2021-11-11
'''

import urllib.parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='a file with URLs line by line as input')
args = parser.parse_args()
input_file = args.input_file

url_parts_collection = []
url_params_parts_collection = []

with open(input_file) as f:
    urls = [line.rstrip() for line in f]

for url in urls:    
    parsed_url = urllib.parse.urlparse(url)
    
    hostname = parsed_url.netloc
    hostname_parts = hostname.split(".")
    
    for element in hostname_parts:
        url_parts_collection.append(element)
    
    url_path = parsed_url.path
    url_path_parts = url_path.split("/")
    for element in url_path_parts:
        url_parts_collection.append(element)
    
    url_params_parts = parsed_url.query.split("&")
    url_params_parts = [element.split("=")[0] for element in url_params_parts]
    for element in url_params_parts:        
        url_params_parts_collection.append(element)
    
with open('output_url_parts.txt', 'w') as output_file:
    for hostname_part in list(set(url_parts_collection)):
        if len(hostname_part) > 0 and '.' not in hostname_part: 
            output_file.write(hostname_part + '\n')
    
with open('output_url_parameters.txt', 'w') as output_file:
    for url_params_part in list(set(url_params_parts_collection)):        
        if len(url_params_part) > 0: 
            output_file.write(url_params_part + '\n')