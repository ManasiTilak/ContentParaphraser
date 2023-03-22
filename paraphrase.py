#For Tokenizing using nltk
import nltk
from nltk.tokenize import sent_tokenize
#For Paraphraser, parrot
from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

#downloading punct
nltk.download('punkt')

#Initialising parrot
parrot = Parrot()

paragraph = input("Enter text to paraphrase")


phrases = sent_tokenize(paragraph)
print(phrases)

#Paraphrasing
for phrase in phrases:
        print("-"*100)
        print("Input_phrase: ", phrase)
        print("-"*100)
        para_phrases = parrot.augment(input_phrase=phrase)
        for para_phrase in para_phrases:
            print(para_phrase)
