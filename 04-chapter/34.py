# coding: utf-8

import mymodule as m

text = open("../data/neko.txt").read()

dict_list = []
for string in text.split():
    c_string = string.replace("　", "")
    morphs = m.get_morphs(c_string)
    for i in range(len(morphs)-2):
        if morphs[i]["pos"] == "名詞" and morphs[i+1]["surface"] == "の" and morphs[i+2]["pos"] == "名詞":
            print morphs[i]["surface"], morphs[i+1]["surface"], morphs[i+2]["surface"]

