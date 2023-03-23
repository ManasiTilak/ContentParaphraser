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

#User Input
paragraph = input("Enter Text to ParaPhrase")

#Spliting paragraph into sentences
phrases = sent_tokenize(paragraph)

#Paraphrasing and adding the paraphrased lines to para[]
para = []
for phrase in phrases:
    para_phrase = parrot.augment(input_phrase=phrase, max_return_phrases = 1)
    print(para_phrase)
    if para_phrase:         
        new_line = (para_phrase[0][0]).capitalize()
        if new_line.endswith('.'):
            para.append(new_line)
        else:
            para.append(new_line+".")
    else:
        para.append(phrase)

#Putting lines in para[] together to form a paragraph
output_para= [' '.join(x for x in para)]
print(output_para)
