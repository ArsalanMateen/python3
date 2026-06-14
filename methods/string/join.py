stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

letters = []
for word in sent.split():
    if(word not in stopwords):
        letters.append(word[:2].upper())

acronym = '. '.join(letters)