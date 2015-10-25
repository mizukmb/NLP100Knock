def cipher(string):
    return ''.join([chr(219-ord(x)) for x in string if ord(x)>=97 and ord(x)<=122])

print cipher("hakodate")
print cipher(cipher("hakodate"))
