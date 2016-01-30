# coding: utf-8
import mymodule as m
import urllib2
import json
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

text = m.get_article_about_UK()
base_info_text = re.search("{{基礎情報 国\n(.+\n)*?}}", text.encode('utf-8'))
dic = {}

for line in base_info_text.group().split("\n"):
    reg_list = re.search("\|(.+) = (.+)", line.encode('utf-8'))
    if reg_list:
        dic[reg_list.group(1)] = reg_list.group(2).split("<ref>")[0]

print dic["国旗画像"]
url = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:" + re.sub(" ", "%20", dic["国旗画像"]) + "&iiprop=url&prop=imageinfo&format=json"
content_json = urllib2.urlopen(url).read()

content = json.loads(content_json)

print content['query']['pages']['347935']['imageinfo'][0]['url']
