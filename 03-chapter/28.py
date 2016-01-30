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
reg_internal = re.compile("\[\[|\]\]")

for line in base_info_text.group().split("\n"):
    reg_list = re.search("\|(.+) = (.+)", line.encode('utf-8'))
    if reg_list:
        value = reg_emphasis.sub("", reg_list.group(2).split("<ref>")[0])
        value = reg_internal.sub("", value)
        value = re.sub("{{|}}", "", value)
        value = re.sub("<.+>",  "", value)
        value = re.sub("\|",  "", value)
        dic[reg_list.group(1)] = value
        print reg_list.group(1), value

