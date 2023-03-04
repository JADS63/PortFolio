from turtle import*                       #importation de turtle
import random                             #importation de random





def illusiontriangle(long,couleur):       #définition du triangle principale
    pencolor(couleur)                     #applique la couleur au stylo
    penup()                               #stylo levé
    goto(0,0)                             #recentrage
    setheading(0)                         #orientation vers le haut
    pendown()                             #stylo en mode écriture
    if long<10:                           #si la valeur rentrez par l'utilisateur est inférienre à 10 alors le programme renvoie que ce n'est pas possible
            return(print("Le triangle nas pas été fais pour cause de cotés trop petits"))
    largtrait=10                          #création de la largeur des traits
    coef=(largtrait/long)*10              #création du coéfficien qui définit la taille du trait*
    pensize(largtrait)                    #définition de la largeur du trait
    while long>1:                         #tant que le triangle est plus petit que 1, le programme continu
        for i in range(3):                #créer un triangle
            forward(long)
            left(120)
            forward(long)
        long=long-10                      #longueur réduite
        largtrait=largtrait-coef          #largeuer du trait réduite
        pensize(largtrait)                #application à la taille du stylo









def reverse(long):                        #définition de l'inverse du triangle principale
        if long<10:                       #si la valeur rentrez par l'utilisateur est inférienre à 10 alors le programme renvoie que ce n'est pas possible
            return(print("Le triangle nas pas été fais pour cause de cotés trop petits"))
        largtrait=0.1                     #pour initialisé le largtrait comme sur l'autre triangle
        coef=(10/long)*10                 #permet de calculer le coefficient de la taille du trait     
        pensize(largtrait)                #défini la taille du trait
        cote=long%10                      #défini la taille du coté grace a la longueur de base
        long=long+10                      #pour faire le dernier tour
        while long>1:                     #tant que le triangle est plus petit que 1, le programme continu
                for i in range(3):        #créer le triangle
                    forward(cote)
                    right(120)
                    forward(cote)
                cote=cote+10              #longueur augmenter
                long=long-10              #
                largtrait=largtrait+coef  #augmente la largeur du tarit
                pensize(largtrait)        #applique la largeur au stylo
        hideturtle()                      #rend la tortue invisible
        return print("C'EST LA FIN DE VOTRE FIGURE ;)") #fin du programme








def rectangle(long,couleur):              #définition du rectangle
    penup()                               #stylo levé
    goto(0,0)                             #recentrage
    pendown()                             #stylo en mopde écriture
    coté=(long*2)+20                      #défini le coté du rectangle en fonction du coté du triangle
    penup()                               #stylo levé
    forward(long+20)                      #avance à l'endroit où commence le triangle
    pendown()                             #stylo en mode écriture
    fillcolor(couleur)                    #la couleur est garder en mémoire pour savoir comment remplir le rectangle
    begin_fill()                          #pour savoir quelle forme il doit colorié
    left(90)                              #le tourne vers le haut
    for i in range(2):                    #créer le rectangle
        forward(coté)
        left(90)
        forward(coté+20)
        left(90)
        forward(coté)
    end_fill()                            #rempli le rectangle
    




def triangle_en_couleur():                #       
    speed(0)
    for i in range (300):
        penup()
        goto(random.randint(-1000, 1000),random.randint(-500, 300))
        r=random.randint(50,250)
        pendown()
        fillcolor(random.choice(['green','blue','red','purple','pink','brown','black','orange','yellow']))
        begin_fill()
        for i in range(3):
            forward(r)
            left(120)
        end_fill()
    speed(6)
            


longueur=int(input("Rentrez la longueur du coté de votre triangle qui doit être supérieur à 10 : "))
couleur1=str(input("Rentrez la couleur du triangle parmis les suivantes : black, grey, white : "))
while couleur1!="black" and couleur1!="white" and couleur1!="grey": #défini la bibliothéque de couleur
        couleur1=str(input("Cette couleur n'est pas référencée, veuillez en choisir une autre parmi: black, grey, white : ")) #si l'utilisateur l'écrit mal, la question est reposée
couleur2=str(input("Rentrez la couleur de l'arrière plan du triangle parmis les suivantes : green, blue, red, purple, pink, brown, orange, yellow : "))
while couleur2!='green'and couleur2!='blue'and couleur2!='red'and couleur2!='purple'and couleur2!='pink'and couleur2!='brown'and couleur2!='orange'and couleur2!='yellow': #défini la bibliothéque de couleur
        couleur2=str(input("Cette couleur n'est pas référencée, veuillez en choisir une autre :green, blue, red, purple, pink, brown, orange, yellow : ")) #si l'utilisateur l'écrit mal, la question est reposée
triangle_en_couleur()
rectangle(longueur,couleur2)
illusiontriangle(longueur,couleur1)
reverse(longueur)
#BY raphaël and julien
    
