# coding: utf-8

import gzip
import json

def get_article_for_UK():
    text=""
    for line in gzip.open('../data/jawiki-country.json.gz'):
        data = json.loads(line)
        if u'イギリス' in data['title']:
            text = data['text']
    return text

t = get_article_for_UK()
print t.encode('utf-8')
