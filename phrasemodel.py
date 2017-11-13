import sys
import os
import spacy
from gensim.models import Phrases
from gensim.models.word2vec import LineSentence

# userinput = open(sys.argv[1],'r').read()
# # nlp = spacy.load('en')
# # doc = nlp(userinput)

unigram_sentences = LineSentence(sys.argv[1])
bigram_sentences_filepath = os.path.join('..', 'bigram_sentences_all.txt')
bigram_model = Phrases(unigram_sentences)

with open(bigram_sentences_filepath, 'w') as f:
	for unigram_sentence in unigram_sentences:
		bigram_sentence = u' '.join(bigram_model[unigram_sentence])
		f.write(bigram_sentence + '\n')



# trigram_model = Phrases(bigram_model)


