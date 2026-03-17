# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Devoir 3 numéro 1

On a un billot de bois qui flotte dans l'eau et qui est aussi retenu par une corde
On crée une fonction pour trouver:
a. Le poids specifique du billot
b. La tension dans la corde
c. L’angle d’inclinaison du billot par rapport à l’horizontale, sachant que
la pression hydrostatique au point A est de 24.5 kPa (jaugee)

20 mars 2026

Justin Léveillé
Benjamin Grégoire
Matis Veilleux
"""
import math

def calcul_billot(l_tot_billot,l_submerge_billot,d_billot,rho_eau,pression):
    
 """
    Parameters
    ----------
   l_tot_billot : Entier ou décimale.Longueur totale du billot en m. 
                  Doit être supérieure à zéro
                  
   l_submerge_billot :Entier ou décimale. Longueur du billot qui est submergé
                      en m. Doit être supérieur à zéro
      
   d_billot : Entier ou décimale. Diamètre du billot en m. Doit être supérieur
              à zéro
              
   rho_eau : Entier ou décimal. Masse volumique de l'eau en kg/m^3
       
   pression : Entier ou décimale. Pression hydrostatique de l'eau en Pa

    Returns
    -------
    poids_spec_billot :Décimal. Poids spécifique du billot en N/m^3
        
    tension_corde : Décimal. Tension dans la corde retenant le billot en N
        
    angle : Décimal.Angle d'inclinaison du billot par rapport à l'horizontal
            en degré
    """
    
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

    return poids_spec_billot,tension_corde, angle




