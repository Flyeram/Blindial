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

###########################

def sous_titre(liste_reponse):
    reponse_sous_titre = []
    for i in range(6):
        if "_" not in liste_reponse[i]:
            reponse_sous_titre.append([liste_reponse[i], " "])
        else:
            reponse_sous_titre.append(liste_reponse[i].split("_"))
    return reponse_sous_titre

def reponse_liste_fct(reponse_sous_titre, font_reponse):
    reponses = list(range(6))
    sous_titre = list(range(6))
    for ind in range(6):
        couple = reponse_sous_titre[ind]
        reponses[ind] = font_reponse.render(couple[0], 1, (255, 255, 255))
        sous_titre[ind] = font_reponse.render(couple[1], 1, (255, 255, 255))

    return reponses, sous_titre
