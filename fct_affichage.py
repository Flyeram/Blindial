# -*-coding: utf8 -*-

import pygame
from random import *
import os
from pygame.locals import *
import sys
import fonction_Q

###########################

def fct_gagne(fenetre_question, font_title, fond, fenetre_jeu):
    """ Cette fonction affiche un message de victoire et prend en argument :
    La fenetre de question, la police de titre, l'image de fond et la fenetre de jeu"""
    med_joie = pygame.image.load("Images/med_joie.png").convert_alpha()
    partie = pygame.image.load("Images/partie.jpg").convert()
    fenetre_jeu.blit(partie, (0, 372))
    fenetre_question.blit(fond, (0,0))
    texte1 = font_title.render("Bonne réponse !", 1, (255, 255, 255))
    texte2 = font_title.render("Tu peux rejouer", 1, (255, 255, 255))
    fenetre_question.blit(texte1, (330,30))
    fenetre_question.blit(texte2, (330,70))
    fenetre_jeu.blit(med_joie, (30, 400))
    fenetre_jeu.blit(fenetre_question, (260, 260))
    pygame.display.flip()
    lol = fonction_Q.presskey()
    return

def fct_perdu(fenetre_question, font_title, fond, reponse_sous_titre, fenetre_jeu):
    """ Cette fonction affiche un message de victoire et prend en argument :
    La fenetre de question, la police de titre, l'image de fond, les réponses
    et la fenetre de jeu"""
    med_triste = pygame.image.load("Images/med_triste.png").convert_alpha()
    partie = pygame.image.load("Images/partie.jpg").convert()
    fenetre_jeu.blit(partie, (0, 372))
    fenetre_question.blit(fond, (0,0))
    couplet = reponse_sous_titre[5]    
    texte1 = font_title.render("Mauvaise réponse !", 1, (255, 255, 255))
    texte_reponse = "La bonne réponse était {}.".format(couplet[0])
    texte2 = font_title.render(texte_reponse, 1, (255, 255, 255))
    texte3 = font_title.render("Au joueur suivant.", 1, (255, 255, 255))
    fenetre_question.blit(texte1, (330,30))
    fenetre_question.blit(texte2, (150,70))
    fenetre_question.blit(texte3, (330,110))
    fenetre_jeu.blit(med_triste, (30, 400))
    fenetre_jeu.blit(fenetre_question, (260, 260))
    pygame.display.flip()
    lol = fonction_Q.presskey()
    return

def fct_temps(fenetre_question, font_title, fond, reponse_sous_titre, fenetre_jeu):
    """ Cette fonction affiche un message de victoire et prend en argument :
    La fenetre de question, la police de titre, l'image de fond, les réponses
    et la fenetre de jeu"""
    med_triste = pygame.image.load("Images/med_triste.png").convert_alpha()
    partie = pygame.image.load("Images/partie.jpg").convert()
    fenetre_jeu.blit(partie, (0, 372))
    fenetre_question.blit(fond, (0,0))
    couple = reponse_sous_titre[5]
    texte1 = font_title.render("Le temps est écoulé !", 1, (255, 255, 255))
    texte_reponse = "La bonne réponse était {}.".format(couple[0])
    texte2 = font_title.render(texte_reponse, 1, (255, 255, 255))
    texte3 = font_title.render("Au joueur suivant.", 1, (255, 255, 255))
    fenetre_question.blit(texte1, (330,30))
    fenetre_question.blit(texte2, (150,70))
    fenetre_question.blit(texte3, (330,110))
    fenetre_jeu.blit(med_triste, (30, 400))
    fenetre_jeu.blit(fenetre_question, (260, 260))
    pygame.display.flip()
    lol = fonction_Q.presskey()
    return
