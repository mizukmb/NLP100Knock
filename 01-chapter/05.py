def n_gram(str, n):
    list = []
    for i in range(len(str)-n+1):
        list.append(str[i:i+n])
    
    return list

str = "I am an NLPer"
print n_gram(str, 2)
print n_gram(str.split(), 2)
