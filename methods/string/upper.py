stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro=''

for word in org.split():
    if(word not in stopwords):
        acro = acro + word[0].upper()