# Copyright 2015 Demasse Gregoire Balu tristan
""" This file is part of Blindial.

    Blindial is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

	Blindial is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Blindial. If not, see http://www.gnu.org/licenses/.
"""

# -*-coding: utf8 -*-

import pygame
from random import *
import os
from pygame.locals import *
import sys
from fonction_Q import *
from fct_affichage import *
from fct_rect import *
from fct_texte import *


###########################

def question_fct(nom_musique, lien_musique, categorie, reponse_sous_titre, fenetre_jeu):
    """renvoie 'Bonne réponse' ou 'Mauvaise réponse' en fonction de la réponse choisie"""
    #On initialise la variable de bug
    bug = False

    #On initialise pygame, une fenetre pour les questions et la variable FIN_MUSIQUE
    #qui permet de savoir quand la musique se fini
    pygame.init()
    fenetre_question = pygame.Surface((850, 200))
    fond = pygame.image.load("Images/fond.jpg").convert()


    #On met une image de fond
    fenetre_question.blit(fond, (0, 0))

    #On charge la musique qui a été précédemment choisi

    pygame.mixer.music.load("Musiques"+categorie+"/"+lien_musique)
    pygame.mixer.music.fadeout(2000)
    pygame.time.set_timer(USEREVENT + 1, 35000)
    pygame.mixer.music.play()
    timer = pygame.time.get_ticks()

    #On écrit le titre
    font_title = pygame.font.Font("Polices/appleberry.ttf", 30)
    font_reponse = pygame.font.Font("Polices/appleberry.ttf", 15)
    title = font_title.render("A quoi correspond cet extrait musical ?", True, (255, 255, 255))

        #Partie 1, on créer les textes des réponses

    reponses, sous_titre = reponse_liste_fct(reponse_sous_titre, font_reponse)

        #Partie 2, on créer des surfaces transparentes qui contiennent
        #les réponses et on créer des rectangles pour pouvoir gérer la
        #collision avec la souris plus tard

    pos_surface = fct_rect(reponses, sous_titre, fenetre_question)
    fenetre_question.blit(title, (140, 20))
    fenetre_jeu.blit(fenetre_question, (260, 260))
    pygame.display.flip()






    #Boucle qui permet de rechercher continuellement les events
    continuer = True
    while continuer:

        #Quitte la fenêtre si on appuie sur la croix
        for event in pygame.event.get():

            #Affiche un écran "temps écoulé" si le joueur met plus de 35s a répondre
            if event.type == USEREVENT + 1:
                lance1 = fct_temps(fenetre_question, font_title, fond, reponse_sous_titre, fenetre_jeu)
                return "Mauvais", bug
            elif event.type == KEYDOWN and event.key == K_1:
                continuer = False
                bug = True
            elif event.type == KEYDOWN and event.key == K_2:
                return "Bon", bug

            #Affiche un écran bonne réponse et permet au joueur de rejouer
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                if pos_surface[5].collidepoint(mouse_position):
                    lance = fct_gagne(fenetre_question, font_title, fond, fenetre_jeu)
                    return "Bon", bug

                #Affiche un écran "mauvaise réponse" et passe le tour du joueur
                else:
                    for position in pos_surface[:5]:
                        if position.collidepoint(mouse_position):
                            lance2 = fct_perdu(fenetre_question, font_title, fond, reponse_sous_titre, fenetre_jeu)
                            return "Mauvais", bug

        time = int(36 - (pygame.time.get_ticks() - timer ) / 1000)
        surface_time = font_title.render(str(time), 1, (255, 255, 255))
        fenetre_question.blit(fond, (750, 20), ((800, 150),(750, 20)) )
        fenetre_question.blit(surface_time, (750, 20))
        fenetre_jeu.blit(fenetre_question, (260, 260))
        pygame.display.flip()


    return False, bug


if __name__ == "__main__":
    result = True
    fenetre_jeu = pygame.display.set_mode((1280, 720))
    num_mu = [0, 0, 0, 0]
    categorie = "/Series"
    liste_musique = crea_liste()
    while result:
        #categorie = choice(["/Animes", "/Films", "/Series"])
        lien_musique, nom_musique, nb_categorie = musique_choix(categorie, num_mu, liste_musique)
        liste_reponse = liste_reponse_fct(lien_musique, liste_musique, nom_musique, nb_categorie)
        reponse_sous_titre = sous_titre(liste_reponse)
        result = question_fct(nom_musique, lien_musique, categorie, reponse_sous_titre, fenetre_jeu)
    pygame.quit()
