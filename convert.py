import json
from json2html import *
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('filename' ,help='Enter the json file')
args=parser.parse_args()

output_filename = str(args.filename.split('.')[0]) + '.html'
print output_filename


with open(args.filename) as json_data:
    d=json.load(json_data)
    f=json2html.convert(json=d)
    print('<pre>' + f + '</pre> <br>\n')
    with open(output_filename, "w") as e: 
        e.write("<pre>" + f + "</pre> <br>\n")
        e.close()

