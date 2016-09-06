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

import pygame
from pygame.locals import *
import plateau_fct

def entreNoms(fenetre_jeu, fond, joueurs):
        font = pygame.font.Font("Polices/appleberry.ttf", 60)
        noms = ['']*joueurs
        jeu = True

        for i in range(joueurs) :
                titre = font.render('Joueur {}'.format(i+1), 1,((255, 255, 255)))
                fenetre_jeu.blit(fond, (0, 0))
                texte_change = font.render('Quel est ton nom ?', 1,((255, 255, 255)))
                nom, jeu, cont = inputName(font, fenetre_jeu, fond, titre, texte_change)
                if cont == False:
                        break
                noms[i] = nom
        if cont == True:
                jeu = plateau_fct.fct_plateau(joueurs, fenetre_jeu, noms)
        return False, jeu

def inputName(font, fenetre_jeu, fond, titre, texte_change):
        jeu = True
        nom = ''
        run = True
        cont = True
        pygame.key.set_repeat(400, 30)
        while run:

                for event in pygame.event.get():
                        if event.type == QUIT :
                                jeu = False
                                run = False
                                cont = False
                        if event.type == KEYDOWN:
                                if event.key == K_RETURN:
                                        if len(nom) > 0:
                                                run = False
                                elif event.key == K_ESCAPE:
                                        jeu = True
                                        run = False
                                        cont = False
                                elif event.key == K_BACKSPACE:
                                        nom = nom [:-1]
                                else :
                                        if len(nom)<7:
                                                nom += event.unicode

                fenetre_jeu.blit(fond, (0, 0))
                fenetre_jeu.blit(texte_change, (400, 300))
                fenetre_jeu.blit(titre, (600, 50))
                fenetre_jeu.blit(font.render('Nom : {}'.format(nom), 1, ((255, 255, 255))), (400, 350))


                pygame.display.flip()

        return nom, jeu, cont

if __name__ == '__main__':
     pygame.init()
     fenetre_jeu = pygame.display.set_mode((1280, 720))


     fond = pygame.image.load("Images/fond.jpg").convert()
     rep = entreNoms(fenetre_jeu, fond, 2)
     print(rep)
     pygame.quit()
