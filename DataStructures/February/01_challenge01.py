'''
Date: Feb 01
Challenge: Count each letter from a given sentence
'''

sentence = input("Frame a sentence: ")

listSentence = list(sentence)
setSentence = set(listSentence)
dict = {}
for iEach in setSentence:
    v = 0
    for jEach in listSentence:
        if iEach in jEach:
            v += 1
    dict[iEach] = v
    
print(dict)