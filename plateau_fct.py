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
    along with BLindial. If not, see http://www.gnu.org/licenses/.
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
from Lanceur_question import *

from rect_cases import *
from tours_de_jeu import *
from de import *
from Menu import *
from affichage_mediator import *
###########################

def fct_plateau(joueurs, fenetre_jeu, noms):
    """ La fonction principale qui gère les tours de jeu et le plateau"""
    nom_joueur = noms
    #On charge l'image du plateau
    plateau = pygame.image.load("Images/flygame.jpg").convert()
    fenetre_jeu.blit(plateau, (0, 0))
    pygame.display.flip()
    result = True
    num_mu = [0, 0, 0, 0]
    #On créer les rectangles des cases du plateau
    cases_vertes, cases_oranges, cases_jaunes, cases_rouges, cases_rejouer, cases_mediator, cases_depla, liste_case = rect_cases()
    #On créer la liste des musiques
    liste_musique = crea_liste()
    #On créer la liste de joueur
    liste_joueur = list(range(joueurs))
    font_joueur = pygame.font.Font("Polices/appleberry.ttf", 30)
    pos = [(0, 0), (5, 40), (40, 5), (40, 40)]
    pos_player = [(609, 329), (614, 369), (649, 334), (649, 369)]
    pos_courante = [(609, 329), (609, 329), (609, 329), (609, 329)]
    for i in range(joueurs):

        liste_joueur[i] = [pos[i], 0, 0, 0, 0]
    #On créer une liste d'image joueur
    image_creation = ["Images/joueur1.png", "Images/joueur2.png", "Images/joueur3.png", "Images/joueur4.png"]
    image_joueur = []
    for i in range(joueurs):

        joueur = pygame.image.load(image_creation[i]).convert()
        image_joueur.append(joueur)

    joueur_now = 0
    de_test = 1
    jeu = True


    continuer = True
    fin = False
    while continuer:

        if de_test == 1:
            #Si le dé n'a pas déjà été lancé ce tour

                de, surf = lancer_de()
                fenetre_jeu.blit(surf, (1100, 100))
                pygame.display.flip()
                case_joueur = pos_courante[joueur_now]
                #On test les cases qui sont atteignables en fonction du numéro
                #du dé et de la postion du joueur
                cases_possibles = verif_case(case_joueur, de, liste_case)
                #On entoure ces cases
                contour(cases_possibles, case_joueur, fenetre_jeu)
                de_test = 2

        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = False
            elif event.type == QUIT:
                jeu = False
                continuer = False
            elif event.type == KEYDOWN and event.key == K_7:
                image_victoire, joueur_victoire = victoire(joueur_now, fenetre_jeu, nom_joueur)
                fenetre_jeu.blit(image_victoire, (0, 0))
                fenetre_jeu.blit(joueur_victoire, (715, 225))
                pygame.display.flip()
                presskey()
                continuer = False
                fin = True
            elif event.type == KEYDOWN and event.key == K_8:
                cases_possibles = liste_case
            #Si on clique sur une case on prend la position de la souris
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                for position in cases_possibles:
                    if position.collidepoint(mouse_position):


                    #Si cette position est dans une case on fait les effets de cette case
                        if position in cases_vertes:
                            #On prend les coordonnées de cette case pour déplacer le joueur dessus
                            place = position.topleft
                            pos_courante[joueur_now] = place
                            pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                            #On choisi la catégorie de la case et on lance la question
                            categorie = "/Series"
                            result, de_test = questionnaire(categorie, num_mu, liste_musique, fenetre_jeu)
                        elif position in cases_rouges:
                            place = position.topleft
                            pos_courante[joueur_now] = place
                            pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                            categorie = "/Clips"
                            result, de_test = questionnaire(categorie, num_mu, liste_musique, fenetre_jeu)
                        elif position in cases_jaunes:
                            place = position.topleft
                            pos_courante[joueur_now] = place
                            pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                            categorie = "/Films"
                            result, de_test = questionnaire(categorie, num_mu, liste_musique, fenetre_jeu)
                        elif position in cases_oranges:
                            place = position.topleft
                            pos_courante[joueur_now] = place
                            pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                            categorie = "/Animes"
                            result, de_test = questionnaire(categorie, num_mu, liste_musique, fenetre_jeu)
                        elif position in cases_mediator:
                            place = position.topleft
                            pos_courante[joueur_now] = place
                            pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                            if position == cases_mediator[0]:
                                categorie = "/Series"
                                ind = 1
                            elif position == cases_mediator[1]:
                                categorie = "/Clips"
                                ind = 2
                            elif position == cases_mediator[2]:
                                categorie = "/Films"
                                ind = 3
                            elif position == cases_mediator[3]:
                                categorie = "/Animes"
                                ind = 4
                            result, de_test = questionnaire(categorie, num_mu, liste_musique, fenetre_jeu)
                            if result == "Bon":
                                play = liste_joueur[joueur_now]
                                play[ind] = 1
                        elif position in cases_rejouer:
                            place = position.topleft
                            pos_courante[joueur_now] = place
                            pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                            de_test = 1
                            if position == cases_rejouer[2] and liste_joueur[joueur_now] == [liste_joueur[joueur_now][0], 1, 1, 1, 1]:
                                image_victoire, joueur_victoire = victoire(joueur_now, fenetre_jeu, nom_joueur)
                                fenetre_jeu.blit(image_victoire, (0, 0))
                                fenetre_jeu.blit(joueur_victoire, (715, 225))
                                pygame.display.flip()
                                presskey()
                                continuer = False
                                fin = True

                        elif position in cases_depla:
                            if position == cases_depla[0]:
                                place = (881, 601)
                                pos_courante[joueur_now] = place
                                pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                                categorie = "/Animes"
                                ind = 4
                            elif position == cases_depla[1]:
                                place = (337, 601)
                                pos_courante[joueur_now] = place
                                pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                                categorie = "/Films"
                                ind = 3
                            elif position == cases_depla[2]:
                                place = (881, 57)
                                pos_courante[joueur_now] = place
                                pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                                categorie = "/Clips"
                                ind = 2
                            elif position == cases_depla[3]:
                                place = (337, 57)
                                pos_courante[joueur_now] = place
                                pos_player = position_joueurs(place, liste_joueur, joueur_now, pos_player)
                                categorie = "/Series"
                                ind = 1
                            result, de_test = questionnaire(categorie, num_mu, liste_musique, fenetre_jeu)
                            if result == "Bon":
                                play = liste_joueur[joueur_now]
                                play[ind] = 1




        pygame.mixer.music.stop()
        if fin != True:
            fenetre_jeu.blit(plateau, (0, 0))
            med_dub = pygame.image.load("Images/med_dub.png").convert_alpha()
            fenetre_jeu.blit(med_dub, (30, 400))
            for i in range(joueurs):
                fenetre_jeu.blit(image_joueur[i], pos_player[i])

            fenetre_jeu.blit(surf, (1100, 100))
            contour(cases_possibles, case_joueur, fenetre_jeu)
            nom_joueur_en_cour = font_joueur.render(nom_joueur[joueur_now], True, (255, 255, 255))
            fenetre_jeu.blit(nom_joueur_en_cour, (163, 21))
            affichage_mediator(liste_joueur, fenetre_jeu, nom_joueur, image_joueur, font_joueur)


            pygame.display.flip()
            if result == "Mauvais" and joueur_now < (joueurs-1):
                joueur_now = joueur_now + 1
                result = "Bon"
            elif result == "Mauvais" and joueur_now >= (joueurs-1):
                joueur_now = 0
                result = "Bon"
            else:
                joueur_now = joueur_now


    return jeu
