#!/usr/bin/python3

from urllib.parse import urlparse, parse_qs
import argparse, json

def extract(targets, filename):
    parameters = []
    outputs = []
    
    with open(f'{targets}', 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        parsed_url = urlparse(line)
        params = parse_qs(parsed_url.query)
        parameters.append(params)
    
    for param in parameters:
        for p in param:
            outputs.append(p)
    outputs = list(set(outputs))
    
    with open(f'{filename}', 'w') as file:
        file.writelines(f'{output}\n' for output in outputs)
    
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, help="output list (txt)")
    parser.add_argument("-d", "--domain", type=str, help="domain list (txt)")
    args = parser.parse_args()
    
    return args

def main():
    args = get_args()
    targets = args.domain
    filename = args.output
    params = extract(targets, filename)

if __name__ == "__main__":
    main()