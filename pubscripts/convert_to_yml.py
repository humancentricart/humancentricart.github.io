import pandas as pd
from pybtex.database.input import bibtex
import os
import yaml



DATA_DIR = './data'


def get_data_from_bib(f, highlights=False):
    parser = bibtex.Parser() 
    data = []
    bib_data = parser.parse_file(f)
    print(len(bib_data.entries))
    for k in bib_data.entries:
        entry = bib_data.entries[k]
        people = entry.persons

        authors = '; '.join([str(x) for x in people['author']])

        entry = entry.fields
        entry['authors'] = authors

        if highlights:
            entry['highlight'] = 1

        data.append(entry)
    return data

redo = True

if not os.path.exists('data/all_pub.csv') or redo:

    data = get_data_from_bib('data/highlights.bib', highlights=True)
    for f in os.listdir('data'):
        print(f)
        if f == 'highlights.bib' or not f.endswith('.bib'):
            continue
        data = data + get_data_from_bib(f'data/{f}')
        

    data = pd.DataFrame(data)
    
    duplicate_keys = ['title']
    url_lookup = (
        data.groupby(duplicate_keys)['url']
        .agg(lambda x: x.dropna().iloc[0] if x.notna().any() else None)
        .reset_index()
    )
    df_nodup = data.drop_duplicates(subset=duplicate_keys, keep='first')
    data = df_nodup.drop(columns='url').merge(url_lookup, on=duplicate_keys, how='left')

    data = data.fillna('')
    data['year'] = data['year'].apply(lambda x: '-' if x == '' else x)
    data = data.sort_values(['year', 'authors'], ascending=False)
    
    data.to_csv('data/all_pub.csv', index=None)
else:
    data = pd.read_csv('data/all_pub.csv')

print(data.head())
if redo or not os.path.exists('data/all_pub.yaml'):
    with open('data/all_pub.yaml', 'w+') as file:
        text = yaml.dump(
            data.to_dict(orient='records'),
            file,
            sort_keys=False, width=72, indent=4,
            default_flow_style=None)

