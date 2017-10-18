#! /usr/bin/env python
# coding: utf-8

# Note: this program requires sklearn to be installed.
# Sklearn itself requires SciPy

# sudo apt-get install python-numpy python-scipy python-matplotlib ipython python-pandas python-sympy python-nose
# pip install -U sklearn

import sklearn
from sklearn.naive_bayes import MultinomialNB

corpus_train = [
    ("Phillipe est un con", 1),
    ("Phillipe est chiant et un connard!", 1),
    ("J'aime bien Phillipe", 0),
    ("Phillipe peut aller crever", 1),
    ("Ta gueule Phillipe", 1),
    ("Ce cours est pas terrible", 0),
    ("Python c'est cool", 0),
    ("J'aime bien Python", 0),
    ("Bonjour mec ça va bien?", 0),
    ("Salut, ouais ça va et toi?", 0),
    ("Oui sauf que comme d'hab Phillipe fait chier", 1),
    ("Bah ignore le.", 0),
    ("Ouais pas con.", 0),
    ("Bon écoute tu ferme ta gueule j'ai pas le temps aujourd'hui", 1),
    ("Va sucer des mikos", 1),
    ("Mange mon yélito", 1),
    ("Ouais c'est des logos comme ça que j'avais.", 0),
    ("Tin c'est long à télécharger", 0),
    ("Le mec s'est foiré alors qu'il avait le truc?", 0),
    ("Ah non il est extrèmement con.", 1),
    ("Putain de Phillipe", 1)
]



corpus_test = [
    ("Des préservatifs je suis tout le temps dedans jamais autours", 1),
    ("J'avance pas sur mon projet", 0),
    ("On a toujours eu des bons doctorants, maintenant on a Etienne", 0),
    ("Raclure de fond de capote", 1),
    ("Pour une fois qu'on a besoin de Phillipe", 0),
    ("Je vois qu'on s'amuse bien!", 0),
    ("Mais va chier connard!", 1),
    ("Putain cet example me soule.", 1),
]

def tokenize_text(text):
    return text.split()

def build_dict(corpus):
    d = {}
    i = 0
    for text, label in corpus:
        for word in tokenize_text(text):
            if word not in d:
                d[word] = i
                i += 1
    return d


def make_BoW(text, word_dict):
    BoW = [0 for i in range(len(word_dict))]
    for w in tokenize_text(text):
        if w in word_dict:
            BoW[word_dict[w]] = 1
    return BoW

def make_BoWs(corpus, word_dict):
    BoWs = []
    for text, label in corpus:
        BoWs.append(make_BoW(text, word_dict))
    return BoWs

if __name__ == '__main__':
    word_dict = build_dict(corpus_train)

    X_train = make_BoWs(corpus_train, word_dict) # Get train features
    y_train = [label for text, label in corpus_train] # Get train labels

    clf = MultinomialNB()
    clf.fit(X_train, y_train) # Train classifier

    X_test = make_BoWs(corpus_test, word_dict) # Get test features

    res = clf.predict(X_test) # Predict labels

    print res


