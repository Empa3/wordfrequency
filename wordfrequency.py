from collections import Counter

def frequency(filename, k):
    file = open(filename, "r")
    contents = file.read()
    file.close()

    contents = contents.lower()
    contents = contents.translate({ord(i): None for i in ',.?!'})
    contents = contents.replace('\n', '')
    word_list = contents.split()
    
    counter = Counter(word_list)

    #k är hur många ord som ska visas och behöver ändras efter behov
    most_occur = counter.most_common(k)

    print(most_occur)

"""Manual
1) Öppna terminalen, gå till rätt mapp och skriv: Python3
2) skriv: from wordfrequency import *
3) skriv: frequency("test.txt", k) där test.txt är pathen till filen om den inte ligger i samma direktiv och k är antalet ord"""
    
    
