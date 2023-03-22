
# Project Title

Content Paraphraser using parrot and NLTK in python


## How it works?

- This script takes input from from user in form of text.
- Tokenises it using NLTK library.
- Runs the tokens through the PARROT 5 model.
- Returns various para-phrased sentences to choose from.


## Description of Libraries used:
- PARROT : https://github.com/PrithivirajDamodaran/Parrot.git

The parrot library contains the pre-trained text paraphrasing model. Under the hood, the pre-trained text paraphrasing model was created using PyTorch (torch) and thus we’re importing it here in order to run the model. This model is called parrot_paraphraser_on_T5 and is listed on the Hugging Face website. It should be noted that Hugging Face is the company that develops the transformer library which hosts the parrot_paraphraser_on_T5 model.

- NLTK : Natural Language Toolkit

NLTK is a leading platform for building Python programs to work with human language data. It provides a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English. NLTK is intended to support research and teaching in NLP or closely related areas, including empirical linguistics, cognitive science, artificial intelligence, information retrieval, and machine learning.