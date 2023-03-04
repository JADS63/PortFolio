#########################################
#########################################
import pygame,sys
from pygame.locals import *
import random
import time
pygame.init()
pygame.font.init()
fenetre_jeu=pygame.display.set_mode((450,560))    	# Taille fenêtre du jeu en pixels
pygame.display.set_caption('SpaceInvader')          	# titre de la fenêtre

#############################
# Déclaration des variables #
#############################

Gauche = False
Droite = False
Texty = pygame.font.Font('SUPERPOI_R.TTF', 10)
clock = pygame.time.Clock()
vaisseau = pygame.image.load('vaisseau.png')
etoile_img=pygame.image.load('etoile.png')
rectangle_vaisseau = pygame.Rect(20,500,31,32)
img_aliens=[pygame.image.load('invader1.png'),pygame.image.load('invader2.png')]
aliens=[]
missiles=[]
etoile=[]
laser=[]
missiles_aliens=[]
points=0
affiche_point=""
i=0
lose=0
vitesse=2
tps_tir_alien=random.randint(0,20)
score=0
score1=Texty.render("SCORE :", 0, (0,155,255))
score2=Texty.render(str(score), 0, (0,155,255))
lesniveaux=1
niveau_affiche=0
vie=3
La_vie=Texty.render("nombre de vie :", 0, (0,155,255))
affiche_vie=Texty.render("3", 0, (100,255,100))
niveau2=Texty.render("NIVEAU :", 0, (0,155,255))
niveau1=Texty.render(str(lesniveaux), 0, (0,155,255))
jauge1=Texty.render("..........", 0, (0,155,255))
delimitation=Texty.render(".", 0, (0,155,255))
jauge2=Texty.render(affiche_point, 0, (255,0,0))
SUPER=Texty.render("super pouvoir :", 0, (255,0,0))
#####################################

# Fonction de détection des Touches #
#####################################

def detecte_touches():
    """ Cette fonction permet de détecter les touches enfoncées ou relâchées
    de quitter le jeu ou de permettre le déplacement du vaisseau"""

    global Gauche,Droite
    global points
    global affiche_point

    for event in pygame.event.get():
        if event.type==QUIT:		# Traite l'évènement fermer la fenêtre avec la souris
                pygame.quit()
                sys.exit()
        if event.type== KEYDOWN:	# Traiter les évènements du clavier
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==K_RIGHT:
                Droite = True
            if event.key==K_LEFT:
                Gauche = True
            if event.key== K_SPACE:
                if len(missiles)<=2:
                    missiles.append(pygame.Rect(rectangle_vaisseau.left+12,rectangle_vaisseau.top,9,16))
            if event.key== K_UP:
                if points>=8:
                    laser_vaisseau()
                    affiche_point=""
                    jauge2=Texty.render(affiche_point, 0, (255,0,0))
                    points=0
                    
        if event.type== KEYUP:
            if event.key==K_RIGHT:
                Droite = False
            if event.key==K_LEFT:
                Gauche = False
            
                
        
            
def deplace_missiles():
    """ Cette fonction permet de changer les coordonnées des missiles contenu dans la liste missiles"""
    for missile in missiles:				# pour chaque missiles existant
        missile.top=missile.top-5			# soustraire 10 à la coordonnée du point haut
        pygame.draw.rect(fenetre_jeu,0xF02000,missile)	# dessinner un rectangle de couleur rouge
        if missile.top<=0:				# si le missiles arrive en haut de l'écran
            missiles.remove(missile)
            
def deplace_laser():
    """ Cette fonction permet de changer les coordonnées des missiles contenu dans la liste missiles"""
    for i in laser:				# pour chaque missiles existant
        i.top=i.top-5			# soustraire 10 à la coordonnée du point haut
        pygame.draw.rect(fenetre_jeu,0xF02000,i)	# dessinner un rectangle de couleur rouge
        if i.top<=-200:				# si le missiles arrive en haut de l'écran
            laser.remove(i)

def deplace_missiles_aliens():
    """ Cette fonction permet de changer les coordonnées des missiles contenu dans la liste missiles"""
    for missile in missiles_aliens:				# pour chaque missiles existant
        missile.top=missile.top+5			# soustraire 10 à la coordonnée du point haut
        pygame.draw.rect(fenetre_jeu,0xFFFFFF,missile)	# dessinner un rectangle de couleur rouge
        if missile.top>=600:				# si le missiles arrive en haut de l'écran
            missiles_aliens.remove(missile)
def deplace_etoile():
    for etoiles in etoile:
        etoiles.top=etoiles.top+5
        pygame.draw.rect(fenetre_jeu,0xFFFFFF,etoiles)
        if etoiles.top>=600:				# si le missiles arrive en haut de l'écran
            etoile.remove(etoiles)
def niveau(n):
    global missiles
    global laser
    global missiles_aliens
    global etoile
    """Cette fonction génère des coordonnées de retangles aléatoirement"""
    if n==1:
            for i in range(100,440,50):
                    aliens.append(pygame.Rect(i,random.randint(100,200),31,24))
            missiles=[]
            laser=[]
            missiles_aliens=[]
            for i in range(random.randint(1,5)):
                etoile.append(pygame.Rect(random.randint(100,400),random.randint(100,200),31,24))
            
    elif n==2:
            for i in range(100,420,40):
                    aliens.append(pygame.Rect(i,random.randint(0,300),31,24))
            missiles=[]
            laser=[]
            missiles_aliens=[]
    elif n==3:
            for i in range(100,420,30):
                    aliens.append(pygame.Rect(i,random.randint(100,400),31,24))
            missiles=[]
            laser=[]
            missiles_aliens=[]
    elif n==4:
            for y in range(100,300,50):
                    for x in range(50,400,50):
                            aliens.append(pygame.Rect(x,y,31,24))
            missiles=[]
            laser=[]
            missiles_aliens=[]
    
def detecte_collision():

    global score
    global points
    global affiche_point
    global jauge2
    global score2
    for missile in missiles:
        for alien in aliens:
            if missile.colliderect(alien): 
                aliens.remove(alien)
                missiles.remove(missile)
                score=score+1
                if points<8:
                    points=points+1
                    affiche_point=affiche_point+"."
                    jauge2=Texty.render(affiche_point, 0, (255,0,0))
                else:
                    jauge2=Texty.render(affiche_point, 0, (255,255,0))
                    
                
                score2=Texty.render(str(score), 0, (0,155,255))
    for i in laser:
        for alien in aliens:
            if i.colliderect(alien):
                aliens.remove(alien)
                score=score+1
                score2=Texty.render(str(score), 0, (0,155,255))

def detecte_collision_vaisseau():
    global vie
    global affiche_vie
    global lose
    for missile in missiles_aliens:
            if missile.colliderect(rectangle_vaisseau):
                fenetre_jeu.fill (0xFF0000)
                fenetre_jeu.blit(score1,(50,20))
                fenetre_jeu.blit(score2,(130,20))
                fenetre_jeu.blit(niveau2,(170,20))
                fenetre_jeu.blit(niveau1,(250,20))
                fenetre_jeu.blit(jauge1,(390,10))
                fenetre_jeu.blit(jauge2,(393,14))
                fenetre_jeu.blit(delimitation,(390,14))
                fenetre_jeu.blit(delimitation,(426,14))
                fenetre_jeu.blit(jauge1,(390,18))
                fenetre_jeu.blit(SUPER,(280,6))
                fenetre_jeu.blit(vaisseau,rectangle_vaisseau)
                vie=vie-1
                affiche_vie=Texty.render(str(vie), 0, (100,255,100))
                missiles_aliens.remove(missile)
                    
                

def detecte_collision_etoile():
    global vie
    global affiche_vie
    global lose
    for etoiles in etoile:
            if etoiles.colliderect(rectangle_vaisseau):
                etoile.remove(etoiles)              
                            

def placer_aliens(image):
    time.sleep(5)
    for alien in aliens:
        fenetre_jeu.blit(image,alien)
def placer_etoile(image):
    for etoiles in etoile:
        fenetre_jeu.blit(image,etoiles)

def deplace_aliens(x,y):
	for alien in aliens:
		alien.left += x
		alien.top += y

def change_sens_aliens():
    global vitesse
    for alien in aliens:
        if alien.right>450 or alien.left<0:
            vitesse=-vitesse
            deplace_aliens(0,5)
        
                   
def ajouter_tir_alien():
    global tps_tir_alien
    if tps_tir_alien==20:
        choix=random.choice(aliens)
        missiles_aliens.append(pygame.Rect(choix.left+12,choix.bottom,3,16))
    tps_tir_alien=random.randint(0,20)
    
def laser_vaisseau():
    global affiche_points
    global jauge2
    affiche_point=""
    jauge2=Texty.render(affiche_point, 0, (255,0,0))
    laser.append(pygame.Rect(rectangle_vaisseau.left-35,rectangle_vaisseau.top-130,100,150))
   
#####################
# BOUCLE PRINCIPALE #
#####################
placer_etoile(etoile_img)
while vie!=0:
    
    
    fenetre_jeu.fill (0x00001A)		
    fenetre_jeu.blit(score1,(20,20))
    fenetre_jeu.blit(score2,(100,20))
    fenetre_jeu.blit(niveau2,(130,20))
    
    fenetre_jeu.blit(niveau1,(210,20))
    fenetre_jeu.blit(jauge1,(375,12))
    fenetre_jeu.blit(jauge2,(378,16))
    fenetre_jeu.blit(delimitation,(375,16))
    fenetre_jeu.blit(delimitation,(411,16))
    fenetre_jeu.blit(jauge1,(375,20))
    fenetre_jeu.blit(SUPER,(230,20))
    fenetre_jeu.blit(La_vie,(20,50))
    fenetre_jeu.blit(affiche_vie,(180,50))
    fenetre_jeu.blit(vaisseau,rectangle_vaisseau)

    detecte_touches()
    ajouter_tir_alien()
    
    

    # Déplacement du vaisseau d'un pixel 
    if Gauche and rectangle_vaisseau.left > 10 : rectangle_vaisseau.left -= 5
    if Droite and rectangle_vaisseau.right < 440 : rectangle_vaisseau.right += 5
    deplace_aliens(vitesse,0)
    deplace_missiles()
    deplace_etoile()
    deplace_laser()
    deplace_missiles_aliens()
    if lesniveaux==1:
        if len(aliens)==0:
            niveau(1)
            niveau1=Texty.render(str(lesniveaux), 0, (0,155,255))
            lesniveaux=2
    elif lesniveaux==2:
        if len(aliens)==0:
            niveau(2)
            niveau1=Texty.render(str(lesniveaux), 0, (0,155,255))
            lesniveaux=3
    elif lesniveaux==3:
        if len(aliens)==0:
            niveau(3)
            niveau1=Texty.render(str(lesniveaux), 0, (0,155,255))
            lesniveaux=4
    elif lesniveaux==4:
        if len(aliens)==0:
            niveau(4)
            niveau1=Texty.render(str(lesniveaux), 0, (0,155,255))
    i+=1
    placer_aliens(img_aliens[(i//15)%2])
    detecte_collision()
    detecte_collision_vaisseau()
    detecte_collision_etoile()
    change_sens_aliens()
    pygame.display.update()				# rafraichir l'affichage de la fenêtre jeu  
    clock.tick(60)					# Vitesse du jeu : 30 FPS

for alien in aliens:
    aliens.remove(alien)
for missile in missiles_aliens:
    missiles_aliens.remove(missile)
for missile in missiles:
    missiles.remove(missile)


fenetre_jeu.fill (0x00001A)		# Remplir l'arrieère plan avec la couleur RVB Bleu foncé
fenetre_jeu.blit(score1,(50,20))
fenetre_jeu.blit(score2,(130,20))
fenetre_jeu.blit(niveau2,(170,20))
fenetre_jeu.blit(niveau1,(250,20))
fenetre_jeu.blit(jauge1,(390,10))
fenetre_jeu.blit(jauge2,(394,14))
fenetre_jeu.blit(delimitation,(390,14))
fenetre_jeu.blit(delimitation,(426,14))
fenetre_jeu.blit(jauge1,(390,18))
fenetre_jeu.blit(SUPER,(280,6))
fenetre_jeu.blit(vaisseau,rectangle_vaisseau)
lose=Texty.render("Vous avez perdu...", 0, (100,255,100))
fenetre_jeu.blit(lose,(130,250))


