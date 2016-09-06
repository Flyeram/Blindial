# Copyright 2015 Demasset Gregoire Balu tristan
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
    along with Foobar. If not, see http://www.gnu.org/licenses/.
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
from Menu import *
###########################


def position_joueurs(place, liste_joueur, joueur_now, pos_player):
    """Fonction pour afficher le joueur sur la case où il est"""
    player = liste_joueur[joueur_now]
    pos_player[joueur_now] = ((place[0] + player[0][0]), (place[1] + player[0][1]))

    return pos_player

def victoire(joueur_now, fenetre_jeu, nom_joueur):
    nb_joueur = str(joueur_now + 1)
    image_victoire = pygame.image.load("Images/Victoire.jpg").convert()
    font_victoire = pygame.font.Font("Polices/appleberry.ttf", 69)
    joueur_victoire = font_victoire.render(nom_joueur[joueur_now]+ " !", True, (255, 255, 255))

    return image_victoire, joueur_victoire







if __name__ == "__main__":
    place = (30, 30)
    liste_joueur = [[(10, 10), 0], [(20, 20), 3]]
    joueur_now = 0
    print(position_joueurs(place, liste_joueur, joueur_now))
