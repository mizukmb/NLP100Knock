# coding: utf-8
import mymodule as m
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

text = m.get_article_about_UK()
base_info_text = re.search("{{基礎情報 国\n(.+\n)*?}}", text.encode('utf-8'))
dic = {}
reg = re.compile("''+")

for line in base_info_text.group().split("\n"):
    reg_list = re.search("\|(.+) = (.+)", line.encode('utf-8'))
    if reg_list:
        dic[reg_list.group(1)] = reg.sub("", reg_list.group(2).split("<ref>")[0])
        print reg_list.group(1) , dic[reg_list.group(1)]
