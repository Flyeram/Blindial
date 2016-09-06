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

from plateau_fct import *
from affichage_joueurs import *
###########################

def affichage_mediator(liste_joueur, fenetre_jeu, nom_joueur, image_joueur, font_joueur):
    """ Affiche le nom des joueurs, leur icone et les médiators qu'ils on obtenu a coté de leur nom """
    image_med = []
    image_mediator = ["Images/mediator vert.png","Images/mediator rouge.png","Images/mediator jaune.png","Images/mediator orange.png"]
    for i in range(4):
        #Créer les images médiator au format python
        mediator = pygame.image.load(image_mediator[i]).convert_alpha()
        image_med.append(mediator)
    for ind in range(len(liste_joueur)):
        #Affiche les noms des joueurs et leur icone
        fenetre_jeu.blit(image_joueur[ind], (10, 10 + (ind+1)*50))
        nom_j = font_joueur.render(nom_joueur[ind], True, (255, 255, 255))
        fenetre_jeu.blit(nom_j, (35, 10 + (ind+1)*50))
        for med in range(1, 5):
            #Affiche les médiators détenu par le joueur
            if liste_joueur[ind][med] == 1:
                fenetre_jeu.blit(image_med[med-1], (150+(med-1)*30, 10 + (ind+1)*50))
