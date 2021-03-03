# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:19:38 2021

@author: LUIS
"""

import pyautogui as pg
import time
import webbrowser as web

number = "+51948653547"
mensajeParcial = " "

web.open('https://web.whatsapp.com/send?phone='+number+'&text='+mensajeParcial)
time.sleep(5)

for i in range(8):
    
    pg.write(" ¡¡¡HOLA VENGO A RECORDARTE QUE!!!\n\n"
             "- Eres una chica muy bonita\n"
             "- Tus ojos son hermosos\n"
             "- Hay algo que no puedas hacer?"
             "\n- Mujer admirable")
    pg.press('enter')
    time.sleep(100)
    pass

pg.alert("Terminado")
