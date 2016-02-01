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
from Menu import *
from plateau_fct import *
from affichage_joueurs import *

###########################

#Le lanceur du jeu

lancer = True
while lancer:
    lancer = menu()
pygame.quit()
