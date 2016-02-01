# -*-coding: utf8 -*-
import pygame
from random import *
import os
from pygame.locals import *
import sys
from fonction_Q import *
from fct_affichage import *

###########################

#Fonction affichant les réponses
def fct_rect(reponses, sous_titre, fenetre_question):
    """ Fonction affichant les réponses, renvoie surface, rect, pos_surface"""
    tuple_blit = []
    tuple_rect = []
    liste_tuple = [[(270, 400), (20, 150)], [(520, 400),(270, 150)], [(770, 400), (530, 150)], [(270, 350), (20, 100)], [(520, 350), (270, 100)], [(770, 350), (530, 100)]]
    shuffle(liste_tuple)
    for i in range(6):
        couple = liste_tuple[i]
        tuple_blit.append(couple[1])
        tuple_rect.append(couple[0])

    surface = list(range(6))
    rect = list(range(6))
    rect2 = list(range(6))
    pos_surface = list(range(6))
    for i in range(6):
        #On défini une couleur comme transparente
        surface[i] = pygame.Surface((230, 40))
        surface[i].set_colorkey((0, 0, 0))
        surface[i].fill((0, 0, 0))
        #On creer un rectangle a partir du texte des réponses
        rect[i] = reponses[i].get_rect()
        rect[i].topleft = (0, 0)
        rect2[i] = sous_titre[i].get_rect()
        rect2[i].topleft = (0, 20)
        surface[i].blit(reponses[i], rect[i])
        surface[i].blit(sous_titre[i], rect2[i])
        pos_surface[i] = surface[i].get_rect()
        pos_surface[i].topleft = tuple_rect[i]
        fenetre_question.blit(surface[i], tuple_blit[i])

    return pos_surface


def rect_menu_joueurs(texte_joueur, fenetre_jeu):
    """ Fonction qui créer les rectangle du texte nombre de joueur et les renvoies """
    rect_menu_joueur = list(range(4))
    pos_text = [(300,300),(300,400),(300,500),(300,600)]

    for i in range(4):
        #On créer les rectangles pour le nombre de joueurs
        rect_menu_joueur[i] = texte_joueur[i].get_rect()
        rect_menu_joueur[i].topleft = pos_text[i]
        fenetre_jeu.blit(texte_joueur[i], pos_text[i])
    return rect_menu_joueur
