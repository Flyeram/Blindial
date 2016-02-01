# -*-coding: utf8 -*-

#(c) Grégoire de Massé

import pygame
from random import *
from pygame.locals import *
from fonction_Q import *
from fct_affichage import *
from fct_rect import *
from fct_texte import *
from rect_cases import *
from random import choice
import pygame.gfxdraw
###########################

def animation_de(fenetre_jeu):
    image_de = ['Images/De1.png', 'Images/De2.png',
                'Images/De3.png', 'Images/De4.png']
    for i in range(10):
        de_face = randint(1,4)
        surface_de = pygame.image.load(image_de[de_face-1]).convert_alpha()
        fenetre_jeu.blit(surface_de, (1100, 100))
        pygame.display.flip()
        pygame.time.wait(200)

def lancer_de():
    
    image_de = ['Images/De1.png', 'Images/De2.png',
                'Images/De3.png', 'Images/De4.png']    
    
    de_point = randint(1, 4)  
    surface_de = pygame.image.load(image_de[de_point-1]).convert_alpha()
    
    
    return de_point, surface_de

def verif_case(pos_player, de, liste_case):
    """renvoie la liste des cases ou le joueur peut aller"""

    cases_possibles = []
            
    for n in range(-de, de+1):
        for c in liste_case:
            #si les pos x et y sont a 'de' cases de distance
            if c.x == pos_player[0] + (n*68) and\
            (c.y == pos_player[1] + ((abs(n)-de)*68) or c.y == pos_player[1] + ((abs(n)-de)*-68)):
                #on ajoute la case aux cases possibles
                cases_possibles.append(c)
        
    if de == 4:
        #on enleve les cases a 4 de distance qu'on ne peut pas atteindre sans tricher
        #c.a.d sans passer par des cases qui n'existent pas
        if  not(pygame.rect.Rect(pos_player[0] + 68, pos_player[1], 62, 62) in liste_case
                or pygame.rect.Rect(pos_player[0] - 68, pos_player[1], 62, 62) in liste_case) :
            #si il n'y a pas de cases a droite ou a gauche du joueur
            for c in cases_possibles[:]:
                if (pygame.rect.Rect(pos_player[0] + 4*68, pos_player[1], 62, 62) == c
                or pygame.rect.Rect(pos_player[0] - 4*68, pos_player[1], 62, 62) == c):
                    #on supprime de la liste les cases a 4 de distance en ligne droite
                    cases_possibles.remove(c)

        #on fait la meme chose pour les coordonnes en y
        elif  not(pygame.rect.Rect(pos_player[0], pos_player[1] + 68, 62, 62) in liste_case
                or pygame.rect.Rect(pos_player[0], pos_player[1] - 68, 62, 62) in liste_case) :
            #si il n'y a pas de cases au dessus ou en dessous du joueur
            
            for d in cases_possibles[:]:
                if (pygame.rect.Rect(pos_player[0], pos_player[1] - 4*68, 62, 62) == d                    
                or pygame.rect.Rect(pos_player[0], pos_player[1] + 4*68, 62, 62) == d):
                    #on supprime de la liste les cases a 4 de distance en ligne droite
                    cases_possibles.remove(d)
            
    return cases_possibles

def contour(cases_possibles, joueur, fenetre_jeu):
    j = pygame.surface.Surface((62, 62))
    j.fill((0, 0, 0))
    j.set_colorkey((0,0,0))
    pygame.gfxdraw.rectangle(j, (0,0, 62, 62), (0, 255, 0))
    fenetre_jeu.blit(j, joueur)
    
    for c in cases_possibles :
        s = pygame.surface.Surface((62, 62))
        s.fill((0, 0, 0))
        s.set_colorkey((0,0,0))
        pygame.gfxdraw.rectangle(s, (0,0, 62, 62), (1, 0, 0))
        fenetre_jeu.blit(s, c.topleft)


if __name__ == '__main__':
    import pygame
    import pygame.gfxdraw
    from pygame.locals import *
    
    pygame.init()
    fenetre_jeu = pygame.display.set_mode((1280, 720))
    fond = pygame.image.load('Images/flygame.jpg')
    fenetre_jeu.blit(fond, (0,0))

    def test(fenetre_jeu, fond):
        
        a, b, c, d, e, f, r, liste_case = rect_cases()
        joueur = choice(liste_case)
        
        print(joueur)
        de, surf = lancer_de()
        print(de)
        cases_possibles = verif_case(joueur, 4, liste_case)
        print(cases_possibles)

        fenetre_jeu.blit(fond, (0,0))
        
        contour(cases_possibles, joueur, fenetre_jeu)


    run = True
    while run :
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    test(fenetre_jeu, fond)
        pygame.display.flip()       
    pygame.quit()
        

    
