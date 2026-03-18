# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Devoir 3 numéro 2

Voici un script servant à calculer le poids spécifique du billot, la tension 
dans la corde retenant le billot et l'angle du celui-ci avec l'horizontal grâce
à la fonction du numéro 1.

20 mars 2026

Justin Léveillé
Benjamin Grégoire
Matis Veilleux
"""

import numpy as np

from numero_1 import calcul_billot

donnees=np.loadtxt("donnees_billot.txt")

l_tot_billot=donnees[:,0]
l_submerge_billot=donnees[:,1]
d_billot=donnees[:,2]
rho_eau=donnees[:,3]
pression=donnees[:,4]

tableau_resultat=[calcul_billot(l_tot_billot,l_submerge_billot,d_billot,rho_eau,pression)]

resultats1=np.array(tableau_resultat)

resultats2=resultats1[0,:,:]

resultat_final=np.transpose(resultats2)

np.savetxt("numero_2.py",resultat_final)

print(resultat_final)
