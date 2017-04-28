# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def moyenne_listes2(list1,list2):
    val=0.0
    for index in list1+list2:
        val+=index
    return val/len(list1+list2)