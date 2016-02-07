# coding: utf-8

from janome.tokenizer import Tokenizer

def get_morphs(string):
    t = Tokenizer()
    dicts=[]
    for token in t.tokenize(unicode(string, 'utf-8')):
        dic = {}
        token_list = str(token).replace("	", ",").split(",")
        dic["surface"] = token_list[0]
        dic["base"] = token_list[6]
        dic["pos"] = token_list[1]
        dic["pos1"] = token_list[2]

        dicts.append(dic)

    return dicts

