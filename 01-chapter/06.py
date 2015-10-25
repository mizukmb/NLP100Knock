def n_gram(str, n):
    list = []
    for i in range(len(str)-n+1):
        list.append(str[i:i+n])
    
    return list

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(n_gram(str1, 2))
Y = set(n_gram(str2, 2))

print list( X | Y )
print list( X & Y )
print list( X - Y )

print 'se' in (X | Y)
