import mymodule as m

text = m.get_article_about_UK()

for line in text.split("\n"):
    if 'Category' in line:
        print line.encode('utf-8')
