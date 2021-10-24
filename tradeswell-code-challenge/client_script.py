import requests
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_filename', help='',
                    default='example_input.txt',
                    type=str)
parser.add_argument('--output_filename', help='',
                    default='outout.json',
                    type=str)
args = parser.parse_args()

data = open(args.input_filename,'r').read()
pkg = {'pkg':json.dumps(data.split('\n'))}
res = requests.post('http://localhost:5000/run_tasks',json=pkg)
print(json.loads(res.text))
json.dump(json.loads(res.text),open(args.output_filename,'w'),indent=1)