#! /usr/bin/python3
import spacy
nlp = spacy.load("en")
doc = nlp(u"This is a sentence.")
print(doc)
