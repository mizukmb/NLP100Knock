str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = str.split()

dic = {}
single_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for i in range(len(words)):
    word = words[i]
    index = i+1
    len = 1 if index in single_list else 2

    dic[word[:len]] = index
    
print dic
