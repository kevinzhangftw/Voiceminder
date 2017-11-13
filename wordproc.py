import sys
import spacy

userinput = open(sys.argv[1],'r').read()
nlp = spacy.load('en')

# print(userinput)
doc = nlp(userinput)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

# print each sentence
# for sent in doc.sents:
#     print(sent)

# speech tag
# for token in doc:
#     print('{} - {}'.format(token, token.pos_))

# entity recognition
# for ent in doc.ents:
#     print('{} - {}'.format(ent, ent.label_))

# noun chunks
# for chunk in doc.noun_chunks:
# 	print(chunk)

# unigram log prob
# for token in doc:
#     print(token, ',', token.prob)

# word comparsion
# apples = doc[0]
# oranges = doc[2]
# boots = doc[6]
# hippos = doc[8]
# print(apples.similarity(oranges))
# print(boots.similarity(hippos))

# Print similarity between sentence and word 'korean'
word = doc.vocab[u'steak']
for sent in doc.sents:
	print(sent.similarity(word))
	