#!/usr/bin/python3

import subprocess
import argparse

def shuffledns(wordlist, subdomains):
    subs = []
    script = f"~/go/bin/./shuffledns -l {subdomains} -w {wordlist} -silent"
    result = subprocess.run([script], capture_output=True, shell=True)
    sub = result.stdout
    norm = sub.decode().split("\n")
    subs.append(norm)
    with open('shuffle.txt', 'w') as file:
        file.writelines(f"{s}\n" for s in subs[0])
        
def dnsgen(subdomains):
    wlists = []
    with open('shuffle.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        script = f'echo {line} | dnsgen -'
        result = subprocess.run([script], capture_output=True, shell=True)
        sub = result.stdout
        norm = sub.decode().split("\n")
        wlists.append(norm)
    
    with open(f'{subdomains}', 'r') as file:
        subdomains = file.readlines()
    for subdomain in subdomains:
        script = f'echo {subdomain} | dnsgen -'
        result = subprocess.run([script], capture_output=True, shell=True)
        sub = result.stdout
        norm = sub.decode().split("\n")
        wlists.append(norm)
    
    with open('dnsgen.txt', 'w') as file:
        file.writelines(f'{wlist}' for wlist in wlists)
        
        
    