# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Devoir 3 numéro 1

Justin Léveillé
Benjamin Grégoire
Matis Veilleux
"""

import math

def calcul_billot(L_TOT_BILLOT,L_SUBMERGEE_BILLOT,D_BILLOT,RHO_EAU,PRESSION):
    
    CENTRE_FLOTTAISON=L_SUBMERGEE_BILLOT/2
    VOL_SUB=L_SUBMERGEE_BILLOT*(D_BILLOT/2)**2*math.pi
    VOL_TOT=L_TOT_BILLOT*(D_BILLOT/2)**2*math.pi
    FB=RHO_EAU*9.81*VOL_SUB
    RHO_BILLOT = (CENTRE_FLOTTAISON*FB)/((L_TOT_BILLOT/2)*9.81*VOL_TOT)
    POIDS_SPEC_BILLOT = RHO_BILLOT*9.81
    W = RHO_BILLOT*9.81*VOL_TOT
    TENSION_CORDE = FB-W
    H = PRESSION/(RHO_EAU*9.81)
    angle = (180/math.pi)*math.asin(H/L_SUBMERGEE_BILLOT)
    
    print(angle)
    print(TENSION_CORDE)
    print(POIDS_SPEC_BILLOT)


