# coding: utf-8
import mymodule as m
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

text = m.get_article_about_UK()
base_info_text = re.search("{{基礎情報 国\n(.+\n)*?}}", text.encode('utf-8'))
dic = {}
reg_emphasis = re.compile("'+")
reg_internal = re.compile("\[\[(?!.+:)(.*\|)?(.*?)\]\]")

for line in base_info_text.group().split("\n"):
    reg_list = re.search("\|(.+?) = (.+?)(\Z|<)", line.encode('utf-8'))
    if reg_list:
        value = reg_internal.search(reg_list.group(2))
        value = reg_emphasis.sub("", value.group(2)) if value else reg_emphasis.sub("", reg_list.group(2))
        dic[reg_list.group(1)] = value
        print reg_list.group(1), value
