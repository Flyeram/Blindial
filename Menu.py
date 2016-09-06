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

###########################

def affichage_Menu(titre, play, regles, credit, quitter, fenetre_jeu, fond):
            fenetre_jeu.blit(fond, (0, 0))
            fenetre_jeu.blit(titre, (550, 50))
            fenetre_jeu.blit(play, (450, 300))
            fenetre_jeu.blit(regles, (450, 380))
            fenetre_jeu.blit(credit, (680, 380))
            fenetre_jeu.blit(quitter, (650, 300))
            pygame.display.flip()

def menu():
    continuer = True
    jeu = True
    while jeu:
        continuer = True
        pygame.init()
        fenetre_jeu = pygame.display.set_mode((1280, 720))
        icon_32x32 = pygame.image.load("Images/Icone.png")
        pygame.display.set_icon(icon_32x32)
        pygame.display.set_caption('Trivial','Images/mediator.png')
        fond = pygame.image.load("Images/fond.jpg").convert()
        fenetre_jeu.blit(fond, (0, 0))
        font_menu = pygame.font.Font("Polices/appleberry.ttf", 70)
        titre = font_menu.render("Menu", 1, (255, 255, 255))
        play = font_menu.render("Jouer", 1, (255, 255, 255))
        regles = font_menu.render("Règles", 1, (255, 255, 255))
        credit = font_menu.render("Crédits", 1, (255, 255, 255))
        quitter = font_menu.render("Quitter", 1, (255, 255, 255))
        phrase_joueur = ["1 joueur", "2 joueurs", "3 joueurs", "4 joueurs"]
        texte_joueur = []
        for i in range(4):
            boucle = font_menu.render(phrase_joueur[i], 1, (255, 255, 255))
            texte_joueur.append(boucle)

        rect_play = play.get_rect()
        rect_play.topleft = (450, 300)
        rect_quitter = quitter.get_rect()
        rect_quitter.topleft = (650, 300)
        rect_regles = regles.get_rect()
        rect_regles.topleft = (450, 380)
        rect_credit = credit.get_rect()
        rect_credit.topleft = (680, 380)
        test = 1

        while continuer == True:
            affichage_Menu(titre, play, regles, credit, quitter, fenetre_jeu, fond)

            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT:
                    continuer = False
                    jeu = False
                elif event.type == QUIT:
                    continuer = False
                    jeu = False
                elif event.type == MOUSEBUTTONDOWN and event.button ==1:
                    mouse_position = pygame.mouse.get_pos()
                    if rect_play.collidepoint(mouse_position):
                        continuer, jeu = affichage_joueurs(fenetre_jeu, texte_joueur, fond, titre, quitter, rect_quitter)
                    elif rect_quitter.collidepoint(mouse_position):
                        continuer = False
                        jeu = False
                    elif rect_regles.collidepoint(mouse_position):
                        regle_nb = randint(1, 10)
                        if regle_nb == 10:
                            image_regles = pygame.image.load("Images/Regles_1.jpg")
                            fenetre_jeu.blit(image_regles, (0, 0))
                        else:
                            image_regles = pygame.image.load("Images/Regles_0.jpg")
                            fenetre_jeu.blit(image_regles, (0, 0))
                        pygame.display.flip()
                        presskey()
                    elif rect_credit.collidepoint(mouse_position):
                        image_credit = pygame.image.load("Images/Credit.png")
                        fenetre_jeu.blit(image_credit, (0, 0))
                        pygame.display.flip()
                        presskey()
            pygame.display.flip()



    return False



if __name__ == "__main__":
    res = True
    while res:
        res = menu()
    pygame.quit()
