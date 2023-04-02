# -*- coding: utf-8 -*-
"""embedding_evaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b3SaQBXbh5Z8aDN3LKIeapwCgi-Puhpc
"""

import gensim
import nltk
import pandas as pd
import numpy as np

nltk.download('punkt')

df = pd.read_csv('EcritureInclusive_dataset.csv', sep=";")
df['2'] = df['2'].str.lower()

print(df['2'])

train_set = df['2'].values # 1st 80% of corpus 
train_set = train_set[0: int(len(train_set) * 0.8)]

training_set = [nltk.word_tokenize(article) for article in train_set]

model = gensim.models.Word2Vec(training_set, min_count=1)

# constructing gender space of which to later calculate the cosine similarity of words onto this. 
# more components to any of these pairs of words than just their gender, so combining their vector directions
# encodes a gender direction -- pairs are mostly a translation from those used in Bolukbasi et. al. 
# except for ils/elles and le/la for which there is no english gender pair equivalent
masculin = ['il', 'ils', 'homme', 'garçon', 'frère', 'fils', 'le', 'père', 'mec', 'mâle', 'jean']
feminin = ['elle', 'elles', 'femme', 'fille','sœur', 'fille', 'la', 'mère', 'meuf', 'femelle', 'marie']
espace_genre = 0
for i in range(len(masculin)):
  espace_genre += model.wv[masculin[i]]
  espace_genre -= model.wv[feminin[i]]

model.wv.most_similar(espace_genre)

print(model.wv.similarity('homme', 'auteur'))
print(model.wv.similarity('femme', 'auteur'))

#MOTS EPICÈNES -- no distinction between masculine and feminine word forms
epicenes = ['activiste', 'artiste', 'céramiste', 'cinéaste', 'dentiste', 'dramaturge', 'guide', 'juriste', 'majordome', 'peintre', 'pilote', 'sculpteur', 'vétérinaire', 'capitaine', 'commissaire', 'docteur', 'gendarme', 'juge', 'maire', 'ministre', 'porte-parole', 'professeur', 'secrétaire', 'accessoiriste']
for mot in epicenes:
  b = model.wv[mot]
  cos_sim = np.dot(espace_genre, b)/(np.linalg.norm(espace_genre)*np.linalg.norm(b))
  print(mot, cos_sim)

# profession pairs where adding an e at the end is optional and recently added to language
neologismes = ['auteur', 'auteure', 'auteur·es', 'chercheur', 'chercheure', 'chercheur·e·s', 'écrivain', 'écrivaine', 'professeur', 'professeure', 'docteur', 'docteure', 'entrepreneur', 'entrepreneure', 'gouverneur', 'gouverneure', 'pasteur', 'pasteure', 'procureur', 'procureure', 'rapporteur', 'rapporteure', 'médecin', 'médecine']
for mot in neologismes:
  b = model.wv[mot]
  cos_sim = np.dot(espace_genre, b)/(np.linalg.norm(espace_genre)*np.linalg.norm(b))
  print(mot, cos_sim)

# Other nouns written that use concatenation of forms, observed in dataset
inclusif = ['auteur', 'auteure', 'auteur·es', 'auteur·trice', 'candidat','candidats', 'candidate', 'candidates', 'candidat·e·s', 'chercheur', 'chercheure', 'chercheur·e·s', 'lycéen', 'lycéenne', 'lycéen·e·s', 'invité', 'invitée', 'invité·e·s', 'citoyen', 'citoyens', 'citoyenne', 'citoyennes', 'citoyen·nes', 'opposant', 'opposante', 'opposant·es', 'étudiant', 'étudiants', 'étudiante', 'étudiantes', 'étudiant·e·s', 'ami', 'amis', 'amie', 'amies', 'ami·e·s', 'acteur', 'acteurs', 'actrice', 'actrices', 'acteur·ices', 'habitant', 'habitants', 'habitante', 'habitantes', 'habitant·es', 'salarié', 'salariée', 'salariées', 'salarié·e·s', 'professionnel', 'professionnelle', 'professionnel·le', 'professionnel·le·s', 'guerrier', 'guerriers', 'guerrière', 'guerrières', 'guerrier·ère·s', 'toute', 'tous', 'tou·te·s', ]

for mot in inclusif:
  b = model.wv[mot]
  cos_sim = np.dot(espace_genre, b)/(np.linalg.norm(espace_genre)*np.linalg.norm(b))
  print(mot, cos_sim)

# French version of famous analogy Man:Computer Programmer :: Woman:X
analogy = model.wv['femme'] - model.wv['homme'] + model.wv['informaticien']
model.wv.most_similar(analogy)

model.wv.most_similar(positive=['il','homme', 'garçon', 'frère', 'le', 'père', 'copain'], negative=['elle', 'femme', 'fille','sœur', 'la', 'mère', 'copine'], topn=20)

#vec = model['roi'] - model['homme'] + model['femme']
#print(model.wv.most_similar(vec))

model.wv.most_similar(positive=['elle', 'femme', 'fille','sœur', 'la', 'mère', 'copine'], negative=['il','homme', 'garçon', 'frère', 'le', 'père', 'copain'], topn=20)

from google.colab import drive
drive.mount('/content/drive')