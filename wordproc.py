
import sys
import spacy

userinput = open(sys.argv[1],'r').read() 
nlp = spacy.load('en')

processedtext = nlp(userinput)
print (processedtext)
