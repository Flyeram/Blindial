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
###########################

#largeur fond/plateau(cotés) = 314 px
#largeur fond/plateau(haut) = 33 px
#taille plateau(cotés)/case = 22 px
#Taille plateau(haut)/case = 23 px
#Espace entre case = 6 px
#Taille case = 61x61 px
#nombre case = 45


def rect_cases():
    taille = (61, 61)
    liste_case = []

    for y in range(9):

        for x in range(9):

            if  x % 4 == 0 or  y % 4 == 0 :
                liste_case.append(pygame.rect.Rect(337 + (68 * x), 57 + (68 * y), 62, 62))



    cases_vertes = [liste_case[5], liste_case[11], liste_case[16], liste_case[24], liste_case[27], liste_case[32], liste_case[34], liste_case[37]]
    cases_oranges = [liste_case[7], liste_case[10], liste_case[12], liste_case[17], liste_case[20], liste_case[28], liste_case[33], liste_case[39]]
    cases_jaunes = [liste_case[1], liste_case[6], liste_case[13], liste_case[15], liste_case[21], liste_case[25], liste_case[35], liste_case[41]]
    cases_rouges = [liste_case[3], liste_case[9], liste_case[19], liste_case[23], liste_case[29], liste_case[31], liste_case[38], liste_case[43]]
    cases_rejouer = [liste_case[4], liste_case[18], liste_case[22], liste_case[26], liste_case[40]]
    cases_mediator = [liste_case[0], liste_case[8], liste_case[36], liste_case[44]]
    cases_depla = [liste_case[2], liste_case[14], liste_case[30], liste_case[42]]

    return cases_vertes, cases_oranges, cases_jaunes, cases_rouges, cases_rejouer, cases_mediator, cases_depla, liste_case



if __name__ == "__main__":
    pygame.init()
    print(rect_cases())
