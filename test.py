import os
import sys
import time
import pandas as pd

cwd = os.getcwd()
print(cwd)

now = time.time()
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

flix_data = pd.read_json('https://healthdata.gov/resource/rxn6-qnx8.json')
flix_data

flix_data.to_csv('data/flix_data.csv')

with open(cwd + '/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(flix_data))
