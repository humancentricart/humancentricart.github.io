import pandas as pd
from pybtex.database.input import bibtex
import os
import yaml


parser = bibtex.Parser()
DATA_DIR = './data'

redo = True

if not os.path.exists('.data/all_pub.csv') or redo:
    data = []
    for f in os.listdir('./data'):
        if not f.endswith('.bib'):
            continue
        bib_data = parser.parse_file(f'./data/{f}')
        for k in bib_data.entries:
            entry = bib_data.entries[k]
            people = entry.persons
            
            authors = '; '.join([str(x) for x in people['author']])

            entry = entry.fields
            entry['authors'] = authors
            data.append(entry)

        data = pd.DataFrame(data)
        print(data)
        data = data.sort_values(['year', 'authors'], ascending=False)
        data = data.fillna('')
        data.to_csv('data/all_pub.csv', index=None)
else:
    data = pd.read_csv('data/all_pub.csv')

print(data.head())
if redo or not os.path.exists('data./all_pub.yaml'):
    with open('data./all_pub.yaml', 'w+') as file:
        text = yaml.dump(
            data.to_dict(orient='records'),
            file,
            sort_keys=False, width=72, indent=4,
            default_flow_style=None)

