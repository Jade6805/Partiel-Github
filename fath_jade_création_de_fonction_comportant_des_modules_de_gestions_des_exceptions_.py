# -*- coding: utf-8 -*-
"""Fath Jade - Création de fonction comportant des modules de gestions des exceptions .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HN3N2bgdJitEgLYN66xr04bPMJAr2bVF

# **Création de fonction comportant des modules de gestions des exceptions**

Utilisation de la fonction factorielle pour cet excercice
"""

# définition de la fonction factorielle par une approche récursive 
def factorielle(n):
  if n == 0 :
      return 1
  else :
      return n * factorielle(n-1)

# test du code 
factorielle(0)

# test du code 
factorielle(5)

# Exception de la chaîne de caractère 
def factorielle(n):
  if n == 0 :
      return 1
  else :
    if ((type(n))== str):
      print("Impossible de saisir un string dans cette fonction")
      print("Veuillez saisir une valeur numérique: ")
      n = int(input())
    return n * factorielle(n-1)

# test du code
factorielle('lm£')

# Exception d'un nombre complexe
def factorielle(n):
  if n == 0 :
      return 1
  else :
    if ((type(n))== complex):
      print("Impossible de saisir un complex dans cette fonction")
      print("Veuillez saisir une valeur numérique: ")
      n = int(input())
    return n * factorielle(n-1)

# test du code 
factorielle(8j)

# Exception d'un nombre négatif en prenant sa valeur absolue
def factorielle(n):
  if n == 0 :
      return 1
  else :
    if (type(n) in [int, float]):
      n = abs(n)
    return n * factorielle(n-1)

# test du code 
factorielle(-5)

# Exception du très grand nombre  
def factorielle(n):
  if n == 0 :
      return 1
  else :
    if (len(str(n)) > 15):
      print("Impossible de saisir un chiffre d'une telle longueur dans cette fonction")
      print("Veuillez saisir une valeur numérique: ")
      n = int(input())
    return n * factorielle(n-1)

factorielle(98765342890653456789)

"""**Exception du très petit nombre ne marche pas et entraine un plantage de colab**"""

# Exception du très petit nombre  
def factorielle(n):
  if n == 0 :
      return 1
  else :
    if (type(n)== float):
      try:
        print (n * factorielle(n-1))
      except RecursionError:
        print("Impossible d'appliquer la fonction factorielle à un float")
        print("Veuillez saisir une valeur numérique: ")
        n = int(input())
    return n * factorielle(n-1)

factorielle(9.07)

"""## **Fonction en entier**"""

# définition de la fonction factorielle par une approche récursive 
def factorielle(n):
  if n == 0 :
      return 1
  elif((type(n))== str): 
      print("Impossible de saisir un string dans cette fonction")
      print("Veuillez saisir une valeur numérique: ")
      n = int(input())
  elif ((type(n))== complex):
      print("Impossible de saisir un complex dans cette fonction")
      print("Veuillez saisir une valeur numérique: ")
      n = int(input())
  elif (type(n) in [int, float]):
      n = abs(n)
  elif (len(str(n)) > 15):
      print("Impossible de saisir un chiffre d'une telle longueur dans cette fonction")
      print("Veuillez saisir une valeur numérique: ")
      n = int(input())
  elif (type(n)== float):
      try:
        print (n * factorielle(n-1))
      except RecursionError:
        print("Impossible d'appliquer la fonction factorielle à un float")
        print("Veuillez saisir une valeur numérique: ")
        n = int(input())
  return n * factorielle(n-1)

factorielle(-5)

factorielle(5)

factorielle(5j)

factorielle("Bonjour")

"""**La fonction ne marche ni sur les grands nombres, ni sur les petits. 
Je n'arrive pas à savoir pourquoi**
"""

factorielle(977557445476698890987564)

factorielle(9.76)