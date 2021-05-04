# Projet : Affichage du Code Barre
# Réalisé par :
# Ghita BOUZIAN


#Importer la bibliothèque turtle
from turtle import*

#Cette fonction convertit une chaîne de caractère (string) n en une liste l d'entiers (digits)
def strtoint(n):
    l=[]
    #chaque élément de n sera converti en entier puis rajouté à la liste l
    for i in n:
        l.append(int(i))
    return(l)

#Cette fonction retourne reste qui est la forme binaire d'un décimal d.
def binaryform (d):
  if d!=0:
    reste=[]
    #Cette boucle construit la liste constituée des restes formant les bits de la forme binaire de d
    while d>=1:
      reste.append(d%2)
      d=d//2
    reste.reverse()
    return reste
  else:
    return [0]

#Cette fonction représente un chiffre binaire donné sous forme d'une liste binaryform, par une liste de 4 bits complétée par des 0 si nécessaire
def binary4b(binaryform):
  z=[]
  #Calculer le nombre de 0 manquants
  x=4-len(binaryform)
  #Construire une liste z de 0 manquants
  for loop in range (x):
    z.append(0)
  #Concaténer la liste des 0 avec la liste binaryform
  binaryform=z+binaryform
  return(binaryform)

#Cette fonction convertit une liste de chiffres l en une liste de listes lol où chacun de ces chiffres est représenté en binaire 4 bits
def convertlto4(l):
  lol=[]
  #Convertir chaque digit d de la liste l, en une liste binaire 4 bits à rajouter à la liste lol
  for d in l:
    b4=binary4b(binaryform(d))
    lol.append(b4)
  return(lol)

#Cette fonction affiche le code barre correspondant à la chaine de de chiffres n et de hauteur introduits comme paramètres
def drawbarcode(n,h):
  speed(0)
  #Convertir la chaine des chiffres n en une liste code4bits constituée de sous-listes qui représentent leurs formats 4 bits
  code4bits=convertlto4(strtoint(n))
  #tracer une ligh du code barre autant de fois qu'il le faut en fonction de la hauteur h
  for loop in range(h):
    #Pour chaque digit l codé 4 bits et chaque bit de position i,tracer les lignes en respectant les contraintes de couleur définies en fonction de la valeur du bit et de longueur en pixels définie en fonction de sa position
    for l in code4bits:
      for i in range (len(l)):
        if l[i]==0:
          color("white")
        else:
          color("black")
        if i==0:
          forward(3)
        elif i==1 or i==2:
          forward(2)
        elif i==3:
          forward(1)
      #Prévoir un pixel blanc à la fin du tracé de chaque chiffre sans le tracer à la fin du nombre
      if code4bits.index(l) < 12:
        color("white")
        forward(1)
    # Passer au début de la ligne suivante avec goto
    # Une autre solution est d'utiliser le code suivant:
    #pu()
    # backward(13*(8+1))
    # right(90)
    # forward(1)
    # left(90)
    #pd()
    penup()
    goto(0,loop+1)
    pendown()

#Ce programme principal lit un string n de 13 chiffres exactement en plus de la hauteur souhaitée, puis appelle la fonction drawbarcode pour tracer le code barre correspondant

n=""
#la boucle est utilisée pour obliger l'utilisateur à saisir un string d'exactement 13 chiffres
while len(n)!=13:
  n=input("Introduire un nombre de 13 chiffres: ")

h=int(input("Introduire la hauteur: "))

drawbarcode(n,h)
