# O POS tagger é horrível na língua portuguesa
# nouns = [word for (word, pos) in palavras_tagueadas if pos in ['NN','NNP','NNS','NNPS']]
# verbs = [word for (word, pos) in palavras_tagueadas if pos in ['VBD', 'VBG', 'VBN', 'VB', 'VBP', 'VBZ']]
#print(nouns)



# Frequências
# from nltk.probability import FreqDist
#
# fdist = FreqDist()
#
# for word in post_punctuation: # frequência dessa lista de 'palavras'
#     fdist[word.lower()]+=1
# fdist_top10 = fdist.most_common(10)
# print(fdist_top10)


# Stemming
# from nltk.stem import RSLPStemmer
# stemmer = RSLPStemmer()
# for word in post_punctuation:
#     #print(word + ":" + stemmer.stem(word))
#     palavras_stemm = stemmer.stem(word)
#     #print(palavras_stemm)
#


# subtree
# def extract_np(psent):
#     for subtree in psent.subtrees():
#         if subtree.label() == 'NP':
#             yield ' '.join(word for word, tag in subtree.leaves())
#
# cp = nltk.RegexpParser(grammar)
# parsed_sent = cp.parse(sentences)
# for npstr in extract_np(parsed_sent):
#     print(npstr)

