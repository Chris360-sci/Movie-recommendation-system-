# Semantic similarity Task 2
# import spaCy once installed
import spacy
# load the model and assign it to the variable nlp
nlp = spacy.load('en_core_web_md')
# open text file and store it in f
f = open('movies.txt', "r")
# create an empty dictionary to store the movie title and description
d = {}
# loop through each line
for line in f :
    # separate the title from the description
    x = line.split(":") 
    a = x[0]
    b = x[1]
    # to remove the '\n', first get the length of b-1
    c = len(b)-1
    # then, go from element 0 to the length of b-1 (doesn't include the last element either)
    b = b[0:c]
    d[a] = b 
# print the dictionary
print(d)
# create a variable for the Planet Hulk description
descrip = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''
sentence = nlp(descrip)
# create an empty list to store the similarities
similarities = []
# loop through the descriptions and compare each one to the Planet Hulk description
for description in d.values():
    similarity = nlp(description).similarity(sentence)
    similarities.append(similarity)
# get the index value of the largest similarity
index = similarities.index(max(similarities))
# retrieve the title of the movie 
count = 0
for title in d.keys():
    if count == index:
        print(title)
    count += 1
# close the file
f.close()
