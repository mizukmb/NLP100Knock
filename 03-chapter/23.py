import mymodule as m
import re

text = m.get_article_about_UK()

for line in text.split("\n"):
    reg_list = re.search("(==+)(.+)", line.encode('utf-8'))
    if reg_list:
        section = reg_list.group(2).replace('=', '')
        lv = len(reg_list.group(1))-1
        print section, ':', lv
