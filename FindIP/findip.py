#!/usr/bin/python3

import subprocess
import argparse
import re

def use_regex(input_text):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv4 = re.findall(pattern, input_text)
    return ipv4

def subfinder(domains, filename):
    subs = []
    for domain in domains:
        script = f'~/go/bin/./subfinder -d {domain} -silent'
        
        result = subprocess.run([script], capture_output=True, shell=True)
        sub = result.stdout
        norm = sub.decode().split("\n")
        subs.append(norm)

    with open(f'{filename}', 'w') as file:
        file.writelines(f"{s}\n" for s in subs[0])

def dnsx(filename):
    dnssubs = []
    
    script = f'~/go/bin/./dnsx -l {filename} -a -resp -silent'
    result = subprocess.run([script], capture_output=True, shell=True)
        
    dnsx = result.stdout
    return dnsx.decode()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, help="output list (txt)")
    parser.add_argument("-d", "--domain", type=str, help="domain list (txt)")
    args = parser.parse_args()
    
    with open(args.domain, 'r') as file:
        lines = file.readlines()
    subfinder(lines, args.output)
    result = dnsx(args.output)
    ipv4 = use_regex(result)
    for ip in ipv4:
        print(ip)

if __name__ == "__main__":
    main()
