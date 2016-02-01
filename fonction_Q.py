# -*-coding: utf8 -*-

import pygame
from random import *
import os
from pygame.locals import *
import sys
from fct_texte import *
from Lanceur_question import *
###########################

def crea_liste():
    
    liste_musique_anime = os.listdir("Musiques/Animes")  #On créer une liste avec toutes
    liste_musique_clip = os.listdir("Musiques/Clips")    #les chansons par catégorie
    liste_musique_film = os.listdir("Musiques/Films")
    liste_musique_serie = os.listdir("Musiques/Series")
    shuffle(liste_musique_anime), shuffle(liste_musique_clip), shuffle(liste_musique_film), shuffle(liste_musique_serie)
    return [liste_musique_anime, liste_musique_clip, liste_musique_film, liste_musique_serie]

def musique_choix(categorie, num_mu, liste_musique):
    
    if categorie == "/Animes":
        #On test si la liste est finie, si oui on en récrée une.
        if num_mu[0] > len(liste_musique[0])-1:
            num_mu[0] = 0
            shuffle (liste_musique[0])
        #On choisit la liste correspondant a la catégorie
        liste_categorie = liste_musique[0]        
        musique_choix = liste_categorie[num_mu[0]]
        #On augmente de 1 l'indice de la catégorie
        num_mu[0] += 1
        nb_categorie = 0
    elif categorie == "/Clips":
        if num_mu[1] > len(liste_musique[1])-1:
            num_mu[1] = 0
            shuffle (liste_musique[1])
        liste_categorie = liste_musique[1]
        musique_choix = liste_categorie[num_mu[1]]
        num_mu[1] += 1
        nb_categorie = 1
    elif categorie == "/Films":
        if num_mu[2] > len(liste_musique[2])-1:
            num_mu[2] = 0
            shuffle (liste_musique[2])
        liste_categorie = liste_musique[2]
        musique_choix = liste_categorie[num_mu[2]]
        num_mu[2] += 1
        nb_categorie = 2
    elif categorie == "/Series":
        if num_mu[3] > len(liste_musique[3])-1:
            num_mu[3] = 0
            shuffle (liste_musique[3])
        liste_categorie = liste_musique[3]
        musique_choix = liste_categorie[num_mu[3]]
        num_mu[3] += 1
        nb_categorie = 3
        
    reponse = musique_choix.split(".")               
    

    return musique_choix, reponse[0], nb_categorie

def liste_reponse_fct(lien_musique, liste_musique, nom_musique, nb_categorie):
    compteur = 0
    liste_reponse = []
    #On créer une liste de 4 fausses réponses pour les choix de réponses
    while compteur < 5:
        #La liste est créée en fonction de la catégorie
        plus = choice(liste_musique[nb_categorie])
        nom_reponse = plus.split(".")
        if nom_reponse[0] != nom_musique and nom_reponse[0] not in liste_reponse:
            liste_reponse.append(nom_reponse[0])
            compteur += 1

    liste_reponse.append(nom_musique)
    return liste_reponse

def presskey():
    while True:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                 return

def questionnaire(categorie, num_mu, liste_musique, fenetre_jeu):
    bug = True
    while bug == True:
        
        lien_musique, nom_musique, nb_categorie = musique_choix(categorie, num_mu, liste_musique)
        liste_reponse = liste_reponse_fct(lien_musique, liste_musique, nom_musique, nb_categorie)
        reponse_sous_titre = sous_titre(liste_reponse)
        result, bug = question_fct(nom_musique, lien_musique, categorie, reponse_sous_titre, fenetre_jeu)
    return result, 1



if __name__ == "__main__":
    musique = musique_choix("/Animes")
    nom_musique = musique[1]
    lien_musique = musique[0]
    liste_musique = musique[2]
    liste_reponse = liste_reponse_fct(lien_musique, liste_musique, nom_musique)
    print(question_fct(nom_musique, lien_musique, "/Animes", liste_reponse))
    
