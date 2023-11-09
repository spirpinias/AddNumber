#!/usr/bin/env python

import argparse
import sys
import glob
import shutil
import os.path
from pathlib import Path

def main(argv=None):

    parser = argparse.ArgumentParser(description='Add a Number')
    parser.add_argument('--AddNumber', required=True, help="Number of Folders", type=int)

    if argv:
        args = parser.parse_args()
    else:
        parser.print_usage()
        return 0

    num=int(f'{args.AddNumber}')

    print(f'This is the number we are adding : {args.AddNumber}')

    for file in list(glob.glob('/data/*.txt')):                             
        
        reader = open(file,"r")
        first_line = reader.readline()
        new_digit=int(first_line)+num   
        new_name=os.path.basename(file)
        filePath = Path(f"/results/{new_name}")
        filePath.touch(exist_ok=True)
        new_file=open(filePath,"w")
        new_file.write(f"{new_digit}")

    return 0


if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))