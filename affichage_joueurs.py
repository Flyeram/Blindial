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
from Lanceur_question import *
from insertNameHere import *
import plateau_fct
###########################

def affichage_joueurs(fenetre_jeu, texte_joueur, fond, titre, quitter, rect_quitter):
    """ Cette fonction affiche et permet de sélectionner le nombre de joueurs
    Elle prend en argument : La fenetre de jeu, le texte joueur, le fond, le titre, quitter et son rectangle"""

    fenetre_jeu.blit(fond, (0,0))
    fenetre_jeu.blit(titre, (550, 50))
    fenetre_jeu.blit(quitter, (650, 300))
    rect_menu_joueur = rect_menu_joueurs(texte_joueur, fenetre_jeu)
    jeu = True
    pygame.display.flip()


    continuer = 1
    while continuer:
       for event in pygame.event.get():
        #Si on appuie sur echap on revient au menu
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = False
                jeu = True
        #Si on clique sur la croix on ferme la fenetre
            elif event.type == QUIT:
                continuer = False
                jeu = False
            #Si on clique avec la souris
            elif event.type == MOUSEBUTTONDOWN and event.button ==1:
                mouse_position = pygame.mouse.get_pos()
                #Si la position de la souris est sur quitter
                if rect_quitter.collidepoint(mouse_position):
                    continuer = False
                    jeu = False
                #Si la position de la souris est sur un nombre de joueur
                else:
                    for i in range(4):
                            if rect_menu_joueur[i].collidepoint(mouse_position):
                                joueurs = i+1
                                #On lance la suite du programme (Le changement de nom)
                                continuer, jeu = entreNoms(fenetre_jeu, fond, joueurs)

    return False, jeu
