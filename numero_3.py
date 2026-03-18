# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Devoir 3 numéro 2

20 mars 2026

Justin Léveillé
Benjamin Grégoire
Matis Veilleux
"""
import numpy as np

def equation_colebrooke(diametre,debit,mv,rugosite,viscosite):
    """
    
    Parameters
    ----------
    diametre : Entier ou décimal. Diamètre de la conduite en (m).Doit être 
               supérieur à zéro
        
    debit : Entier ou décimal. Débit du fluide en (m/s).Doit être supérieur à
            zéro
        
    mv : Entier ou décimal. Masse volumique du fluide en (kg/m^3) 
        
    rugosite : Décimal. Rugosité de la conduite en (m)
        
    viscosite : Décimal. Viscosité dynamique du fluide en (kg/m*s)
        
    Returns
    -------
    None.

    """
    
    aire=(diametre**2*np.pi)/4
    
    vitesse=debit/aire
    
    reynolds=mv*vitesse*diametre/viscosite
