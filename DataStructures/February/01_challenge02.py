'''
Date: Feb 01
Challenge: Count each word from the given sentence
'''

sentence = input("Frame a sentence:")

splitSentence = sentence.split(' ')
dict = {}

for iEach in splitSentence:
    v = 0
    for jEach in splitSentence:
        if iEach == jEach:
            v += 1
    dict[iEach] = v

print(dict)