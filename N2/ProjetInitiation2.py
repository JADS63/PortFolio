#------------------------------------------------------------------------#
#---------------------------Bibliotèques---------------------------------#
#------------------------------------------------------------------------#
import turtle
from turtle import*
from random import *
from tkinter import*
#------------------------------------------------------------------------#
#-----------------------------Fonctions----------------------------------#
#------------------------------------------------------------------------#
screen = Screen()  #set size
screen.setup(width = 1.0, height = 1.0)  
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
hideturtle()
def interface():
    global cac# cac est une variable qui permet de savoir quand les jeux sont finis
    if cac==1:
        cac=0
        clear()
        turtle.bgpic("imagevrai.png")
        z=1
        c=0
        while z!=0:
            c=textinput("LETTRE","A quel jeu voulez-vous jouer??")
            if c=="1" or c=="2" or c=="3":
                z=0
        c=int(c)
        turtle.bgpic("image1.png")
        programme(c)
#-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
#---------------------------------Fonctions_Puissance4------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
def GrilleVide():
    return[["." for colonne in range(7)]for ligne in range(6)]
def dessin_grille():                    #dessine une grille
    penup()
    seth(0)
    goto(-350,-300)
    speed(0)
    pensize(5)
    pendown()
    for i in range(2):
        forward(700)
        left(90)
        forward(600)
        left(90)
    for k in range(3):
        forward(100)
        left(90)
        forward(600)
        right(90)
        forward(100)
        right(90)
        forward(600)
        left(90)
    forward(100)
    left(90)
    for k in range(3):
        forward(100)
        left(90)
        forward(700)
        right(90)
        forward(100)
        right(90)
        forward(700)
        left(90)
    
        
#---------------------------------------------------------------------------------------------------------------------------#
def yposition(Grille,colonne):#permet de déterminer ou la tortue a besoin de dessiner
    for i in range(6):
        if Grille[5-i][colonne]== ".":
            y=-250+i*100
            return y
#---------------------------------------------------------------------------------------------------------------------------#


def CoupPossible(Grille,Colone):#regarde si c'est possible de jouer dans cette colonne
    if Grille[0][Colone]== ".":
        return True
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------------#

def Jouer(Grille,Joueur,Colone):#fonction qui change la valeur dans la Grille
    Ligne=5
    if CoupPossible(Grille,Colone)== True:
        while Ligne>=0 :
            if Grille[Ligne][Colone]!=".":
                Ligne=Ligne-1
            else:
                if Joueur==1:
                    Grille[Ligne][Colone]=0
                elif Joueur==2:
                    Grille[Ligne][Colone]=1
                Ligne=-1
#---------------------------------------------------------------------------------------------------------------------------#

def Horiz(Grille,Joueur):#regarde un alignement possible horizontalement
    for Ligne in range(6):
        for Colonne in range(7-3):
            if Joueur==1:
                if Grille[Ligne][Colonne]==0 and Grille[Ligne][Colonne+1]==0 and Grille[Ligne][Colonne+2]==0 and Grille[Ligne][Colonne+3]==0:
                    return True
            if Joueur==2:
                if Grille[Ligne][Colonne]==1 and Grille[Ligne][Colonne+1]==1 and Grille[Ligne][Colonne+2]==1 and Grille[Ligne][Colonne+3]==1:
                    return True
#---------------------------------------------------------------------------------------------------------------------------#

def Vert(Grille,Joueur):#regarde un alignement possible verticalement
    for Ligne in range(6-3):
        for Colonne in range(7):
            if Joueur==1:
                if Grille[Ligne][Colonne]==0 and Grille[Ligne+1][Colonne]==0 and Grille[Ligne+2][Colonne]==0 and Grille[Ligne+3][Colonne]==0:
                    return True
            if Joueur==2:
                if Grille[Ligne][Colonne]==1 and Grille[Ligne+1][Colonne]==1 and Grille[Ligne+2][Colonne]==1 and Grille[Ligne+3][Colonne]==1:
                    return True
###---------------------------------------------------------------------------------------------------------------------------#

def DiagBas(Grille,Joueur):#regarde un alignement possible a la diagonale bas
    if Joueur==1:
        for Ligne in range(3):
            for Colonne in range(4):
                if Grille[5-Ligne][Colonne+0]==0 and Grille[4-Ligne][Colonne+1]==0 and Grille[3-Ligne][Colonne+2]==0 and Grille[2-Ligne][Colonne+3]==0:
                    return True
    if Joueur==2:
        for Ligne in range(3):
            for Colonne in range(4):
                if Grille[5-Ligne][Colonne+0]==1 and Grille[4-Ligne][Colonne+1]==1 and Grille[3-Ligne][Colonne+2]==1 and Grille[2-Ligne][Colonne+3]==1:
                    return True
#---------------------------------------------------------------------------------------------------------------------------#

def DiagHaut(Grille,Joueur):#regarde un alignement possible a la diagonale haut
    if Joueur==1:
        for Ligne in range(3):
            for Colonne in range(4):
                if Grille[0+Ligne][Colonne+0]==0 and Grille[1+Ligne][Colonne+1]==0 and Grille[2+Ligne][Colonne+2]==0 and Grille[3+Ligne][Colonne+3]==0:
                    return True
    if Joueur==2:
        for Ligne in range(3):
            for Colonne in range(4):
                if Grille[0+Ligne][Colonne+0]==1 and Grille[1+Ligne][Colonne+1]==1 and Grille[2+Ligne][Colonne+2]==1 and Grille[3+Ligne][Colonne+3]==1:
                    return True
#---------------------------------------------------------------------------------------------------------------------------#

def Victoire(Grille,Joueur):#fonction qui détermine si il y a victoire
    if Horiz(Grille,Joueur)==True or Vert(Grille,Joueur)== True or DiagBas(Grille,Joueur)==True or DiagHaut(Grille,Joueur)==True:
        global cac
        cac=1
        penup()
        goto(-150,300)
        if Joueur==1:
            phrase_vic="Le joueur bleu a gagné"
        else:
            phrase_vic="Le joueur rouge a gagné"
        write(phrase_vic,move=False, align="left", font=("Times New Roman", 20, "normal"))
        penup()
        seth(0)
        goto(-950,100)
        pendown()
        write("Appuyez sur la touche Up pour recommencer le jeu ",move=False, align="left", font=("Times New Roman", 15, "normal"))
        penup()
        seth(0)
        goto(-950,-100)
        pendown()
        write("Appuyez sur la touche Down pour changer de jeu ",move=False, align="left", font=("Times New Roman", 15, "normal"))
        return True
#---------------------------------------------------------------------------------------------------------------------------#

def MatchNul(Grille):#fonction qui détermine si il y a un match nul
    Nbr_col_non_Vide=0
    for Colonne in range(7):
        if Grille[0][Colonne]!=".":
            Nbr_col_non_Vide=Nbr_col_non_Vide+1
    if Nbr_col_non_Vide==7:
        penup()
        goto(-150,300)
        write("match nul ",font=("Arial", 40, "normal"))
        global cac
        cac=1
        penup()
        seth(0)
        goto(-950,100)
        pendown()
        write("Appuyez sur la touche Up pour recommencer le jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
        penup()
        seth(0)
        goto(-950,-100)
        pendown()
        write("Appuyez sur la touche Down pour changer de jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
        return True
    else:
        return False
###---------------------------------------------------------------------------------------------------------------------------#

tab=[0]
def rond(j):#dessine un rond de couleur en fonction du joueur
    if j==1:
        penup()
        right(90)
        forward(40)
        left(90)
        pendown()
        fillcolor("blue")
        begin_fill()
        circle(40)
        end_fill()
    if j==2:
        penup()
        right(90)
        forward(40)
        left(90)
        pendown()
        fillcolor("red")
        begin_fill()
        circle(40)
        end_fill()
def puissance(x,y):
    global result
    result=0
    if tab[0]==0:#ceci permet d'alterner le joueur 
        j=1
        tab[0]=1
    else:
        j=2
        tab[0]=0
    if x < -250 and x > -350  and  y > -300 and y < 300:#on regarde si le click se trouve dans une colonne
        if CoupPossible(Grille,0)==True:#on regarde si la colonne est vide
            penup()
            goto(-300,yposition(Grille,0))#on dessine une forme en ce point avec un appel de fonction
            pendown()
            rond(j)
            Jouer(Grille,j,0)#on ajoute a la grille la valeur de j
            if Victoire(Grille,j)==True:#on regarde si  il y a victoire
                turtle.onscreenclick(None)
                result=1#l'utilisateur ne peut plus cliquer
            elif MatchNul(Grille)==True:#on regarde si il y a match nul
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
            #idem pour les 7 autres conditions
            
            
    elif x < -150 and x > -250  and  y > -300 and y < 300:
        if CoupPossible(Grille,1)==True:
            penup()
            goto(-200,yposition(Grille,1))
            pendown()
            rond(j)
            Jouer(Grille,j,1)
            if Victoire(Grille,j)==True:#on regarde si  il y a victoire
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
            elif MatchNul(Grille)==True:#on regarde si il y a match nul
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
    elif x < -50 and x > -150  and  y > -300 and y < 300:
        if CoupPossible(Grille,2)==True:
            penup()
            goto(-100,yposition(Grille,2))
            pendown()
            rond(j)
            Jouer(Grille,j,2)
            if Victoire(Grille,j)==True:#on regarde si  il y a victoire
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
            elif MatchNul(Grille)==True:#on regarde si il y a match nul
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
    elif x < 50 and x > -50  and  y > -300 and y < 300:
        if CoupPossible(Grille,3)==True:
            penup()
            goto(0,yposition(Grille,3))
            pendown()
            rond(j)
            Jouer(Grille,j,3)
            if Victoire(Grille,j)==True:#on regarde si  il y a victoire
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
            elif MatchNul(Grille)==True:#on regarde si il y a match nul
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
    elif x < 150 and x > 50  and  y > -300 and y < 300:
        if CoupPossible(Grille,4)==True:
            penup()
            goto(100,yposition(Grille,4))
            pendown()
            rond(j)
            Jouer(Grille,j,4)
            if Victoire(Grille,j)==True:#on regarde si  il y a victoire
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
            elif MatchNul(Grille)==True:#on regarde si il y a match nul
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
    elif x < 250 and x > 150  and  y > -300 and y < 300:
        if CoupPossible(Grille,5)==True:
            penup()
            goto(200,yposition(Grille,5))
            pendown()
            rond(j)
            Jouer(Grille,j,5)
            if Victoire(Grille,j)==True:#on regarde si  il y a victoire
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
            elif MatchNul(Grille)==True:#on regarde si il y a match nul
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
    elif x < 350 and x > 250  and  y > -300 and y < 300:
        if CoupPossible(Grille,6)==True:
            penup()
            goto(300,yposition(Grille,6))
            pendown()
            rond(j)
            Jouer(Grille,j,6)
            if Victoire(Grille,j)==True:#on regarde si  il y a victoire
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
            elif MatchNul(Grille)==True:#on regarde si il y a match nul
                turtle.onscreenclick(None)#l'utilisateur ne peut plus cliquer
                result=1
    else:
        if tab[0]==0:#ceci permet de rester sur le même joueur quand il écris à coté 
            tab[0]=1
        else:
            tab[0]=0

def reset1():# cette fonction permet quand elle est appellée de rénitialisé le jeu
    global result #global sert a changer une variable dans tout le programme pas que dans la fonction
    if result==1:
        clear()
        
        global Grille
        Grille=GrilleVide()
        dessin_grille()
        penup()
        goto(-350,-300)
        pendown()
        global tab
        tab=[0]
        turtle.onscreenclick(puissance)
#-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
#-------------------------------------Fonctions_Pendu-------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------#
def lettre(le,long):  #Pour écrire chaque lettres   
    if le=="a":#-------------------------------------A-------------------------------------#
        seth(90)
        pendown()
        right(20)
        forward(35*long)
        right(135)
        forward(35*long)
        backward(13*long)
        left(245)
        forward(16*long)
        penup()
    elif le=="b":#-------------------------------------B-------------------------------------#
        seth(0)
        pendown()
        forward(16*long)
        circle(8*long,180)
        forward(15*long)
        left(180)
        forward(15*long)
        circle(8*long,180)
        forward(16*long)
        left(90)
        forward(30*long)
        penup()
    elif le=="c":#-------------------------------------C-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        forward(5*long)
        right(180)
        circle(15*long,180)
        forward(3*long)
        penup()
    elif le=="d":#-------------------------------------D-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        right(90)
        forward(30*long)
        right(-90)
        circle(15*long,180)
        penup()
    elif le=="e":#-------------------------------------E-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        forward(15*long)
        backward(15*long)
        right(90)
        forward(15*long)
        left(90)
        forward(15*long)
        backward(15*long)
        right(90)
        forward(15*long)
        left(90)
        forward(15*long)
        penup()
    elif le=="f":#-------------------------------------F-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        forward(15*long)
        backward(15*long)
        right(90)
        forward(15*long)
        left(90)
        forward(15*long)
        backward(15*long)
        right(90)
        forward(15*long)
        penup()
    elif le=="g":#-------------------------------------G-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        forward(10*long)
        seth(0)
        pendown()
        right(180)
        circle(15*long,180)
        left(90)
        forward(12*long)
        right(90)
        forward(10*long)
        penup()
    elif le=="h":#-------------------------------------H-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        right(90)
        forward(30*long)
        backward(15*long)
        left(90)
        forward(15*long)
        left(90)
        forward(15*long)
        backward(30*long)
        penup()
    elif le=="i":#-------------------------------------I-------------------------------------#
        seth(0)
        penup()
        forward(10*long)
        seth(90)
        forward(25*long)
        seth(0)
        pendown()
        pendown()
        circle(5*long)
        right(90)
        forward(25*long)
        penup()
    elif le=="j":#-------------------------------------J-------------------------------------#
        seth(0)
        penup()
        forward(18*long)
        seth(90)
        forward(27*long)
        seth(0)
        pendown()
        forward(4*long)
        right(90)
        forward(20*long)
        circle(-10*long,180)
        penup()
    elif le=="k":#-------------------------------------K-------------------------------------#
        seth(90)
        pendown()
        forward(30*long)
        backward(15*long)
        right(45)
        forward(22*long)
        backward(22*long)
        right(90)
        forward(22*long)
        penup()
    elif le=="l":#-------------------------------------L-------------------------------------#
        seth(90)
        pendown()
        forward(30*long)
        backward(30*long)
        right(90)
        forward(20*long)
        penup()
    elif le=="m":#-------------------------------------M-------------------------------------#
        seth(90)
        pendown()
        forward(30*long)
        right(135)
        forward(15*long)
        left(90)
        forward(15*long)
        right(135)
        forward(30*long)
        penup()
    elif le=="n":#-------------------------------------N-------------------------------------#
        seth(90)
        pendown()
        forward(30*long)
        right(150)
        forward(35*long)
        left(150)
        forward(30*long)
        penup()
    elif le=="o":#-------------------------------------O-------------------------------------#
        seth(90)
        penup()
        forward(15*long)
        seth(270)
        pendown()
        circle(15*long)
        penup()
    elif le=="p":#-------------------------------------P-------------------------------------#
        seth(90)
        pendown()
        forward(30*long)
        backward(5*long)
        seth(270)
        circle(10*long)
        penup()
    elif le=="q":#-------------------------------------Q-------------------------------------#
        penup()
        seth(90)
        forward(15*long)
        seth(270)
        pendown()
        circle(16*long)
        penup()
        seth(90)
        backward(5*long)
        right(90)
        forward(14*long)
        pendown()
        left(320)
        forward(20*long)
        penup()
    elif le=="r":#-------------------------------------R-------------------------------------#
        seth(90)
        pendown()
        forward(30*long)
        backward(5*long)
        seth(270)
        circle(10*long)
        forward(8)
        left(35)
        forward(25*long)
        penup()
    elif le=="s":#-------------------------------------S-------------------------------------#
        seth(0)
        pendown()
        forward(5*long)
        circle(8*long,180)
        circle(-8*long,190)
        forward(5*long)
        penup()
    elif le=="t":#-------------------------------------T-------------------------------------#
        seth(0)
        penup()
        forward(15*long)
        pendown()
        seth(90)
        forward(30*long)
        left(90)
        forward(15*long)
        backward(30*long)
        penup()
    elif le=="u":#-------------------------------------U-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        right(90)
        forward(20*long)
        circle(10*long,180)
        forward(21*long)
        penup()
    elif le=="v":#-------------------------------------V-------------------------------------#
        seth(90)
        penup()
        forward(28*long)
        seth(0)
        pendown()
        right(65)
        forward(30*long)
        left(130)
        forward(31*long)
        penup()
    elif le=="w":#-------------------------------------W-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        right(75)
        forward(30*long)
        left(150)
        forward(30*long)
        right(150)
        forward(30*long)
        left(150)
        forward(30*long)
        penup()
    elif le=="x":#-------------------------------------X-------------------------------------#
        seth(90)
        penup()
        forward(25*long)
        seth(0)
        pendown()
        right(45)
        forward(30*long)
        backward(15*long)
        right(85)
        forward(15*long)
        backward(30*long)
        penup()
    elif le=="y":#-------------------------------------Y-------------------------------------#
        seth(90)
        penup()
        forward(30*long)
        seth(0)
        pendown()
        right(65)
        forward(15*long)
        left(130)
        forward(15*long)
        backward(15*long)
        left(25)
        backward(15*long)
        penup()
    elif le=="z":#-------------------------------------Z-------------------------------------#
        seth(90)
        penup()
        forward(25*long)
        seth(0)
        pendown()
        forward(25*long)
        right(130)
        forward(30*long)
        left(130)
        forward(23*long)
        penup()
#------------------------------------------------------------------------#
def dessin(nb_erreurs):#fonction permettant de faire le dessin du pendu à chaques étapes
    speed(0)
    pensize(10)
    if nb_erreurs==1:
        penup()
        home()
        goto(-500,-100)
        pendown()
        forward(200)
        backward(400)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==2:
        penup()
        home()
        goto(-500,-100)
        pendown()
        left(90)
        forward(500)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==3:
        penup()
        home()
        goto(-500,400)
        pendown()
        left(180)
        forward(200)
        backward(600)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==4:
        penup()
        home()
        goto(-100,400)
        pendown()
        backward(300)
        right(120)
        forward(190)
        backward(190)
        right(60)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==5:
        penup()
        home()
        goto(-100,400)
        pendown()
        right(90)
        forward(70)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==6:
        penup()
        home()
        goto(-100,330)
        right(90)
        right(90)
        forward(5)
        pendown()
        fillcolor('violet')
        begin_fill()
        circle(50)
        end_fill()
        circle(50,180)
        right(90)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==7:
        penup()
        home()
        goto(-100,230)
        pendown()
        right(90)
        forward(200)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==8:
        penup()
        home()
        goto(-100,80)
        pendown()
        right(90)
        backward(140)
        right(80)
        forward(100)
        backward(100)
        right(20)
        backward(100)
        forward(100)
        left(20)
        left(80)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==9:
        penup()
        home()
        goto(-100,30)
        right(90)
        pendown()
        left(60)
        forward(100)
        backward(100)
        right(120)
        forward(100)
        penup()
        home()
        pensize(5)
        return False
    elif nb_erreurs==10:
        penup()
        home()
        goto(-100,230)
        right(90)
        right(180)
        forward(60)
        right(90)
        forward(20)
        fillcolor('black')
        begin_fill()
        circle(7)
        end_fill()
        backward(40)
        fillcolor('black')
        begin_fill()
        circle(7)
        end_fill()
        forward(-2)
        right(90)
        forward(20)
        pendown()
        pencolor("red")
        circle(20,180)
        penup()
        home()
        pencolor("black")
        pensize(5)
        return True
    else:
        pensize(5)
        return False

#------------------------------------------------------------------------#
def verification(lettre):  #Pour savoir si la lettre est dans le mot où non
    for verif in Mot:
        if verif==lettre:
            return True
    return False
            
#------------------------------------------------------------------------#
def couleur(let):          #Mettre les lettres utilisées dans le carré: rouge si pas bon, vert si bon
    if verification(let)==True:
        pencolor("green")
        lettre_carre(let,1)
    else:
        global Mauvaises_lettres #pour augmenter la variable qui dessine le pendu
        Mauvaises_lettres=Mauvaises_lettres+let+", "#rajoute les lettres pas bonne pour la phrase finale
        pencolor("red")
        lettre_carre(let,1)
    pencolor("black")
#------------------------------------------------------------------------#
def lettre_carre(b,long):# ceci est la fonction qui dessine les lettres de l'alphabets jouées par l'utilisateur
    penup()
    for i in range(len(Alphabet)):#ce programme trouve la position de la lettre jouée et la range dans le tableau en fonction de sa position dans l'alphabet
        if Alphabet[i]==b:
            if i<5:
                goto(320+i*80,220)
                pendown()
                lettre(Alphabet[i],long)
            elif i<10 and i>4:
                k=i-5
                goto(320+k*80,140)
                pendown()
                lettre(Alphabet[i],long)
            elif i>9 and i<15:
                k=i-10
                goto(320+k*80,65)
                pendown()
                lettre(Alphabet[i],long)
            elif i>14 and i<20:
                k=i-15
                goto(320+k*80,-10)
                pendown()
                lettre(Alphabet[i],long) 
            elif i>19 and i<25:
                k=i-20
                goto(320+k*80,-80)
                pendown()
                lettre(Alphabet[i],long)
            else :
                goto(320,-130)
                pendown()
                lettre(Alphabet[i],long)
#------------------------------------------------------------------------#
def tiret(mot):# cette fonction permet de dessiner les tirets en fonction du nombre de lettre dans le mot tout en étant centrée
    penup()
    x=500/len(mot)
    f=x/3
    goto(-250-(f*len(mot)),-350)
    for i in range(len(mot)):    #pour chaque lettres
        pendown()
        forward(x)
        penup()
        forward(f)
        pendown()
    penup()
    goto(250,400)
    write("Les lettres n'ont pas d'accents et les", align="left", font=("Times New Roman", 20, "normal"))
    penup()
    goto(250,350)
    write("mots sont écrits sans: ex: pasteque", align="left", font=("Times New Roman", 20, "normal"))
    

#------------------------------------------------------------------------#
def lettreDejaUtilisee(choixlet, Lettre_utilisees):#regarde les lettres qui sont deja utilisées
    iLettre_utilisee = 0                           #variable permettant de regarder si la lettre est déja utilisée
    while Lettre_utilisees[iLettre_utilisee]!=choixlet and iLettre_utilisee < len(Lettre_utilisees)-1:#vérifie les lettres une par une
        iLettre_utilisee = iLettre_utilisee + 1
    return Lettre_utilisees[iLettre_utilisee]==choixlet   #renvoie si elle est utilisée(True) ou pas(False)
#------------------------------------------------------------------------#
def lettreValide(choixlet, Alphabet): #regarde si la lettre est valide
    iLettre = 0                             #variable permettant de regarder si la lettre existe
    while Alphabet[iLettre]!=choixlet and iLettre < len(Alphabet)-1:#vérifie dans l'alphabet 
        iLettre = iLettre + 1
    return Alphabet[iLettre]==choixlet  #renvoie si elle existe(True) ou pas(False)  

#------------------------------------------------------------------------#
def pendu(mot):#fonction generale qui demande a l'utilisateur une lettre et la place sur les tirets si la lettre est présente dans le mot sinon elle dessine un pendu  
    z=0
    choixlet=str(textinput("Alphabet","Quel lettre voulez-vous jouer??"))   #demande la lettre au joueur
    while not (lettreValide(choixlet, Alphabet)) or lettreDejaUtilisee (choixlet, Lettre_utilise):
        choixlet=str(textinput("Alphabet","Cette lettre n'est pas valide, choisissez en une autre"))
    Lettre_utilise.append(choixlet)#ajoute la lettre choisie aux lettres utilisées
    couleur(choixlet)
    for i in range(len(mot)):
        if mot[i]==choixlet:
            penup()
            x=500/len(mot)                      #Pour centrer le mot dans l'écran
            f=x/3
            if i ==0:# quand on est au début 
                goto(-250-(f*len(mot)),-350)
                choixlet=str(choixlet)
                pendown()
                pensize(7)
                lettre(choixlet,15/len(mot))
                pensize(5)
                z=z+1
            else:# pour que les tirets ne soient pas trop grop
                goto(-250-(f*len(mot)-f*i-i*x),-350)
                choixlet=str(choixlet)
                pendown()
                pensize(7)
                lettre(choixlet,15/len(mot))
                pensize(5)
                z=z+1
    if z!=0:       #pour rajouter le nombre de lettre qui de fois que la lettre est dans le mot
        global victoire
        victoire=victoire+z
    else:          #pour dessiner le pendu si la lettre est fausse
        global dessin_pendu
        dessin_pendu=dessin_pendu+1
        dessin(dessin_pendu)
    return True
                
    

#------------------------------------------------------------------------#
def MotAlea():  #Définition du mot en aléatoire grâce à random
    a=choice(["ananas","fraise","tomate","pomme","banane","poire","voiture","clarinette","guitare","musique","maison","tractopelle","wagon","ordinateur","mannette","ecran","bureau","arbre","tableau","clavier","enceinte","trouse","alphabet","haie","souris","elephant","tapis","gym","acrobatyque","fusee","frigidaire","musee","lit","panthère","porte","habit","camion","commode","livre","chausette","appartement","mer","clef","terre","tour","magie","pierre","robot","lampe","lettre","reveil","monaie"])
    #ensemble des mots/>
    return a




#------------------------------------------------------------------------#
def carre():                #Définition du carré à droite pour mettre les lettres dedans
    fillcolor("black")
    begin_fill()            #début de la fonction pour remplir le carré(fonction turtle)
    penup()
    goto(300,280)
    pendown()
    for i in range(4):      #carré en lui même
        forward(425)
        right(90)
    end_fill()              #fin de la fonction pour remplir le carré(fonction turtle)
#------------------------------------------------------------------------#        
def Victoire1(mot,gagne):#regarde si il y a victoire
    if gagne==len(mot):
        return True
    else:
        return False
#------------------------------------------------------------------------#  
def reset2():# lorsque cette fonction est appellée elle rénitialise le pendu seulement si le jeu est fini
    global result
    global cac
    if result==1:
        clear()
        global tab
        tab=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        global victoire
        victoire=0
        global dessin_pendu
        dessin_pendu=0
        global Lettre_utilise
        Lettre_utilise=[""]
        speed(0)
        pensize(5)
        hideturtle()
        global Mot

        Mot=MotAlea()
        tiret(Mot)
        carre()
        global Mauvaises_lettres
        Mauvaises_lettres=""


        while Victoire1(Mot,victoire)==False and dessin(dessin_pendu)==False:
            pendu(Mot)

        phrase="Bien jouer, tu as trouvé le mot : "+Mot+", et tu as eu "+str(dessin_pendu)+" mauvaises lettres: "+Mauvaises_lettres
        phrase_False="Domage, tu n'as pas trouvé le mot : "+Mot+", et tu as eu "+str(dessin_pendu)+" mauvaises lettres: "+Mauvaises_lettres

        if dessin(dessin_pendu):
            cac=1
            result=1
            reset()
            hideturtle()
            penup()
            goto(-500,0)
            pendown()
            write(phrase_False,move=False, align="left", font=("Times New Roman", 20, "normal"))
            penup()
            seth(0)
            goto(-850,-200)
            pendown()
            write("Appuyez sur la touche Up pour recommencer le jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
            penup()
            seth(0)
            goto(-850,-300)
            pendown()
            write("Appuyez sur la touche Down pour changer de jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))

        elif Victoire1(Mot,victoire):
            cac=1
            result=1
            reset()
            hideturtle()
            penup()
            goto(-400,0)
            pendown()
            write(phrase,move=False, align="left", font=("Times New Roman", 20, "normal"))
            penup()
            seth(0)
            goto(-850,-200)
            pendown()
            write("Appuyez sur la touche Up pour recommencer le jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
            penup()
            seth(0)
            goto(-850,-300)
            pendown()
            write("Appuyez sur la touche Down pour changer de jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
        turtle.onkey(reset2,"Up")
        turtle.onkey(interface,"Down")
        turtle.listen()


#------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------Fonctions_Morpion-----------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------#
def grille():#dessine une grille de morpion
    penup()
    couleur=choice(["red","blue","pink","black","brown","purple","yellow","grey"])
    pensize(10)
    pencolor(couleur)
    seth(0)
    goto(-300,-300)
    pendown()
    speed(0)
    for i in range(4):     
        forward(600)
        left(90)
    forward(200)
    left(90)
    forward(600)
    right(90)
    forward(200)
    right(90)
    forward(600)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(600)
    right(90)
    forward(200)
    right(90)
    forward(600)
    

    


xclick = 0
 
yclick = 0
def forme(j):#fonction qui permet de dessiner une croix
    if j==1:
       
        pendown()
        pencolor(couleurJ1)#changement de couleur(bleu)
        left(45)
        forward(100)
        backward(200)
        forward(100)
        left(90)
        forward(100)
        backward(200)
        penup()
        home()
#fonction qui permet de dessiner un rond
    else:
    
        penup()
        right(90)
        forward(80)
        left(90)
        pendown()
        pencolor(couleurJ2)#changement de couleur(rouge)
        circle(80)
        penup()
    
 
            #fonction qui determine les coordonées quand la fonction morpion s'execute

def morpion(x,y):
    global result
    result=0
    xclick = x
    yclick = y
    if tableau[0]==0:#ceci permet d'alterner le j(joueur) entre 1 et 2 .
        j=1
        tableau[0]=1
        
    else:
        j=2
        tableau[0]=0
       
    if x > -300 and x<-100 and y>-300 and y<-100 and tab[2][0]==0:#ceci permet de délimiter les cases et de tracer les formes en fonction du joueur,il regarde aussi si la case a déja été jouée
                                      # a chaque fois le programme teste si il y un alignement de 3 points et arrete le detectage de click avec turtle.onscreenclick(None)
        penup()
        goto(-200,-200)#de plus il teste si il y a égalité
        pendown()#
        forme(j)
        tab[2][0]=j # on stock tans un tableau  la valeur j afin de pouvoir mettre le morpion sous forme de tableau et pouvoir le réutiliser pour regarder si il y a victoire
        # idem pour les neufs autres cas 
        if Victoire2(j)==True:
            turtle.onscreenclick(None)
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            result=1
        
    elif x > -100 and x<100 and y>-300 and y<-100 and tab[2][1]==0:#ceci permet de délimiter les cases
        penup()
        goto(0,-200)
        pendown()
        
        forme(j)
        tab[2][1]=j
        if Victoire2(j)==True:
            turtle.onscreenclick(None)
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            
            result=1
    elif x > 100 and x<300 and y>-300 and y<-100 and tab[2][2]==0:#ceci permet de délimiter les cases
        penup()
        goto(200,-200)
        forme(j)
        tab[2][2]=j
        if Victoire2(j)==True:
            turtle.onscreenclick(None)
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            result=1
    elif x > -300 and x<-100 and y>-100 and y<100 and tab[1][0]==0:#ceci permet de délimiter les cases
        penup()
        goto(-200,0)
        forme(j)
        tab[1][0]=j
        if Victoire2(j)==True:
            turtle.onscreenclick(None)           
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            result=1

    elif x > -100 and x<100 and y>-100 and y<100 and tab[1][1]==0:#ceci permet de délimiter les cases
        penup()
        goto(0,0)
        forme(j)
        tab[1][1]=j
        if Victoire2(j)==True:
            turtle.onscreenclick(None)
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            result=1
        
    elif x > 100 and x<300 and y>-100 and y<100 and tab[1][2]==0:#ceci permet de délimiter les cases
        penup()
        goto(200,0)
        forme(j)
        tab[1][2]=j
        if Victoire2(j)==True:
            turtle.onscreenclick(None)
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            
            result=1
        
    elif x > -300 and x<-100 and y>100 and y<300 and tab[0][0]==0:#ceci permet de délimiter les cases
        penup()
        goto(-200,200)
        forme(j)
        tab[0][0]=j
        if Victoire2(j)==True:
            result=1
            turtle.onscreenclick(None)
        elif nul2()==True:
            turtle.onscreenclick(None)
            result=1
    elif x > -100 and x<100 and y>100 and y<300 and tab[0][1]==0:#ceci permet de délimiter les cases
        penup()
        goto(0,200)
        forme(j)
        tab[0][1]=j
        if Victoire2(j)==True:
            turtle.onscreenclick(None)
            
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            
            result=1
    elif x > 100 and x<300 and y>100 and y<300 and tab[0][2]==0:#ceci permet de délimiter les cases
        penup()
        goto(200,200)
        forme(j)
        tab[0][2]=j
        if Victoire2(j)==True:
            turtle.onscreenclick(None)
            
            result=1
        elif nul2()==True:
            turtle.onscreenclick(None)
            
            result=1
    else:
        if tableau[0]==0:#ceci permet d'alterner le j(joueur) entre 1 et 2 .
            j=1
            tableau[0]=1
            global J
            Joueur=1
        else:
            j=2
            global J
            J=2
            tableau[0]=0

   

def nul2():#permet de regarder si il y a match nul
    result=0
    for i in range(3): #on regarde dans le tableau si  toute les valeurs sont supérieures a 0 si oui c'est qu'il y a match nul
        for k in range(3):
            if tab[i][k]>0:
                result=result+1
                if result==9:
                    global cac
                    cac=1
                    penup()
                    goto(-50,300)
                    pendown()
                    pencolor("black")
                    phrase_nul="Match nul"
                    write(phrase_nul,move=False, align="left", font=("Times New Roman", 20, "normal"))
                    penup()
                    seth(0)
                    goto(-850,100)
                    pendown()
                    write("Appuyez sur la touche Up pour recommencer le jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
                    penup()
                    seth(0)
                    goto(-850,-100)
                    pendown()
                    write("Appuyez sur la touche Down pour changer de jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
                    return True


def horiz():
    result=0#permet de vérifier si aucun point est aligné horizontalement 
    for i in range(3):
        result=0
        for k in range(3): #on regarde ligne par ligne si chaque element de la ligne a la meme valeur pour le joueur 1
            if tab[i][k]==2:
                result=result+1
                if result==3:
                    return True

    result=0
    for i in range(3):#on regarde ligne par ligne si chaque element de la ligne a la meme valeur pour le joueur 2
        result=0
        for k in range(3):
            if tab[i][k]==1:
                 result=result+1
                 if result==3:
                    return True

def verti():
    result=0#permet de vérifier si aucun point est aligné verticalement
    for i in range(3):
        result=0
        for k in range(3):
            if tab[k][i]==2:
                result=result+1#on regarde colonne par colonne si chaque element de la ligne a la meme valeur pour le joueur 1
                if result==3:
                    return True
    result=0
    
    for i in range(3):
        result=0
        for j in range(3):
            if tab[j][i]==1:
                 result=result+1#on regarde colonne par colonne si chaque element de la ligne a la meme valeur pour le joueur 1
                 if result==3:
                     return True
def diag():#permet de vérifier si aucun point est aligné en diagonale
    result=0
    for i in range(3):
        if tab[i][i]==2:
            result=result+1#on regarde les deux diagonales possibles pour le joueur 1
            if result==3:
                return True
    result=0
    for i in range(3):
        if tab[i][i]==1:
            result=result+1
            if result==3:
                return True
    result=0
    for i in range(3):
        if tab[2-i][i]==2:
            result=result+1#on regarde les deux diagonales possibles pour le joueur 2
            if result==3:
                return True
    result=0
    for i in range(3):
        if tab[2-i][i]==1:
            result=result+1
            if result==3:
                return True
def Victoire2(joueur):#regarde si il y a victoire
    if diag()==True or horiz()==True or verti()==True:
        global cac
        cac=1
        penup()
        goto(-110,300)
        pendown()
        pencolor("black")
        phrase_vic="Le joueur "+str(Joueur)+" a gagné"
        write(phrase_vic,move=False, align="left", font=("Times New Roman", 20, "normal"))
        penup()
        seth(0)
        goto(-850,100)
        pendown()
        write("Appuyez sur la touche Up pour recommencer le jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
        penup()
        seth(0)
        goto(-850,-100)
        pendown()
        write("Appuyez sur la touche Down pour changer de jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
        return True

def Reset():#lorsque cette fonction est appellé elle rénitialise le morpion, elle marche que quand il y a match nul ou victoire
    global result
    if result==1:
        result=0
        global couleurJ1
        couleurJ1=choice(["red","blue","pink","black","brown","purple","yellow","grey"])#couleur aleatoire
        global couleurJ2
        couleurJ2=choice(["red","blue","pink","black","brown","purple","yellow","grey"])
        global tab
        tab=[[0,0,0],[0,0,0],[0,0,0]]
        clear()
        pencolor("black")
        grille()
        turtle.onscreenclick(morpion)
#-----------------------------------Programme------------------------------------------------------------#
def programme(b):
    if b==1:
        global Grille
        Grille=GrilleVide()#définit la grille
        dessin_grille()#dessine la grille en turtle
        turtle.onscreenclick(puissance)#ceci permet de donner a la fonction puissance deux valeurs x et y au click de l'utilistateur
        turtle.onkey(reset1,"Up")
        turtle.onkey(interface,"Down")#ceci appelle une fonction si la touche up est préssée par l'utilisateur
        turtle.listen()

    elif b==2:
        global cac
        global result
        global Alphabet
        Alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        global victoire
        victoire=0
        global dessin_pendu
        dessin_pendu=0
        global Lettre_utilise
        Lettre_utilise=[""]
        speed(0)
        pensize(5)
        hideturtle()
        global Mot
        Mot=MotAlea()
        tiret(Mot)
        carre()
        global Mauvaises_lettres
        Mauvaises_lettres=""


        while Victoire1(Mot,victoire)==False and dessin(dessin_pendu)==False:
            pendu(Mot)

        phrase="Bien jouer, tu as trouvé le mot : "+Mot+", et tu as eu "+str(dessin_pendu)+" mauvaises lettres: "+Mauvaises_lettres
        phrase_False="Domage, tu n'as pas trouvé le mot : "+Mot+", et tu as eu "+str(dessin_pendu)+" mauvaises lettres: "+Mauvaises_lettres
        

        if dessin(dessin_pendu):
            cac=1
            result=1
            reset()
            hideturtle()
            penup()
            goto(-500,0)
            pendown()
            write(phrase_False,move=False, align="left", font=("Times New Roman", 20, "normal"))
            penup()
            seth(0)
            goto(-850,-200)
            pendown()
            write("Appuyez sur la touche Up pour recommencer le jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
            penup()
            seth(0)
            goto(-850,-300)
            pendown()
            write("Appuyez sur la touche Down pour changer de jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))

        elif Victoire1(Mot,victoire):
            cac=1
            result=1
            reset()
            hideturtle()
            penup()
            goto(-400,0)
            pendown()
            write(phrase,move=False, align="left", font=("Times New Roman", 20, "normal"))
            penup()
            seth(0)
            goto(-850,-200)
            pendown()
            write("Appuyez sur la touche Up pour recommencer le jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
            penup()
            seth(0)
            goto(-850,-300)
            pendown()
            write("Appuyez sur la touche Down pour changer de jeu",move=False, align="left", font=("Times New Roman", 15, "normal"))
        turtle.onkey(reset2,"Up")
        turtle.onkey(interface,"Down")#ceci appelle une fonction si la touche up est préssée par l'utilisateur
        turtle.listen()
        
    elif b==3:
        global tab
        tab=[[0,0,0],[0,0,0],[0,0,0]]
        pensize(20)
        grille()
        global J
        J=0
        global Joueur
        Joueur=0
        hideturtle()
        global xclick
        global yclick
        xclick = 0
        yclick = 0
        global couleurJ2
        global couleurJ1
        couleurJ2=choice(["red","blue","pink","black","brown","purple","yellow","grey"])
        couleurJ1=choice(["red","blue","pink","black","brown","purple","yellow","grey"])
        global tableau
        tableau=[0]
        turtle.onscreenclick(morpion)
        turtle.onkey(Reset,"Up")
        turtle.onkey(interface,"Down")#ceci appelle une fonction si la touche up est préssée par l'utilisateur
        turtle.listen()
        #cela permet de déterminer les deux paramètres de morpion sur un click de l'utilisateur
        penup()
        goto(-300,300)
        pendown()
global cac
cac=1
interface()
