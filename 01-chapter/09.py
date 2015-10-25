import random

def typo(sentence):
    words = sentence.split()
    out = []
    for word in words:
        if len(word) > 4:
            rand = list(word[1:len(word)-1])
            random.shuffle(rand)
            text = word[0] + ''.join(rand) + word[len(word)-1]
            out.append(text)
        else:
            out.append(word)

    return ' '.join(out)

print typo("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
