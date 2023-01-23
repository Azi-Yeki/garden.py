import spacy

nlp = spacy.load('en_core_web_sm')

#adding five garden  path sentences found on the internet
gardenpathSentences = u"The old man the boat, We painted the wall with cracks, The girl told the story cried, That Jill is never here hurts, The horse raced past the barn fell"

doc = nlp(gardenpathSentences)

#tokenising the sentences
#splitting the sentences at the commas
doc.text.split(", ")

[token.orth_ for token in doc]

#accessing each token’s .orth_ method which returns a string representation of the token
print([(token, token.orth_, token.orth) for token in doc])

#avoid returning tokens that are punctuations or white space
print([token.orth_ for token in doc if not token.is_punct | token.is_space])

#getting labels and entities and printing them
nlp_gardenpathSentences = nlp(gardenpathSentences)
print([(i, i.label_, i.label) for i in nlp_gardenpathSentences.ents])

#looking up the entities, their meanings and printing them
entity_fac = spacy.explain("NORP")
print(f"NORP:{entity_fac}")

entity_fac = spacy.explain("GPE")
print(f"GPE:{entity_fac}")

#the first entity is NORP which is Nationalities, or religious or political groups. It makes sense because it's basically the acronym.
#the second entity is GPE which is countries, cities and states. It doesn't make sense because I don't see how the letters are linked to the explanation