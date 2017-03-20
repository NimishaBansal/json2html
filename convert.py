import json
from json2html import *
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('filename' ,help='Enter the json file')
parser.add_argument('output_filename' ,help='Enter the name of output file with html extension')
args=parser.parse_args()
with open(args.filename) as json_data:
    d=json.load(json_data)
    f=json2html.convert(json=d)
    print('<pre>' + f + '</pre> <br>\n')
    with open(args.output_filename, "w") as e: 
        e.write("<pre>" + f + "</pre> <br>\n")
        e.close()
        
