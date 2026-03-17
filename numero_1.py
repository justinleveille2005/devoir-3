# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Devoir 3 numéro 1

Justin Léveillé
Benjamin Grégoire
Matis Veilleux
"""
import math

def calcul_billot(l_tot_billot,l_submerge_billot,d_billot,rho_eau,pression):

    centre_flottaison=l_submerge_billot/2
    vol_sub=l_submerge_billot*(d_billot/2)**2*math.pi
    vol_tot=l_tot_billot*(d_billot/2)**2*math.pi
    fb=rho_eau*9.81*vol_sub
    rho_billot = (centre_flottaison*fb)/((l_tot_billot/2)*9.81*vol_tot)
    poids_spec_billot = rho_billot*9.81
    w = rho_billot*9.81*vol_tot
    tension_corde = fb-w
    h = pression/(rho_eau*9.81)
    angle = (180/math.pi)*math.asin(h/l_submerge_billot)

    print(angle)
    print(tension_corde)
    print(poids_spec_billot)



