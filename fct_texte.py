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
