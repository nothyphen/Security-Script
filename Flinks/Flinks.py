#!/usr/bin/python3

import subprocess
import argpars 

def gospider(targets, filename):
    results = []
    for target in targets:
        script = f'~/go/bin/./gospider --site {target} --other-source --include-other-source --depth 3 --quiet --robots --sitemap --json | grep -v "\[url\]" | jq -r ".output" | grep -Eiv "\.(css/jpeg/png/svg/img/mp4/flv/ogv/webm/webp/mov/mp3/m4a/m4p/ppt/pptx/scss/tif/tiff/ttf/otf/woff/woff2/bmp/ico/eot/htc/swf/rtf/image)" | sort -u'
        run = subprocess.run([script], capture_output=True, shell=True)
        result = run.stdout
        norm = result.decode().split("\n")
        results.append(norm)
    with open(f'{filename}-sp', "w") as file:
        file.writelines(f"{result}\n" for result in results[0])

def robofinder(targets, filename):
    results = []
    for target in targets:
        script = f"python3 robofinder/robofinder.py -u {target}"
        run = subprocess.run([script], capture_output=True, shell=True)
        result = run.stdout
        norm = result.decode().split("\n")
        results.append(norm)
    with open(f"{filename}-rb", "w") as file:
        file.writelines(f"{target}\n" for result in results[0])

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
    gospider(targets, filename)
    robofinder(targets, filename)


if __name__ == "__main__":
    main()