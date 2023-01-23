import nltk 
nltk.download('stopwords')
import pandas as pd
import json 
from nltk.corpus import stopwords


rmv_word = {"glands", "disorders", "enlargement" "insufficiency", "gland", "medicine", "books", "features",
          "WHO", "histology", "terms", "stains", "disease",
          "infection", "tissue", "vitamin", "autopsy",
          "anatomy", "syndrome", "development", "transfusion",
            "management", "chemistry",
            "Lab", "informatics", "small", "covid-19", "topics"}


def filter(text, flag=False):
    tokenized = nltk.word_tokenize(text)
    nouns = ""
    all_noun = set()
    for (word, pos) in nltk.pos_tag(tokenized):
        word = word.lower()
        if (pos[:2] == 'NN'):
            if word not in stopwords.words('english'):
                if word != "/":
                    all_noun.add(word)
    
    for noun in all_noun:
        if len(noun) >= 4 and (noun[-4:] == "logy" or noun[-4:]=="ysis" or noun[-3:]=="ion"):
            continue
        else:
            if noun.lower() not in rmv_word:
                if flag==True:
                    noun = str.capitalize(noun)
                nouns+=noun
                nouns+=" "
    return nouns


f = open('organ.json')
organ = json.load(f)

organ_final = {}

for key, value in organ.items():
    new_key = filter(key, True)
    new_value = filter(value)
    for word in nltk.word_tokenize(new_key):
        organ_final[word] = new_value
    
for key, value in organ_final.items():
    print(key, value, sep = "----")
    

json.dump(organ_final, open('organ_final.json', 'w'))

# print(organ_final)