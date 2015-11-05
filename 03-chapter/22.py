import mymodule as m
import re

text = m.get_article_about_UK()

for line in text.split("\n"):
    if 'Category' in line:
        print re.search("\[\[Category:(.+)\]\]", line.encode('utf-8')).group(1)
        
