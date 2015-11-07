# coding: utf-8
import mymodule as m
import re

text = m.get_article_about_UK()

for line in text.split("\n"):
    reg_list = re.search("\[\[(File|ファイル):(.+?)\|.+\]\]", line.encode('utf-8'))
    if reg_list:
        print reg_list.group(2)
    
