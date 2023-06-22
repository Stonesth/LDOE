import time
import sys
import cv2
import os
import subprocess
import pyautogui
import glob
import numpy as np

import pytesseract
import datetime

import multiprocessing
import random

def test1(queue, event):
    while True:
        for i in range(1000):
            time.sleep(1)
            print('============')
            print('test' + str(i+1))
            print('============')
            print('')
        event.set()
        break
    

def test2(queue, event):
    while True:
        time.sleep(2)
        random_number = random.randint(0, 20)
        if random_number == 15:
            print("Test 2 failed => stop all process")
            event.set()
            break
    

def dead_or_not(queue, event) :
    while True :
        if test_if_find_image("dead", 500, 275, 950, 330) :
            time.sleep(1)
            pushTheAction_2("ressuciter", 50, 50)
            # Let the time to back to home
            time.sleep(8)
            event.set()
            break

        if test_if_find_image("ressuciter", 720, 590, 990, 650) :
            time.sleep(1)
            pushTheAction_2("ressuciter", 50, 50)
            # Let the time to back to home
            time.sleep(8)
            event.set()
            break
        time.sleep(60)

def faire_pipi() :
    if test_if_find_image("toilette", 700, 320, 740, 368) :
        pushTheAction("toilette", 50, 50)

def prendre_detruire(dossier) :
    print("prendre_detruire = ", dossier)

    movement(225, 770, 0.5)

    time.sleep(1)
    pushTheAction("main", 50, 50)
    time.sleep(1)

    # Prend dans le coffre
    object_1 = dragAndDropObject(dossier, 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    object_2 = dragAndDropObject(dossier, 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    object_3 = dragAndDropObject(dossier, 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    object_4 = dragAndDropObject(dossier, 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    # Ferme le coffre
    pushTheAction("croix", 50, 50)
    time.sleep(1)

    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)
    if (object_1) :
        detruire(dossier)
    if (object_2) :
        detruire(dossier)
    if (object_3) :
        detruire(dossier)
    if (object_4) :
        detruire(dossier)

    time.sleep(1)
    # Ferme le coffre
    pushTheAction("croix", 50, 50)
    time.sleep(1)


def prendre_pierre() :
    print ("prendre_pierre")

    movement(225, 770, 0.5)

    time.sleep(1)
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    dragAndDropObject("pierre", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("pierre", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("pierre", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("pierre", 50, 50, "right")
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def prendre_blocs() :
    print ("prendre_blocs")

    movement(225, 770, 0.5)

    time.sleep(1)
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    dragAndDropObject("blocs", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("blocs", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("blocs", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("blocs", 50, 50, "right")
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)


def detruire_pierre() :
    print ("detruire_pierre")

    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    detruire("pierre")
    detruire("pierre")
    detruire("pierre")
    detruire("pierre")
    detruire("pierre")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def detruire_blocs() :
    print ("detruire_blocs")

    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    detruire("blocs")
    detruire("blocs")
    detruire("blocs")
    detruire("blocs")
    detruire("blocs")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def detruire(dossier) :

    dragAndDropObject(dossier, 50, 50, "left")
    time.sleep(1)
    pyautogui.click(button='left') # clic avec le bouton gauche
    
    dragAndDropObject("poubelle", 50, 50, "left")
    time.sleep(1)
    dragAndDropObject("supprimer", 50, 50, "right")


def deposer_vetements() :
    print ("deposer_vetements")

    # Ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("casquette", 50, 50, "left")
    dragAndDropObject("chemise", 50, 50, "left")
    dragAndDropObject("pantalon", 50, 50, "left")
    dragAndDropObject("chaussures", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)
    time.sleep(1)


def take_items_to_treat() :
    print ("take_items_to_treat")
    # Ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("barre_fer", 50, 50, "right")
    pushTheAction("order_box", 50, 50)

    dragAndDropObject("charbons", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("planches", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("corde", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("tissus", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("bois", 50, 50, "right")
    pushTheAction("order_box", 50, 50)

    dragAndDropObject("casquette", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("chemise", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("pantalon", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("chaussures", 50, 50, "right")
    pushTheAction("order_box", 50, 50)

    dragAndDropObject("lance", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("hachette", 50, 50, "right")
    dragAndDropObject("hachette", 50, 50, "right")
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("pioche", 50, 50, "right")
    dragAndDropObject("pioche", 50, 50, "right")
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)
    time.sleep(1)
    


def take_items_from_base_to_colony() :
    print("take_items_from_base_to_colony")

    movement(313, 690, 0.25)

    # open cabane
    pushTheAction("main", 50, 50)

    dragAndDropObject("planches", 50, 50, "right")
    dragAndDropObject("barre_fer", 50, 50, "right")

    # Ferme la cabane
    pushTheAction("croix", 50, 50)
    time.sleep(1)
    
    movement(225, 770, 0.5)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("charbons", 50, 50, "right")

    pushTheAction("croix", 50, 50)
    time.sleep(1)

def go_to_home() :
    print("go_to_home")

    # tant que on ne voie pas l'image continuer de cliquer sur home_button
    while True :
        time.sleep(2)
        click_images("home_button", 1264, 231, 1330, 300)

        click_images("voyager", 810, 445, 1015, 512)
        if (test_if_find_image("accueil", 131, 74, 253, 125)) :
            break
        else : 
            print ("Je ne vois pas l'image, acceuil. recommence le process")

    time.sleep(20)
    
def go_to_colonie() :
    print("go_to_colonie")

    # tant que on ne voie pas l'image continuer de cliquer sur home_button
    while True :
        click_images("home_button", 1264, 231, 1330, 300)

        time.sleep(1)
        click_images("voyager", 810, 445, 1015, 512)
    
        if (test_if_find_image("colonie", 131, 74, 253, 125)) :
            break
        else : 
            print ("Je ne vois pas l'image, colonie. recommence le process")

    time.sleep(20)


def remplir_etabli_colonie() :
    print("remplir_etabli_colonie")
    
    go_to_colonie()

    time.sleep(1)
    
    movement(220, 770, 10)

    movement(200, 740, 2)

    # Ouvrir le creuset
    pushTheAction("gear", 50, 50)
    time.sleep(1)
    
    # Prendre les billettes
    # dragAndDropObject("billette", 50, 50, "right")

    # Enlever le charbons déjà présent
    # dragAndDropObject("charbons", 50, 50, "right")

    # Mettre les bar de Fer
    # dragAndDropObject("barre_fer", 50, 50, "left")

    # Mettre le charbons
    # dragAndDropObject("charbons", 50, 50, "left")


    # Ferme le creuset
    pushTheAction("croix", 50, 50)

    movement(354, 667, 2)

    movement(336, 799, 2)

    movement(230, 784, 2)

    # Ouvrir la scierie
    pushTheAction("gear", 50, 50)
    time.sleep(1)
    
    # Mettre les planches
    # dragAndDropObject("planches", 50, 50, "left")

    # Prendre les poutres_de_pin
    # dragAndDropObject("poutres_de_pin", 50, 50, "right")

    # Ferme la scierie
    pushTheAction("croix", 50, 50)

    # remplir_etabli_avec("poutres_de_pin", "planches", 50, 50)

    movement(355, 659, 1.5)

    movement(366, 753, 1.5)

    movement(266, 767, 2)

    movement(190, 711, 1.5)

    # Ouvrir le stock de poutre en pein
    pushTheAction("gear", 50, 50)
    time.sleep(1)

    # Déposer les poutres_de_pin
    dragAndDropObject("poutres_de_pin", 50, 50, "left")
    # Prendre des poutres de pin pour constuire des Cadre Léger
    dragAndDropObject("poutres_de_pin", 50, 50, "right")

    # Ferme la scierie
    pushTheAction("croix", 50, 50)

    movement(190, 711, 0.5)

    # Ouvrir le stock de billette
    pushTheAction("gear", 50, 50)
    time.sleep(1)

    # Déposer les billettes
    dragAndDropObject("billette", 50, 50, "left")

    # Ferme le stock de billette
    pushTheAction("croix", 50, 50)

    movement(350, 669, 1.5)

    # Ouvrir l'etagere
    pushTheAction("gear", 50, 50)
    time.sleep(1)

    # Prendre des Vis
    dragAndDropObject("vis_v2", 50, 50, "right")

    # Ferme l'etagere
    pushTheAction("croix", 50, 50)

    movement(386, 644, 2.8)

    # Ouvrir la table d'assemblage
    pushTheAction("gear", 50, 50)
    time.sleep(1)

    # Deposer les Vis
    dragAndDropObject("vis_v2", 50, 50, "left")
    # Deposer les poutres_de_pin
    dragAndDropObject("poutres_de_pin", 50, 50, "left")
    
    # prendre les cadres léger
    dragAndDropObject("cadre_leger", 50, 50, "right")

    # Ferme la table d'assemblage
    pushTheAction("croix", 50, 50)

    movement(202, 774, 2.5)

    movement(280, 629, 0.8)

    # Vider les vis_v2
    # Ouvrir l'etagere
    pushTheAction("gear", 50, 50)
    time.sleep(1)

    # Deposer les Vis
    dragAndDropObject("vis_v2", 50, 50, "left")
    # Ferme l'etagere
    pushTheAction("croix", 50, 50)
    
    movement(195, 691, 0.8)
    # Vider les cadres léger
    # Ouvrir l'etagere
    pushTheAction("gear", 50, 50)
    time.sleep(1)

    # Deposer les Vis
    dragAndDropObject("cadre_leger", 50, 50, "left")
    # Ferme l'etagere
    pushTheAction("croix", 50, 50)


    movement(195, 691, 0.8)
    # Vider les poutres de pin
    # Ouvrir l'etagere
    pushTheAction("gear", 50, 50)
    time.sleep(1)

    # Deposer les poutres_de_pin
    dragAndDropObject("poutres_de_pin", 50, 50, "left")
    # Ferme l'etagere
    pushTheAction("croix", 50, 50)

    go_to_home()
    

def open_coffre():
    print("open_coffre")

    # Ouvre le coffre
    pushTheAction("main", 50, 50)

    time.sleep(6)

def search_enemi() :
    print("search_enemi")


def go_to_the_coffre() :
    print("go_to_the_coffre")

    print (where_is_the_item("coffre", 1115, 25, 1325, 245))

    x, y = where_is_the_item("coffre", 1115, 25, 1325, 245)
    print("x = " + str(x) + ", y = " + str(y))

    x1, y1 = where_is_the_item("arrow", 1115, 25, 1325, 245)
    print("x1 = " + str(x1) + ", y1 = " + str(y1))

    x0 = abs(x - x1)
    y0 = abs(y - y1)
    
    if x0 > y0 :
        sum = x0
    else :
        sum = y0

    print("sum = " + str(sum))
    if (sum < 100) :
        movement(x+82, y+497, 1.1)
    elif (sum < 115) :
        movement(x+82, y+497, 1.5)
    else :
        movement(x+82, y+497, 2)




def where_is_the_item(dossier, x1, y1, x2, y2) :
    print("where_is_the_item")

    # Capture d'écran partielle
    x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
    screenshot = np.array(pyautogui.screenshot(region=(x1, y1, x2, y2)))
    cv2.imwrite('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png', screenshot)

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        # Lecture de l'image modèle
    # Lecture de l'image modèle
    # template = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/template.png")
        template = cv2.imread(filepath)

        # Afficher la taille de l'image
        print("dossier : ", dossier)
        # print("Taille de l'image template : ", template.shape)
        # print("Taille de l'image screenshot : ", screenshot.shape)

        # Conversion en niveaux de gris
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Récupération des dimensions de l'image modèle
        h, w = gray_template.shape

        # Correspondance de modèle
        result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)

        # Récupération de la position de la correspondance maximale
        _, _, min_loc, max_loc = cv2.minMaxLoc(result)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # print (str(max_loc))
        # print (str(min_loc))
        print (str(max_val))

        if max_val >= 0.8:
            return max_loc

        # # Affichage de la correspondance maximale
        # cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

        # # Affichage de l'image résultat
        # cv2.imshow("Result", screenshot)
        # cv2.waitKey(0)

    return find_image


def search() :

    p0 = multiprocessing.Process(target=check_radar)
    # p1 = multiprocessing.Process(target=bouger)
    p0.start()
    # p1.start()
   
    p0.join()
    # p1.terminate()

def bouger() :
    while True :
        movement(217, 659, 15)


def check_radar() :
    
    while True :
        if test_if_find_image("coffre", 1115, 25, 1325, 245) :
            break

        if test_if_find_image("enemy", 1115, 25, 1325, 245) :
            break

    return True
            
def stop_moving() :
    if (test_if_find_image("enemy", 1110, 20, 1320, 245)) :
        movement(100, 100, 0.1)

    if (test_if_find_image("animaux", 1110, 20, 1320, 245)) :
        movement(100, 100, 0.1)

def kill() :
    # p1 = multiprocessing.Process(target=live_in_the_field)
    p2 = multiprocessing.Process(target=stop_moving)
    # p1.start()
    p2.start()

    while True :
        kill_target("enemy")
        kill_target("animaux")

        if (not test_if_find_image("enemy", 1110, 20, 1320, 245) and not test_if_find_image("animaux", 1110, 20, 1320, 245)) :
            pushTheAction("auto", 50, 50)
        else :
            print ("enemy = " + str(test_if_find_image("enemy", 1110, 20, 1320, 245)))
            print ("animaux = " + str(test_if_find_image("enemy", 1110, 20, 1320, 245)))
            print ("")

        # break the while when stay in the same place
        if test_if_stay_same_place(80, 810, 150, 890, 1.00) :
            pushTheAction("auto", 50, 50)
            if test_if_stay_same_place(80, 810, 150, 890, 1.00) :
                break
    # return to base
    # p1.terminate()
    p2.terminate()
    print("STOP")

def kill_target(dossier) :
    print("kill_enemy")

    try :
        if (test_if_find_image(dossier, 1110, 20, 1320, 245)) :
            # s'acroupir
            dragAndDropObject("acroupir", 50, 50, "right")

            print (where_is_the_item(dossier, 1115, 25, 1325, 245))

            x, y = where_is_the_item(dossier, 1115, 25, 1325, 245)
            print("x = " + str(x) + ", y = " + str(y))

            x1, y1 = where_is_the_item("arrow", 1115, 25, 1325, 245)
            print("x1 = " + str(x1) + ", y1 = " + str(y1))

            x0 = abs(x - x1)
            y0 = abs(y - y1)
            
            if x0 > y0 :
                sum = x0
            else :
                sum = y0

            print("sum = " + str(sum))
            if (sum < 100) :
                movement(x+82, y+497, 1.1)
            elif (sum < 115) :
                movement(x+82, y+497, 1.5)
            else :
                movement(x+82, y+497, 2)

            # dois tuer l'ennemi
            # Tant que on voit le nom d'un enemi 
            while test_if_find_image("name_enemi", 570, 25, 800, 60) :
                click_gauche(1, 1265, 710)

            # ramasser ce qui est tombé
            ramasser_items()
    except :
        print ("continue")


def kill_enemy() :
    print("kill_enemy")

    try :
        if (test_if_find_image("enemy", 1110, 20, 1320, 245)) :
            # s'acroupir
            dragAndDropObject("acroupir", 50, 50, "right")

            print (where_is_the_item("enemy", 1115, 25, 1325, 245))

            x, y = where_is_the_item("enemy", 1115, 25, 1325, 245)
            print("x = " + str(x) + ", y = " + str(y))

            x1, y1 = where_is_the_item("arrow", 1115, 25, 1325, 245)
            print("x1 = " + str(x1) + ", y1 = " + str(y1))

            x0 = abs(x - x1)
            y0 = abs(y - y1)
            
            if x0 > y0 :
                sum = x0
            else :
                sum = y0

            print("sum = " + str(sum))
            if (sum < 100) :
                movement(x+82, y+497, 1.1)
            elif (sum < 115) :
                movement(x+82, y+497, 1.5)
            else :
                movement(x+82, y+497, 2)

            # dois tuer l'ennemi
            # Tant que on voit le nom d'un enemi 
            while test_if_find_image("name_enemi", 570, 25, 800, 60) :
                click_gauche(1, 1265, 710)

            # ramasser ce qui est tombé
            ramasser_items()
    except :
        print ("continue")

def ramasser_items() :
    pushTheAction("main", 50, 50)
    time.sleep(1)

    dragAndDropObject("corde", 50, 50, "right")
    dragAndDropObject("viande", 50, 50, "right")
    dragAndDropObject("peau", 50, 50, "right")

    # Fermer l'équipement
    pushTheAction("croix", 50, 50)

def click_gauche(duree_clic, x, y) :
    # Obtenez les coordonnées de la position actuelle de la souris (optionnel)
    # current_x, current_y = pyautogui.position()

    # Déplacez la souris à la position souhaitée
    pyautogui.moveTo(x, y)

    # Appuyez sur le bouton gauche de la souris
    pyautogui.mouseDown()

    # Attendez pendant la durée spécifiée
    time.sleep(duree_clic)

    # Relâchez le bouton gauche de la souris
    pyautogui.mouseUp()

def movement_haut() :
    movement(280, 650, 15)

def movement_gauche() :
    movement(190, 710, 15)

def movement_droite() :
    movement(370, 710, 15)

def movement_bas() :
    movement(280, 800, 15)

def hide_objectif() :
    # click_images("hide_objectif", 370, 135, 407, 170)
    pyautogui.moveTo(390, 156)
    time.sleep(1)
    pyautogui.click(button='left') # clic avec le bouton gauche

def hide_objectif_2() :
    # click_images("hide_objectif", 370, 135, 407, 170)
    pyautogui.moveTo(390, 192)
    time.sleep(1)
    pyautogui.click(button='left') # clic avec le bouton gauche

def remplir_eau() :
    print("Remplir les bouteilles vide et mettre les pleins dans le bar")

    movement(335, 641, 0.5)

    # Ouvre le bar
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 770) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # range le bar
    pushTheAction("order_box", 50, 50)
    
    # Ferme le bar
    pushTheAction("croix", 50, 50)

    # Remplir les capteurs de pluie avec les bouteilles vides
    # Aller au capteur de pluies
    movement(193, 675, 0.8)

    # Ouvre le capteur de pluies
    pushTheAction("gear", 50, 50)
    
    # place les bouteilles vide
    dragAndDropObject("eau_vide", 50, 50, "left")

    # prendre les bouteilles pleine
    dragAndDropObject("eau", 50, 50, "right")

    # Ferme le capteur de pluies
    pushTheAction("croix", 50, 50)

    # Aller au deuxième capteur de pluies
    movement(351, 647, 0.5)
    # Ouvre le capteur de pluies
    pushTheAction("gear", 50, 50)
    
    # place les bouteilles vide
    dragAndDropObject("eau_vide", 50, 50, "left")

    # prendre les bouteilles pleine
    dragAndDropObject("eau", 50, 50, "right")

    # Ferme le capteur de pluies
    pushTheAction("croix", 50, 50)

    # Il faut remplir le bar avec les bouteilles pleines
    # Aller vers le bar
    movement(333, 786, 0.5)

    # Ouvre le bar
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 770) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # range le bar
    pushTheAction("order_box", 50, 50)
    
    # Ferme le bar
    pushTheAction("croix", 50, 50)

def place_food_fridge() :

    # Ouvre le frigo
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le frigo
    pyautogui.moveTo(1110, 770) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # range le frigo
    pushTheAction("order_box", 50, 50)
    
    # Ferme le frigo
    pushTheAction("croix", 50, 50)



def take_water() :
    movement(360, 745, 0.80)

    movement(358, 640, 2.00)

    # prendre de l'eau dans la réserver
    # Ouvre le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("eau", 50, 50, "right")
    dragAndDropObject("eau", 50, 50, "right")
    
    # range le coffre
    pushTheAction("order_box", 50, 50)
    
    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

# We need to used this procedure after take_water()
def boire(number):
    print ("boire")

    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    click_images_side("eau", 50, 50, "left")

    for i in range (0,number) :
    # click sur UTILISER * 13 => pipi
        click_images("utiliser", 115, 720, 300, 790)

    # Fermer l'équipement
    pushTheAction("croix", 50, 50)

# We need to used this procedure after boire()
def toilette() : 
    print ("Doit aller a la toilette")

    click_images("toilette", 1100, 750, 1220, 860)

    time.sleep(8)
    
# We need to used this procedure after take_water()
def douche() :
    print ("Prende une douche")
    
    movement(241, 785, 0.5)
    
    click_images("douche", 1100, 750, 1220, 870)

    # attendre pour rentrer dans la douche
    time.sleep(2)

    click_images("confirmer", 815, 582, 1023, 650)

    # Attendre de prendre la douche
    time.sleep(12)



def take_items_reorganize() :

    # Ouvre le coffre
    pushTheAction("main", 50, 50)

    # Prendre les resources
    dragAndDropObject("herbes", 50, 50, "right")
    dragAndDropObject("herbes", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("tissus", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("corde", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)

    dragAndDropObject("piles", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("telephone", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("usb", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("lampe", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("ampoule", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("montre", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)

    dragAndDropObject("transistor", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("caoutchouc", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("roulement", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("vis", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

def go_to_coffre_tissu_corde() :
    
    movement(265, 711, 0.2)

    # Aller aux ateliers de couture
    time.sleep(0)
    movement(146, 800, 1.71)

    time.sleep(0)
    # Aller aux coffres
    movement(210, 660, 2.2)

    # Aller aux coffres
    movement(185, 743, 0.7)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("tissus", 50, 50, "left")
    dragAndDropObject("herbes", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller aux coffres pour prendre de la corde
    movement(270, 800, 0.4)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("corde", 50, 50, "left")
    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def go_to_coffre_items() :
    # Aller aux autres coffres
    movement(330, 630, 0.9)
    
    # Aller aux autres coffres
    movement(335, 780, 1.7)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("piles", 50, 50, "left")
    dragAndDropObject("telephone", 50, 50, "left")
    dragAndDropObject("usb", 50, 50, "left")
    dragAndDropObject("lampe", 50, 50, "left")
    dragAndDropObject("ampoule", 50, 50, "left")
    dragAndDropObject("montre", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller aux autres coffres
    movement(215, 772, 0.7)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("transistor", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)
    
    # Aller aux autres coffres
    movement(215, 772, 0.7)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("caoutchouc", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller aux autres coffres
    movement(300, 640, 0.3)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("roulement", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller aux autres coffres
    movement(315, 650, 0.5)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("vis", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def reorganize_items_items() :
    take_items_reorganize()
    
    

    go_to_coffre_tissu_corde()

    go_to_coffre_items()

def reorganize_items_food() :
    # Déplacer le personnage a la position ou ce trouve le coffre ou tout les objets pour s'équiper sont
    movement(225, 770, 0.3)

    # Ouvre le coffre
    pushTheAction("main", 50, 50)

    # Prendre les carottes, carottes_preparee, baies qui restent.
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")

    dragAndDropObject("baies", 50, 50, "right")
    dragAndDropObject("baies", 50, 50, "right")

    dragAndDropObject("carottes", 50, 50, "right")
    dragAndDropObject("carottes", 50, 50, "right")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

    # Doit aller au frigo
    movement(330, 770, 1.4)

    # Ouvrir le frigo
    pushTheAction("main", 50, 50)

    # Trouver les baies
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")
    dragAndDropObject("baies", 50, 50, "left")
    dragAndDropObject("baies", 50, 50, "left")
    dragAndDropObject("carottes", 50, 50, "left")
    dragAndDropObject("carottes", 50, 50, "left")
    
    dragAndDropObject("carottes", 50, 50, "right")

    # Fermer le frigo
    pushTheAction("croix", 50, 50)

def take_metal() :

    movement(313, 690, 0.25)

    pushTheAction("main", 50, 50)

    dragAndDropObject("barre_fer", 50, 50, "right")
    dragAndDropObject("barre_fer", 50, 50, "right")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def go_to_etabli_metal() :

    movement(200, 700, 1.5)

    movement(325, 638, 1.5)

def go_to_etabli_metal2() :

    movement(321, 777, 0.5)


def place_metal() :
    # Ouvrir l'etabli'
    pushTheAction("gear", 50, 50)

    dragAndDropObject("barre_fer", 50, 50, "left")
    dragAndDropObject("plaque_fer", 50, 50, "right")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def metal() :
    take_metal()

    go_to_etabli_metal()

    # place_metal()

    go_to_etabli_metal2()

    # place_metal()


def graines() :
    take_graines_charbons()

    planter_graines()

    aller_cuisiniere()

    cuisiner_carottes()


def create_equipment() :

    # Voir dans les coffres si pas des outils
    time.sleep(1)
    movement(225, 770, 0.5)

    pushTheAction("main", 50, 50)

    # range le coffre
    pushTheAction("order_box", 50, 50)

    lance = dragAndDropObject("lance", 50, 50, "right")
    hachette_full = dragAndDropObject("hachette_full", 50, 50, "right")
    hachette = dragAndDropObject("hachette", 50, 50, "right")
    pioche1 = dragAndDropObject("pioche", 50, 50, "right")
    pioche2 = dragAndDropObject("pioche", 50, 50, "right")
    pioche3 = dragAndDropObject("pioche", 50, 50, "right")
    pioche4 = dragAndDropObject("pioche", 50, 50, "right")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Je dois prendre de la pierre et du bois dans le coffre
    movement(313, 690, 0.7)

    pushTheAction("main", 50, 50)

    dragAndDropObject("pierre", 50, 50, "right")
    dragAndDropObject("pierre", 50, 50, "right")
    dragAndDropObject("bois", 50, 50, "right")
    dragAndDropObject("bois", 50, 50, "right")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    time.sleep(1)
    if hachette_full == False :
        create_object("craft", "hachette", 50, 50)
    if hachette == False :
        create_object("craft", "hachette", 50, 50)
    if pioche1 == False :
        create_object("craft", "pioche_craft", 50, 50)
    if pioche2 == False :
        create_object("craft", "pioche_craft", 50, 50)
    if pioche3 == False :
        create_object("craft", "pioche_craft", 50, 50)
    if pioche4 == False :
        create_object("craft", "pioche_craft", 50, 50)

    if lance == False :
        create_object("craft", "lance", 50, 50)
    
    # Equiper la lance
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    # Placer l'équipement
    dragAndDropObject("lance", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

    # vider le reste des ressources dans le coffre
    pushTheAction("main", 50, 50)
    
    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 770) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def create_sac_a_dos_basique() :
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    if not test_if_find_image("sac_a_dos_basique", 700, 385, 830, 490) :
        # Ferme l'équipement
        pushTheAction("croix", 50, 50)
        create_object("craft", "sac_a_dos_basique", 50, 50)
    else : 
        # Ferme l'équipement
        pushTheAction("croix", 50, 50)


def create_and_dress_suit() :
    print("create_and_dress_suit")

    # Voir dans les coffres si pas des vetements
    movement(218, 764, 0.3)
    movement(336, 779, 0.5)

    pushTheAction("main", 50, 50)

    # range le coffre
    pushTheAction("order_box", 50, 50)

    casquette = dragAndDropObject("casquette", 50, 50, "right")
    chemise = dragAndDropObject("chemise", 50, 50, "right")
    pantalon = dragAndDropObject("pantalon", 50, 50, "right")
    chaussures = dragAndDropObject("chaussures", 50, 50, "right")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)
    
    dress_suit()

    movement(215, 678, 0.5)
    take_materiaux()

    # créer un sac a dos basique si besoin
    create_sac_a_dos_basique()

    if not casquette :
        create_object("craft", "casquette", 50, 50)
        dress_suit_specific("casquette")
    if not chemise : 
        create_object("craft", "chemise", 50, 50)
        dress_suit_specific("chemise")
    if not pantalon :
        create_object("craft", "pantalon", 50, 50)
        dress_suit_specific("pantalon")
    if not chaussures : 
        create_object("craft", "chaussures", 50, 50)
        dress_suit_specific("chaussures")

    replace_materiaux()

def dress_suit_specific(dossier) :
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    # 
    dragAndDropObject(dossier, 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)


def dress_suit() :
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    # 
    dragAndDropObject("sac_a_dos_basique", 50, 50, "left")
    dragAndDropObject("casquette", 50, 50, "left")
    dragAndDropObject("chemise", 50, 50, "left")
    dragAndDropObject("pantalon", 50, 50, "left")
    dragAndDropObject("chaussures", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

def replace_materiaux() :

    # vider le reste des ressources dans le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("corde", 50, 50, "left")
    dragAndDropObject("corde", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller aux ateliers de couture
    movement(235, 635, 0.3)
    pushTheAction("main", 50, 50)

    dragAndDropObject("tissus", 50, 50, "left")
    dragAndDropObject("tissus", 50, 50, "left")
    dragAndDropObject("herbes", 50, 50, "left")
    dragAndDropObject("herbes", 50, 50, "left")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)


def take_materiaux() :
    print("take_materiaux")
    # Aller aux ateliers de couture
    time.sleep(1)
    movement(146, 800, 1.2)

    time.sleep(1)
    # Aller aux coffres
    movement(210, 660, 2.0)

    # Aller aux coffres
    time.sleep(1)
    movement(185, 743, 1.5)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("tissus", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("herbes", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller aux coffres pour prendre de la corde
    time.sleep(1)
    movement(329, 786, 0.4)

    # ouvrir le coffre
    pushTheAction("main", 50, 50)

    dragAndDropObject("corde", 50, 50, "right")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)


def equip_yourself() :
    print("equip_yourself")

    create_equipment()
    create_and_dress_suit()

    time.sleep(1)
    movement(352, 657, 0.7)
    time.sleep(1)
    movement(340, 760, 2.5)
    time.sleep(1)
    movement(337, 668, 1.0)
    time.sleep(1)
    movement(370, 700, 0.65)

    # Déplacer le personnage a la position ou ce trouve le coffre ou tout les objets pour s'équiper sont
    time.sleep(1)
    movement(225, 770, 0.5)

    # Doit aller au frigo
    time.sleep(1)
    movement(330, 770, 1.50)

    # Ouvrir le frigo
    pushTheAction("main", 50, 50)

    # Trouver les baies
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")
    dragAndDropObject("baies", 50, 50, "right")

    # Fermer le frigo
    pushTheAction("croix", 50, 50)

    # Mettre dans les poches des baies
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    dragAndDropObject("baies", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)
    
    # remettre de la vie si en dessous de 100
    while True :
        live = extract_live()
        
        try : 
            if live < 100 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,1) :
                    pushTheAction("food", 50, 50)
            else :
                break
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 
    
    # retirer de l'équipement
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)
    dragAndDropObject("baies", 50, 50, "right")

    # mettre de l'équipement
    dragAndDropObject("baies", 50, 50, "left")
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

def wait_until_next_action (x, minutes, texte) :

    subprocess.call('caffeinate &', shell=True)
    for i in range(60 * minutes, 0, -10):
        print("Nous sommes dans la xeme :", str(x+1), " itération - ", texte ," - Prochaine exécution dans", i, "secondes")
        time.sleep(10)
        if i < 100 :
            pyautogui.moveTo(200/2, 200/2)

    subprocess.call('killall caffeinate', shell=True)


def go_to_calcaire() :
    print("go_to_calcaire")

    while True :
        try : 
            hide_objectif_2()
            
            time.sleep(1)
            # Click to center to the user
            pyautogui.click(250, 850, button ='left') 

            pushTheAction_2("calcaire", 150, 150)
            # click_images("calcaire", 1, 1, 1400, 850)
            time.sleep(2)
            pushTheAction_2("marcher", 50, 50)
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 
        if (test_if_find_image("calcaire_message", 80, 804, 467, 886) ) :
            break
        else :
            print("Je ne vois pas le message, on recommence le process")
            # Need to look if you still in the colony
            if (test_if_find_image("acroupir", 1300, 830, 1350, 885)) :
                print ("je suis dans la colony")
                carpet()

                # enlever la lance si j'en ai une
                # Ouvre l'équipement
                pushTheAction("sac", 50, 50)
                time.sleep(1)

                # vider ce que j'ai dans les poches
                dragAndDropObject("lance", 50, 50, "right")
                
                # Ferme l'équipement
                pushTheAction("croix", 50, 50)

                # vider le sac 
                vider_sac()

                # vider l'équipement
                vider_equipement_poche()
                time.sleep(1)
                movement(380, 715, 0.5)
                # vider le sac 
                vider_sac()
                
                time.sleep(1)
                movement(280, 670, 0.5)
                
                time.sleep(1)
                go_to_farm()



def go_to_calcaire2() :
    # # try to avoid the pub
    # pyautogui.click(1207, 719, button ='left') 

    i = 0
    while True :
        i = i + 1
            # x1, y1 = 930 - 0, 560 - 0
            # x2, y2 = 1070, 610
        if test_if_find_image("fermer", 930, 560, 1070, 610) :
            # Je dois fermer les popups 
            pushTheAction_2("fermer", 50, 50)

            # x1, y1 = 675 - 0, 600 - 0
            # x2, y2 = 800, 640
        if test_if_find_image("plus_tard", 660, 590, 810, 645) :
            # Je dois fermer les popups 
            pushTheAction_2("plus_tard", 50, 50)
        
        if i > 8 : 
            break

    # pyautogui.click(200, 200, button ='left') 
    # pushTheAction("calcaire", 50, 50)

    # Need to test if you return or not to home
    while True :
        # pushTheAction("home", 10, 10)
        pushTheAction_2("calcaire", 150, 150)

        try : 
            time.sleep(2)
            pushTheAction_2("marcher", 50, 50)
            # pushTheAction_2("courir", 50, 50)
            break
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

def go_to_farm() :
    print("go_to_farm")
    # je dois équipper mon personnage
    equip_yourself()

    # Quitter la zone pour aller farmer, après avoir mis dans le recycleur
    # Déplacer le personnage vers la position pour partir
    movement(200, 740, 1)
    movement(200, 800, 7)

    time.sleep(5)

    go_to_calcaire()


def create_object(dossier, object, x_plus, y_plus) :
    screenshot = read_screen()

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            pyautogui.moveTo(x/2, y/2)
            pyautogui.doubleClick(button='left') # @bouton gauche
            find_image = True
            break

    time.sleep(1)
    if find_image == True  :
        if object == 'hachette' :    
            # click sur le tab des outils
            pyautogui.moveTo(290, 745)
            pyautogui.click(button='left')

            pyautogui.moveTo(200, 250)
            pyautogui.click(button='left')
        elif object == 'pioche_craft' :
            # click sur le tab des outils
            pyautogui.moveTo(290, 745)
            pyautogui.click(button='left')

            pyautogui.moveTo(350, 250)
            pyautogui.click(button='left')
        elif object == 'lance' :
            # click sur le tab des outils
            pyautogui.moveTo(395, 745)
            pyautogui.click(button='left')

            pyautogui.moveTo(200, 250)
            pyautogui.click(button='left')
        elif object == 'casquette' :
            # click sur le tab des vêtements
            pyautogui.moveTo(500, 745)
            pyautogui.click(button='left')

            pyautogui.moveTo(350, 250)
            pyautogui.click(button='left')
        elif object == 'chemise' :
            # click sur le tab des vêtements
            pyautogui.moveTo(500, 745)
            pyautogui.click(button='left')

            pyautogui.moveTo(500, 250)
            pyautogui.click(button='left')
        elif object == 'pantalon' :
            # click sur le tab des vêtements
            pyautogui.moveTo(500, 745)
            pyautogui.click(button='left')
            
            pyautogui.moveTo(640, 250)
            pyautogui.click(button='left')
        elif object == 'chaussures' :
            # click sur le tab des vêtements
            pyautogui.moveTo(500, 745)
            pyautogui.click(button='left')

            pyautogui.moveTo(770, 250)
            pyautogui.click(button='left')
        elif object == 'sac_a_dos_basique' :
            # click sur le tab des vêtements
            pyautogui.moveTo(500, 745)
            pyautogui.click(button='left')

            pyautogui.moveTo(200, 250)
            pyautogui.click(button='left')
        
        time.sleep(1)
        pushTheAction("creer", 50, 50)
        time.sleep(1)

        # click sur le tab du multiple
        pyautogui.moveTo(190, 745)
        pyautogui.click(button='left')

        # need to replace the cursor on the top if it's sac_a_dos_basique
        if object == "sac_a_dos_basique" :
            x, y = 364, 272
            # Clique au plus haut sur le sac_a_dos_basique
            pyautogui.click(x, y, button ='left') 

            # Bouger vers le haut
            pyautogui.dragRel(x, 565, duration=1, button='left')

            time.sleep(2)

            # clique sur la hachette
            dragAndDropObject("hachette", 50, 50, "left")

        if inventory_full_after_craft("inventory_full_after_craft", 50, 50) :
            time.sleep(1)
            pushTheAction("croix", 50, 50)
            return "Inventory_full"

        time.sleep(1)
        pushTheAction("croix", 50, 50)

    return dossier + "_create"

def inventory_full(dossier, x_plus, y_plus) :
    screenshot = read_screen()

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            find_image = True
            break

    return find_image


def need_tools(dossier, x_plus, y_plus) :
    screenshot = read_screen()

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            find_image = True
            break

    if find_image :
        return create_object("craft", "pioche_craft", 50, 50)


def inventory_full_after_craft(dossier, x_plus, y_plus) :

    screenshot = read_screen()

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            find_image = True
            break

    return find_image

def back_to_home() :
    print ("return to home")

    time.sleep(1)
    
    while True :
        try : 
            if (test_if_find_image("lieu_actuel_calcaire", 82, 807, 480, 890)) :
                hide_objectif_2()

                time.sleep(1)
                # Click to center to the user
                pyautogui.click(250, 850, button ='left') 

                pushTheAction_2("home", 200, 200)
                time.sleep(2)
                pushTheAction_2("marcher", 50, 50)
            else :
                # We are in the field need to go out
                run_outside_of_the_field()

        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 
        if (test_if_find_image("home_message", 80, 804, 467, 886) ) :
            break
        else :
            print("Je ne vois pas le message, on recommence le process")


def back_to_home2() :
    print ("return to home")
     # je dois retourner a la maison
    time.sleep(7)

    # Je dois fermer les popups 
    pushTheAction_2("fermer", 50, 50)

    # Je dois fermer les popups 
    pushTheAction_2("plus_tard", 50, 50)

    # Need to test if you return or not to home
    while True :
        try : 
            # pushTheAction("home", 10, 10)
            pushTheAction_2("home", 200, 200)
            time.sleep(2)
            pushTheAction_2("marcher", 50, 50)
            # pushTheAction_2("courir", 50, 50)
            break
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

def test_if_stay_same_place(x1, y1, x2, y2, threshold=0.01):

    # Je ne sais pas pourquoi mais on doit multiplier les valeurs par deux.
    x1 = x1*2
    y1 = y1*2
    x2 = x2*2
    y2 = y2*2

    # Capture the initial screenshot
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Wait for 1 seconds
    time.sleep(1)

    # Capture the second screenshot
    screenshot2 = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    screenshot2 = cv2.cvtColor(np.array(screenshot2), cv2.COLOR_RGB2BGR)

    # Compare the two screenshots
    difference = cv2.subtract(screenshot, screenshot2)
    result = not np.any(difference)

    # # Affichage des captures d'écran
    # concatenated_images = np.concatenate((screenshot, screenshot2), axis=1)
    # cv2.imshow('Screenshots comparison', concatenated_images)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    if not result:
        # Calculate the percentage of difference
        num_pixels = difference.shape[0] * difference.shape[1] * difference.shape[2]
        diff_percent = np.sum(difference) / num_pixels

        # Check if the difference is greater than the threshold
        print("diff_percent" + str(diff_percent))
        print("threshold" + str(threshold))
        if diff_percent > threshold:
            result = False
        else:
            result = True

    return result

def auto() :
    while True :
        try : 
            if test_if_stay_same_place(80, 810, 150, 890, 1.00) :
                pushTheAction("auto", 50, 50)
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 


def take_everything() :
    while True :
        try : 
            # if test_if_stay_same_place(550, 330, 800, 670, 1.00) :
            #     movement(50, 670, 1)
            #     pushTheAction("auto", 50, 50)

            # if test_if_find_image_90("auto", 80, 820, 150, 890) :
            #     pushTheAction("auto", 50, 50)
            #     pyautogui.moveTo((100), 100)


            if test_if_find_image("main", 1100, 745, 1230, 875) :
                pyautogui.click(1160, 800, button ='left') 

                # to let the time to open the box  
                # time.sleep(5)

                # Si on est dans le cas d'une caisse ou d'un zombie
                if test_if_find_image("inventory", 90, 90, 340, 160) :
                    # On doit tout prendre dans l'inventaire
                    pyautogui.click(830, 755, button ='left') 
                    if test_if_find_image("croix", 1280, 15, 1360, 210) :
                        # Fermer l'inventaire
                        pushTheAction("croix", 50, 50)

                if test_if_find_image("croix", 1280, 15, 1360, 210) :
                    # Fermer l'inventaire
                    pushTheAction("croix", 50, 50)
             
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 
    

def farm() :
    print ("Farme the field")
    p0 = multiprocessing.Process(target=auto)
    p1 = multiprocessing.Process(target=live_in_the_field)
    p2 = multiprocessing.Process(target=take_everything)
    p3 = multiprocessing.Process(target=faire_pipi)
    
    p0.start()
    p1.start()
    p3.start()
    # p2.start()
    i = 0
    j = 0 
    back_home = False
    while True :
        print ("p1 is alive = "+ str(p1.is_alive()))

        try : 
            if not p1.is_alive() : 
                break
            

            if need_tools("need_tools", 50, 50) == "Inventory_full" :
                # back to home
                back_home =  True
                break
            if inventory_full("inventory_full", 0, 0) :
                # back to home
                back_home =  True
                break
            if inventory_full("no_more_items", 0, 0) :
                # back to home
                back_home =  True
                break
            if test_if_stay_same_place(550, 330, 800, 670, 1.00) :
                movement(50, 670, 0.3)
                pushTheAction("auto", 50, 50)
            if test_if_still_places("entrer") :
                pushTheAction_2("entrer", 50, 50)
                time.sleep(7)

        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

    p0.terminate()
    p1.terminate()
    # p2.terminate()
    p3.terminate()

    p2 = multiprocessing.Process(target=stay_in_live)
    p2.start()
    # Je n'ai plus de nouriture je dois fuir
    run_outside_of_the_field()
    p2.terminate()

    return back_home


def farm2() :
    print ("Farme")

    p1 = multiprocessing.Process(target=live_in_the_field)

    p1.start()

    back_home = False
    while True :
        print ("p1 is alive = "+ str(p1.is_alive()))
        search()    
        time.sleep(1)
        
        go_to_the_coffre()
        try : 
            if not p1.is_alive() : 
                break

            if need_tools("need_tools", 50, 50) == "Inventory_full" :
                # back to home
                back_home =  True
                break
            if inventory_full("inventory_full", 0, 0) :
                # back to home
                back_home =  True
                break
            if inventory_full("no_more_items", 0, 0) :
                # back to home
                back_home =  True
                break
            if test_if_stay_same_place(550, 330, 800, 670, 1.00) :
                movement(50, 670, 0.3)
                # pushTheAction("auto", 50, 50)
            if test_if_still_places("entrer") :
                pushTheAction_2("entrer", 50, 50)
                time.sleep(7)

        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

    p1.terminate()
    # p2.terminate()

    p2 = multiprocessing.Process(target=stay_in_live)
    p2.start()
    # Je n'ai plus de nouriture je dois fuir
    run_outside_of_the_field()
    p2.terminate()

    return back_home

def farm_2() :
    print ("Farme the field")
    p1 = multiprocessing.Process(target=live_in_the_field)
    p2 = multiprocessing.Process(target=stay_in_live)
    p1.start()
    time.sleep(1)
    # Push the button to automate the action 
    pushTheAction("auto", 50, 50)

    time.sleep(1)

    while True :
        live = extract_live()
        print ("p1 is alive = "+ str(p1.is_alive()))
        print ("p2 is alive = "+ str(p2.is_alive()))
        try : 
            if not p1.is_alive() : 
                break
            if live < 69 :
                break

            if need_tools("need_tools", 50, 50) == "Inventory_full" :
                break

            if inventory_full("inventory_full", 0, 0) :
                break

            if inventory_full("no_more_items", 0, 0) :
                break
            if test_if_still_places("entrer") :
                pushTheAction_2("entrer", 50, 50)
                time.sleep(7)

        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

        # # De temps en temps on sort de la zone il faut pouvoir y rentrer à nouveau
        # pushTheAction("entrer", 50, 50)
            
    p1.terminate()
    
    p2.start()
    # Je n'ai plus de nouriture je dois fuir
    run_outside_of_the_field()
    p2.terminate()
    print ("p1 is alive = "+ str(p1.is_alive()))
    print ("p2 is alive = "+ str(p2.is_alive()))
    if p1.is_alive() :
        p1.terminate()
    if p2.is_alive() :
        p2.terminate()

def run_outside_of_the_field() :
    try : 
        movement(50, 670, 20)   
    except Exception as e:
        # afficher l'exception, mais ne rien faire d'autre
        print(e) 

def farm_field() :
    print ("farm_field")
    back_home = False
    i = 1
    while stay_in_battle() :
        if i > 3 :
            break
        else :
            try : 
                # Click to center to the user
                pyautogui.click(250, 850, button ='left') 

                # Pour fermer les pubs
                pushTheAction_2("plus_tard", 50, 50)
                time.sleep(1)
                pushTheAction_2("fermer", 50, 50)
                time.sleep(1)
                while test_if_inside_field("entrer") :
                    # Cliquer sur ENTRER
                    pushTheAction_2("entrer", 50, 50)
                    time.sleep(7)

            except Exception as e:
                # afficher l'exception, mais ne rien faire d'autre
                print(e) 

            time.sleep(1)
            back_home = farm()
        if back_home :
            break
        time.sleep(10)

        # Pour fermer les pubs
        try : 
            pushTheAction_2("plus_tard", 50, 50)
            time.sleep(1)
            pushTheAction_2("fermer", 50, 50)
            time.sleep(1)
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

        i = i + 1

def farm_and_back_to_home() :
    farm_field()

    # Need to take all items left on the field

    back_to_home()

def remplir_etablis() :

    print("Remplir les établis de bois et de pierre")

    movement(220, 760, 1)

    # Prendre dans le coffre le minerais de fer
    # Ouvrir le coffre
    pushTheAction("gear", 50, 50)

    dragAndDropObject("minerai_fer", 50, 50, "right")
    dragAndDropObject("minerai_fer", 50, 50, "right")
    dragAndDropObject("charbons", 50, 50, "right")
    dragAndDropObject("charbons", 50, 50, "right")


    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    movement(313, 680, 1)

    # Ouvrir la cabane
    pushTheAction("gear", 50, 50)

    # Prendre 2 stack de bois
    dragAndDropObject("bois", 50, 50, "right")
    # dragAndDropObject("bois", 50, 50, "right")

    # Prendre 2 stack de pierre
    dragAndDropObject("pierre", 50, 50, "right")
    dragAndDropObject("pierre", 50, 50, "right")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # se diriger vers la porte ou se trouve les établis.
    movement(240, 715, 1.25)

    # Remonter l'allée jusqu'au établis de bois
    movement(217, 675, 2.8)

    # Aller a l'établi le plus en haut a gauche
    movement(240, 685, 0.50)

    # 
    remplir_etabli_avec("planches", "bois", 50, 50)

    # Aller a l'établi plus bas
    movement(320, 745, 0.50)

    # 
    remplir_etabli_avec("planches", "bois", 50, 50)

    # Aller a l'établi de pierre
    movement(348, 742, 1.10)
    # 
    # remplir_etabli_avec("blocs", "pierre", 50, 50)

    # Aller a l'établi de pierre
    time.sleep(1)
    movement(310, 686, 0.50)
    # 
    # remplir_etabli_avec("blocs", "pierre", 50, 50)

    # Monter pour prendre le charbon dans les feux
    time.sleep(1)
    movement(220, 685, 0.75)

    # Ouvrir
    pushTheAction("gear", 50, 50)

    # Prendre le charbon qui a été fait.
    time.sleep(1)
    dragAndDropObject("charbons", 50, 50, "right")
    
    dragAndDropObject("charbons_sac", 50, 50, "left")

    # Mettre des nouvelles planches dans le feu
    dragAndDropObject("planches_sac", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Monter pour prendre le charbon dans les feux
    movement(320, 675, 0.50)

    # Ouvrir
    pushTheAction("gear", 50, 50)

    # # # Prendre le charbon qui a été fait.
    # time.sleep(1)
    # dragAndDropObject("charbons", 50, 50, "right")
    
    # dragAndDropObject("charbons_sac", 50, 50, "left")

    # # Mettre des nouvelles planches dans le feu
    # dragAndDropObject("planches_sac", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    time.sleep(1)
    # Aller au fourneau de haut a droite
    movement(280, 620, 1.25)

    # Ouvrir le coffre
    time.sleep(1)
    pushTheAction("gear", 50, 50)

    dragAndDropObject("barre_fer", 50, 50, "right")
    dragAndDropObject("charbons", 50, 50, "right")

    dragAndDropObject("minerai_fer_sac", 50, 50, "left")
    dragAndDropObject("charbons_sac", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # # Aller au fourneau de haut a gauche
    time.sleep(1)
    movement(240, 748, 0.90)

    # Ouvrir le coffre
    time.sleep(1)
    pushTheAction("gear", 50, 50)

    dragAndDropObject("barre_fer", 50, 50, "right")
    dragAndDropObject("charbons", 50, 50, "right")

    dragAndDropObject("charbons_sac", 50, 50, "left")
    dragAndDropObject("minerai_fer_sac", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def herbes() :
    # prendre de l'herbe
    # coffre de rangement

    # Ouvrir le coffre
    pushTheAction("gear", 50, 50)

    dragAndDropObject("herbes", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("herbes", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)
    dragAndDropObject("tissus", 50, 50, "right")
    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    time.sleep(1)
    # Aller aux ateliers de couture
    movement(146, 800, 1.75)

    time.sleep(1)
    # Aller aux ateliers de couture
    movement(210, 660, 3.1)

    # Ouvrir le coffre
    time.sleep(1)
    pushTheAction("gear", 50, 50)

    dragAndDropObject("tissus", 50, 50, "right")
    dragAndDropObject("herbes_sac", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller aux ateliers de couture
    movement(170, 755, 0.50)

    # Ouvrir le coffre
    time.sleep(1)
    pushTheAction("gear", 50, 50)

    dragAndDropObject("tissus", 50, 50, "right")
    dragAndDropObject("herbes_sac", 50, 50, "left")
    # dragAndDropObject("tissus_epais", 50, 50, "right")
    # dragAndDropObject("tissus_sac", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def remplir_etabli_avec(resource_rafinee, resource_brut, x_plus, y_plus) :

    # Ouvrir l'établi
    pushTheAction("gear", x_plus, y_plus)

    # Vider l'établi
    time.sleep(1)
    dragAndDropObject(resource_rafinee, x_plus, y_plus, "right")

    # Mettre le bois
    dragAndDropObject(resource_brut, x_plus, y_plus, "left")

    # Ferme l'établi
    pushTheAction("croix", x_plus, y_plus)

def push_home_button(x, y, x_plus, y_plus) :

    x = x + x_plus
    y = y + y_plus
    pyautogui.click(x/2, y/2, button ='left') 
    time.sleep(1)
    dragAndDropObject("voyager", 50, 50, "right")

def prendre_equipement_used() :
    movement(225, 770, 0.5)
    pushTheAction("main", 50, 50)

    # dragAndDropObject("lance", 50, 50, "right")

    # dragAndDropObject("hachette", 50, 50, "right")
    # dragAndDropObject("hachette", 50, 50, "right")
    # dragAndDropObject("hachette", 50, 50, "right")

    # dragAndDropObject("pioche", 50, 50, "right")
    # dragAndDropObject("pioche", 50, 50, "right")
    # dragAndDropObject("pioche", 50, 50, "right")

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def vider_equipement_poche() :

    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    # vider ce que j'ai dans les poches
    dragAndDropObject("lance", 50, 50, "right")
    dragAndDropObject("casquette", 50, 50, "right")
    dragAndDropObject("chemise", 50, 50, "right")
    dragAndDropObject("pantalon", 50, 50, "right")
    dragAndDropObject("chaussures", 50, 50, "right")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

def after_vider_equipement_poche() : 
    # vider le reste dans le coffre recyclage
    time.sleep(1)
    movement(380, 715, 0.9)

    time.sleep(1)
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 750) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # range le coffre
    pushTheAction("order_box", 50, 50)
    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def vider_nouriture_poche() :

    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    # vider ce que j'ai dans les poches
    dragAndDropObject("baies", 50, 50, "right")
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

def vider_sac() :
    # Je dois vider mon sac
    # vider le bois les pierres dans la cabane
    movement(313, 690, 0.25)

    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 770) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # vider le reste dans le coffre
    time.sleep(1)
    movement(225, 770, 0.5)

    time.sleep(1)
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 750) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # range le coffre
    pushTheAction("order_box", 50, 50)
    # Ferme le coffre
    pushTheAction("croix", 50, 50)


def extract_live() :
    now = datetime.datetime.now()
    # print("La date et l'heure actuelles sont :", now)
    # Sauvegarde la capture d'écran avant le raise de l'erreur
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    x1, y1, x2, y2 = 680, 60, 760, 110
    cropped_screenshot = screenshot[y1:y2, x1:x2, :]

    cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/live.png", cropped_screenshot)

    # Chargement de l'image
    img = cv2.imread('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/live.png')

    # Utiliser PyTesseract pour extraire le texte
    text = pytesseract.image_to_string(img, config='--psm 7')

    # Convertir le texte en nombre
    try :
        nombre = int(text)
        print('Le nombre est :', nombre)
    except Exception as e:
        # afficher l'exception, mais ne rien faire d'autre
        print(e)
        nombre = "59"

    now = datetime.datetime.now()
    # print("La date et l'heure actuelles sont :", now)
    print (str(nombre))
    return nombre


def avoid_litle_screen() :
    print("Test")
    pyautogui.hotkey('command', 'tab')
    time.sleep(2)
    print("Test")
    pyautogui.hotkey('command', 'tab')
    time.sleep(2)
    pyautogui.click(800, 400, button ='left') 


def startApplication() :


    subprocess.Popen(["open", "-a", "Last Day On Earth: Survival.app"])

    # Doit attendre que l'application se lance
    time.sleep(15)

    pyautogui.click(1400/2, 1160/2, button ='left') 

    loading_screen = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/loading_screen.png", cv2.IMREAD_GRAYSCALE)
    # Attendre jusqu'au moment ou l'application est chargée

    avoid_litle_screen()

    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png')
        time.sleep(1)
        # Charger l'image en couleur
        screenshot = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png", cv2.IMREAD_GRAYSCALE)

        result = cv2.matchTemplate(screenshot, loading_screen, cv2.TM_CCOEFF_NORMED)

        # Trouver la correspondance la plus élevée
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        print("max_val = " + str(max_val))

        # Si la correspondance est supérieure à un certain seuil, simuler un clic à ce point
        if max_val >= 0.5:
            print("Loading screen is still visible.")
        else:
            print("Loading screen is no longer visible.")
            break


    print(sys.version)


def enterCamp() :
    screenshot = pyautogui.screenshot()
    screenshot.save('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png')
    time.sleep(1)
    # Charger l'image en couleur
    screenshot = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png", cv2.IMREAD_GRAYSCALE)

    map_screen = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/map_screen.png", cv2.IMREAD_GRAYSCALE)

    result = cv2.matchTemplate(screenshot, map_screen, cv2.TM_CCOEFF_NORMED)
    # Trouver la correspondance la plus élevée
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print("max_val = " + str(max_val))

    # Si la correspondance est supérieure à un certain seuil, simuler un clic à ce point
    if max_val >= 0.5:
        print("Need to click on the button 'Enter' ")
        pushTheAction_2("entrer", 50, 50)
        # pyautogui.click(1400/2, 1160/2, button ='left') 
        time.sleep(10)

    else:
        print("We are not on the map screen")
    

def testImage(images) :
    # Sauvegarde de l'ecran
    screenshot = pyautogui.screenshot()
    screenshot.save('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png')

    # Charger les images
    template = cv2.imread(images, cv2.IMREAD_GRAYSCALE)
    screenshot = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png", cv2.IMREAD_GRAYSCALE)

    # Appliquer la fonction de détection de formes
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    # # Duplicate the screenshot image
    # screenshot2 = screenshot.copy()

    # # Draw a red square at position X = 100, Y = 100
    # # x, y = 2100, 1350
    # side = 100
    # color = (0, 0, 255)
    # thickness = 5

    # _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # print("max_val = " + str(max_val))
    # x, y = max_loc
    # x = x + 50
    # y = y + 50

    # cv2.rectangle(screenshot2, (x - side, y - side), (x + side, y + side), color, thickness)

    # # Save the duplicate image with the red square
    # cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot2.png", screenshot2)

    return cv2.minMaxLoc(result)

def movement(x_mov, y_mov, duration_mov) :
    x, y = 280, 715
    # Clique au centre du paddle
    pyautogui.click(x, y, button ='left') 

    # Bouger
    pyautogui.dragRel(x_mov-x, y_mov-y, duration=duration_mov, button='left')
    return

def movement_0(x_mov, y_mov, duration_mov) :
    directory = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/nav_buttons'

    for filepath in glob.glob(os.path.join(directory, '*.png')):
        # Trouver la correspondance la plus élevée
        _, max_val, _, max_loc = testImage(filepath)
        print("max_val = " + str(max_val))
        if max_val >= 0.8:
            x, y = max_loc
            x = x + 50
            y = y + 50

            # Clique au centre du paddle
            print("x = "+ str(x) + " y = "+ str(y) )
            pyautogui.click(x/2, y/2, button ='left') 

            # Bouger
            pyautogui.dragRel(x_mov, y_mov, duration=duration_mov, button='left')
            print("L'image a été trouvé = movement_0")
            return

    # Sauvegarde la capture d'écran avant le raise de l'erreur
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    x1, y1 = 422 - 50, 1314 - 50
    x2, y2 = x1 + 350, y1 + 350
    cropped_screenshot = screenshot[y1:y2, x1:x2, :]

    i = 1
    while os.path.exists("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/nav_buttons/nav_button_" + str(i) + ".png"):
        i += 1
    cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/nav_buttons/nav_button_" + str(i) + ".png", cropped_screenshot)

    raise Exception("PaddleNotDetectable")

class ImageNotFound(Exception):
    def __init__(self, dossier):
        self.dossier = dossier
        self.message = "ImageNotFound: " + self.dossier
        super().__init__(self.message)

def read_screen():
    screenshot = pyautogui.screenshot()
    screenshot_path = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png'
    screenshot.save(screenshot_path)
    return cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)

def pushTheAction (dossier, x_plus, y_plus) :
    
    x, y = 2220 - 50, 1550 - 50

    if dossier == "gear"  :
        x, y = 2220 - 50, 1550 - 50
    if dossier == "toilette"  :
        x, y = 2220 - 50, 1550 - 50
    elif dossier == "main"  :
        x, y = 2220 - 50, 1550 - 50
    elif dossier == "croix"  :
        x, y = 2630 - 50, 295 - 50
    elif dossier == "order_box" :
        x, y = 1950 - 50, 1500 - 50
    elif dossier == "calcaire" :
        x, y = 280 - 50, 1420 - 50
    elif dossier == "marcher" :
        x, y = 2000 - 50, 1200 - 50
    elif dossier == "entrer" :
        x, y = 1400 - 50, 1160 - 50
    elif dossier == "auto" :
        x, y = 220 - 50, 1690 - 50
    elif dossier == "food" :
        x, y = 2540 - 50, 1180 - 50
    elif dossier == "food_2" :
        x, y = 2382 - 50, 1224 - 50
    elif dossier == "home" :
        x, y = 2340 - 50, 440 - 50
    elif dossier == "sac" :
        x, y = 2120 - 50, 1680 - 50
    elif dossier == "sac_map" :
        x, y = 1170*2 - 50, 850*2 - 50
    elif dossier == "creer" :
        x, y = 2100 - 50, 1450 - 50

    x = x + x_plus
    y = y + y_plus
    pyautogui.click(x/2, y/2, button ='left') 

def test_if_inside_field(dossier) :

    # Capture d'écran partielle
    x1, y1, x2, y2 = 900, 700, 1000, 800
    screenshot = np.array(pyautogui.screenshot(region=(x1, y1, x2, y2)))

    cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/entrer.png", screenshot)

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        # Lecture de l'image modèle
    # Lecture de l'image modèle
    # template = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/template.png")
        template = cv2.imread(filepath)

        # Afficher la taille de l'image
        print("dossier : ", dossier)
        # print("Taille de l'image template : ", template.shape)
        # print("Taille de l'image screenshot : ", screenshot.shape)

        # Conversion en niveaux de gris
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Récupération des dimensions de l'image modèle
        h, w = gray_template.shape

        # Correspondance de modèle
        result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)

        # Récupération de la position de la correspondance maximale
        _, _, min_loc, max_loc = cv2.minMaxLoc(result)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        print (str(max_loc))
        print (str(min_loc))
        print (str(max_val))

        if max_val >= 0.8:
            find_image = True
            break

        # # Affichage de la correspondance maximale
        # cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

        # # Affichage de l'image résultat
        # cv2.imshow("Result", screenshot)
        # cv2.waitKey(0)

    return find_image

def test_if_outside_field(dossier) :

    screenshot = read_screen()
    screenshot = np.array(screenshot)
    x1, y1, x2, y2 = 140, 85, 350, 125
    cropped_screenshot = screenshot[y1:y2, x1:x2, :]

    cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/carte_globale.png", cropped_screenshot)

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            find_image = True
            break
    
    return find_image

def boite_inconue() :

    pushTheAction_2("boite_inconnue", 50, 50)
    
    x, y = 900, 170
    # Clique le plus à droite possible
    pyautogui.click(x, y, button ='left') 

    # Bouger à gauche
    pyautogui.dragRel(80-x, 170-y, duration=1, button='left')
    
    x, y = 900, 170
    # Clique le plus à droite possible
    pyautogui.click(x, y, button ='left') 

    # Bouger à gauche
    pyautogui.dragRel(80-x, 170-y, duration=1, button='left')

    time.sleep(1)

    pushTheAction_2("gratuit", 50, 50)

    time.sleep(1)

    pushTheAction_2("regarder_video", 50, 50)

    time.sleep(1)
    try :
        pushTheAction_2("accepte", 50, 50)
    except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

    time.sleep(60)

    try :
        pushTheAction_2("croix_pub", 50, 50)
    except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

    time.sleep(15)

    try :
        pushTheAction_2("croix_pub", 50, 50)
    except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

    time.sleep(2)

    try :
        pushTheAction_2("redemarrer", 50, 50)
    except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

    time.sleep(8)

    pushTheAction_2("prendre", 50, 50)

    time.sleep(4)

    pushTheAction_2("fermer_pub", 50, 50)

    time.sleep(1)

    pushTheAction_2("fermer", 50, 50)



def pushTheAction_2 (dossier, x_plus, y_plus) :
    screenshot = read_screen()

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            print("Click aux coordonées x = " + str(x/2) + " y = " + str(y/2))
            pyautogui.click(x/2, y/2, button ='left') 
            find_image = True
            break

    # if not find_image:
    #     # Sauvegarde la capture d'écran avant le raise de l'erreur
    #     screenshot = pyautogui.screenshot()
    #     screenshot = np.array(screenshot)

    #     x1, y1 = 422 - 50, 1314 - 50
    #     x2, y2 = 10, 10
    #     if dossier == "gear"  :
    #         x1, y1 = 2220 - 50, 1550 - 50
    #         x2, y2 = x1 + 350, y1 + 350
    #     elif dossier == "main"  :
    #         x1, y1 = 2220 - 50, 1550 - 50
    #         x2, y2 = x1 + 350, y1 + 350
    #     elif dossier == "calcaire" :
    #         x1, y1 = 160 - 50, 1280 - 50
    #         x2, y2 = x1 + 350, y1 + 350
    #     elif dossier == "home" :
    #         x1, y1 = 2180 - 50, 300 - 50
    #         x2, y2 = x1 + 350, y1 + 350
    #     elif dossier == "marcher" :
    #         x1, y1 = 930 - 0, 560 - 0
    #         x2, y2 = 1070, 610
    #     elif dossier == "courir" :
    #         x1, y1 = 725 - 0, 570 - 0
    #         x2, y2 = 907, 720
    #     elif dossier == "fermer" :
    #         x1, y1 = 930 - 0, 560 - 0
    #         x2, y2 = 1070, 610
    #     elif dossier == "plus_tard" :
    #         x1, y1 = 675 - 0, 600 - 0
    #         x2, y2 = 800, 640
    #     elif dossier == "croix_pub" : 
    #         x1, y1 = 1291 - 0, 20 - 0
    #         x2, y2 = 1350, 66
    #     elif dossier == "prendre" : 
    #         x1, y1 = 933 - 0, 536 - 0
    #         x2, y2 = 1058, 569
    #     elif dossier == "boite_inconnue" : 
    #         x1, y1 = 876*2 - 0, 831*2 - 0
    #         x2, y2 = 923*2, 869*2
    #     elif dossier == "entrer" : # possible that it's not working because the screen moved
    #         x1, y1 = 600*2 - 0, 545*2 - 0
    #         x2, y2 = 830*2, 630*2

    #     cropped_screenshot = screenshot[y1:y2, x1:x2, :]

    #     if dossier == "fermer" :
    #         print("Pas de popup à fermer, continuer")
    #     elif dossier == "plus_tard" :
    #         print("Pas de popup à mettre plus tard, continuer")
    #     else :
    #         print("Image not found : " + dossier)
    #         i = 1
    #         while os.path.exists("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/" + dossier + "/" + dossier + "_" + str(i) + ".png"):
    #             i += 1
    #         cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/" + dossier + "/" + dossier + "_" + str(i) + ".png", cropped_screenshot)

    #         raise ImageNotFound(dossier)
        
        

def pushTheAction_3 (dossier, x_plus, y_plus) :
    # Sauvegarde de l'ecran
    screenshot = pyautogui.screenshot()
    screenshot.save('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png')
    screenshot = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png", cv2.IMREAD_GRAYSCALE)

    # Charger les images
    directory = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/'+dossier

    find_image = False
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        # Appliquer la fonction de détection de formes
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)

        # Trouver la correspondance la plus élevée
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        print("max_val = " + str(max_val))
        x, y = max_loc
        x = x + x_plus
        y = y + y_plus

        if max_val >= 0.8:
            # Clique 
            print("x = "+ str(x) + " y = "+ str(y) )
            pyautogui.click(x/2, y/2, button ='left') 

            find_image = True
            break

    if (find_image) :
        print("L'image a été trouvé = " + dossier)
    else :
        raise Exception("ImageNotFound = " + dossier)

def click_images_side(dossier, x_plus, y_plus, side) :
    screenshot = read_screen()
    if side == 'left':
        screenshot = screenshot[:, :screenshot.shape[1]//2]
    elif side == 'right':
        screenshot = screenshot[:, screenshot.shape[1]//2:]
    else:
        raise ValueError('Invalid side parameter value. Must be "left" or "right".')
    # Do the rest of the code for drag and drop with the selected side of the screenshot

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            print(dossier)
            if side == 'left':
                print("x = " + str((x/2)) + " y = " + str(y/2) )
                pyautogui.moveTo((x/2), y/2)  # ajustement pour la partie droite de l'écran
            else : 
                print("x = " + str((x/2) + screenshot.shape[1]//2) + " y = " + str(y/2) )
                pyautogui.moveTo((x/2) + screenshot.shape[1]//2, y/2)  # ajustement pour la partie droite de l'écran
            
            pyautogui.click(button='left') # clic avec le bouton gauche

            find_image = True
            break

def dragAndDropObject(dossier, x_plus, y_plus, side) :
    screenshot = read_screen()
    if side == 'left':
        screenshot = screenshot[:, :screenshot.shape[1]//2]
    elif side == 'right':
        screenshot = screenshot[:, screenshot.shape[1]//2:]
    else:
        raise ValueError('Invalid side parameter value. Must be "left" or "right".')
    # Do the rest of the code for drag and drop with the selected side of the screenshot

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            print(dossier)
            if side == 'left':
                print("x = " + str((x/2)) + " y = " + str(y/2) )
                pyautogui.moveTo((x/2), y/2)  # ajustement pour la partie droite de l'écran
            else : 
                print("x = " + str((x/2) + screenshot.shape[1]//2) + " y = " + str(y/2) )
                pyautogui.moveTo((x/2) + screenshot.shape[1]//2, y/2)  # ajustement pour la partie droite de l'écran
            
            pyautogui.doubleClick(button='left') # double clic avec le bouton gauche
            find_image = True
            break
    return find_image

def take_graines_charbons() :
    # Aller dans le coffre
    movement(220, 750, 0.4)

    # Ouvre le coffre
    time.sleep(1)
    pushTheAction("main", 50, 50)

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Prendre les graines
    dragAndDropObject("graines", 50, 50, "right")
    dragAndDropObject("graines", 50, 50, "right")

    # Prendre le nécessaire pour cuire
    dragAndDropObject("charbons", 50, 50, "right")
    dragAndDropObject("carottes", 50, 50, "right")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def carpet() :
    # push_home_button(2600, 500, 10, 10)
    # time.sleep(1)
    # click_images("home_button", 1264, 231, 1330, 300)
    # time.sleep(2)
    # click_images("voyager", 810, 445, 1015, 512)
    # time.sleep(9)
    # click_images("home_button", 1264, 231, 1330, 300)
    # time.sleep(2)
    # click_images("voyager", 810, 445, 1015, 512)
    # time.sleep(9)
    go_to_colonie()

    go_to_home()

def planter_graines() :
    # Aller vers les champs
    movement(300, 750, 3)

    # Aller vers les champs
    movement(330, 715, 0.5)

    # Ouvrir le premier champ
    time.sleep(1)
    pushTheAction("gear", 50, 50)

    # reprendre les carottes plantées
    dragAndDropObject("carottes", 50, 50, "right")

    # planter les graines
    dragAndDropObject("graines", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Aller a l'autre champ
    time.sleep(1)
    movement(368, 680, 1.1)

    # Ouvrir le deuxième champ
    pushTheAction("gear", 50, 50)

    # reprendre les carottes plantées
    dragAndDropObject("carottes", 50, 50, "right")

    # planter les graines
    dragAndDropObject("graines", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def aller_cuisiniere() :
    # Doit être après avoir utiliser planter_graines
    # Aller a la cuisinière
    movement(210, 750, 1.3)
    
    # Aller a la cuisinière
    movement(206, 663, 1)

def cuisiner_carottes() :
    # Ouvrir la cuisinière
    pushTheAction("gear", 50, 50)

    # Prendre les carottes cuites
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")

    # Mettre les carottes
    dragAndDropObject("carottes", 50, 50, "left")

    # Mettre le charbons
    dragAndDropObject("charbons", 50, 50, "left")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)


def dragAndDropObject_2(dossier, x_plus, y_plus) :
    screenshot = read_screen()

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            x, y = max_loc
            x = x + x_plus
            y = y + y_plus
            pyautogui.moveTo(x/2, y/2)
            pyautogui.doubleClick(button='left') # double clic avec le bouton gauche
            find_image = True
            break


def dragAndDrop(x_mov, y_mov, a_mov, b_mov, duration_mov) :
    pyautogui.click(x_mov/2, y_mov/2, button ='left') 
    pyautogui.dragRel(a_mov, b_mov, duration=duration_mov, button='left')

def movement_2(x_mov, y_mov, duration_mov) :
    directory = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/nav_buttons'

    find_image = False
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Trouver la correspondance la plus élevée
        _, max_val, _, max_loc = testImage(filepath)
        print("max_val = " + str(max_val))
        x, y = max_loc
        x = x + 50
        y = y + 50
        if max_val >= 0.8:
            # Clique au centre du paddle
            print("x = "+ str(x) + " y = "+ str(y) )
            pyautogui.click(x/2, y/2, button ='left') 

            # Bouger
            pyautogui.dragRel(x_mov, y_mov, duration=duration_mov, button='left')
            find_image = True
            break

    if (find_image) :
        print("L'image a été trouvé = nav_buttons")
    else :
        raise Exception("PaddleNotDetectable")

def recycle() :
    # aller a la box avec les objets a recyclé
    movement(334, 720, 1)
    movement(270, 700, 0.75)
    
    time.sleep(1)
    pushTheAction("main", 50, 50)
    time.sleep(1)
    pushTheAction("order_box", 50, 50)
    time.sleep(2)

    # Take first item
    pyautogui.moveTo(750, 225)
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    # Take the second item
    pyautogui.moveTo(870, 225) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pushTheAction("croix", 50, 50)

    time.sleep(1)
    movement(310, 745, 0.30)

    time.sleep(1)
    pushTheAction("gear", 50, 50)

    # Vider les machines 4 emplacement
    pyautogui.moveTo(800, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pyautogui.moveTo(900, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pyautogui.moveTo(1025, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pyautogui.moveTo(1125, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    # Pour mettre les vêtements
    pyautogui.moveTo(185, 230) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pushTheAction("croix", 50, 50)

    # Aller a la deuxième machine
    time.sleep(1)
    movement(320, 675, 0.7)

    time.sleep(1)
    pushTheAction("gear", 50, 50)

    # Vider les machines 4 emplacement
    pyautogui.moveTo(800, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pyautogui.moveTo(900, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pyautogui.moveTo(1025, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pyautogui.moveTo(1125, 525) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    # Pour mettre les vêtements
    pyautogui.moveTo(300, 230) 
    pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

    pushTheAction("croix", 50, 50)

    # Vider les poches
    # Aller dans le coffre en bas des recycleur
    time.sleep(1)
    movement(240, 771, 1.3)
    
    # Ouvre le coffre
    time.sleep(1)
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1100, 750) 
    pyautogui.click(button='left') # clic avec le bouton gauche

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def stopApplication() :

    # Pour stopper l'application
    pyautogui.press('esc')
    pyautogui.moveTo(1900/2, 1050/2) 
    pyautogui.click(button='left') # clic avec le bouton gauche

def stay_in_live() : 
    try :
        while True : 
            live = extract_live()
            if live < 80 :
                for i in range (0,2) :
                    pushTheAction("food_2", 50, 50)
                try :         
                    movement(50, 670, 20)   
                except Exception as e:
                    # afficher l'exception, mais ne rien faire d'autre
                    print(e) 
    
    except Exception as e:
        # afficher l'exception, mais ne rien faire d'autre
        print(e) 

def take_food_from_sac() :
    
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)
    time.sleep(1)

    dragAndDropObject("baies", 50, 50, "left")
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

def test_if_find_image(dossier, x1, y1, x2, y2) :
    # Capture d'écran partielle
    x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
    screenshot = np.array(pyautogui.screenshot(region=(x1, y1, x2, y2)))
    cv2.imwrite('/Users/thononpierre/Documents/Projet/Python/Project/LDOE/test_if_find_image.png', screenshot)

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        # Lecture de l'image modèle
    # Lecture de l'image modèle
    # template = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/template.png")
        template = cv2.imread(filepath)

        # Afficher la taille de l'image
        print("dossier : ", dossier)
        # print("Taille de l'image template : ", template.shape)
        # print("Taille de l'image screenshot : ", screenshot.shape)

        # Conversion en niveaux de gris
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Récupération des dimensions de l'image modèle
        h, w = gray_template.shape

        # Correspondance de modèle
        result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)

        # Récupération de la position de la correspondance maximale
        _, _, min_loc, max_loc = cv2.minMaxLoc(result)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # print (str(max_loc))
        # print (str(min_loc))
        print (str(max_val))

        if max_val >= 0.85:
            find_image = True
            print("Correspondance with the image = " + filepath)
            break

        # # Affichage de la correspondance maximale
        # cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

        # # Affichage de l'image résultat
        # cv2.imshow("Result", screenshot)
        # cv2.waitKey(0)

    return find_image

def test_if_find_image_90(dossier, x1, y1, x2, y2) :
    # Capture d'écran partielle
    x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
    screenshot = np.array(pyautogui.screenshot(region=(x1, y1, x2, y2)))

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        # Lecture de l'image modèle
    # Lecture de l'image modèle
    # template = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/template.png")
        template = cv2.imread(filepath)

        # Afficher la taille de l'image
        print("dossier : ", dossier)
        # print("Taille de l'image template : ", template.shape)
        # print("Taille de l'image screenshot : ", screenshot.shape)

        # Conversion en niveaux de gris
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Récupération des dimensions de l'image modèle
        h, w = gray_template.shape

        # Correspondance de modèle
        result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)

        # Récupération de la position de la correspondance maximale
        _, _, min_loc, max_loc = cv2.minMaxLoc(result)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # print (str(max_loc))
        # print (str(min_loc))
        # print("test_if_find_image_90 = " + str(max_val))

        if max_val >= 0.9:
            find_image = True
            break

        # # Affichage de la correspondance maximale
        # cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

        # # Affichage de l'image résultat
        # cv2.imshow("Result", screenshot)
        # cv2.waitKey(0)

    return find_image

def click_images(dossier, x1, y1, x2, y2) :
    # Capture d'écran partielle
    x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
    screenshot = np.array(pyautogui.screenshot(region=(x1, y1, x2, y2)))

    cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/screenshot.png", screenshot)

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        # Lecture de l'image modèle
    # Lecture de l'image modèle
    # template = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/template.png")
        template = cv2.imread(filepath)

        # Afficher la taille de l'image
        print("dossier : ", dossier)
        # print("Taille de l'image template : ", template.shape)
        # print("Taille de l'image screenshot : ", screenshot.shape)

        # Conversion en niveaux de gris
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Récupération des dimensions de l'image modèle
        h, w = gray_template.shape

        # Correspondance de modèle
        result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)

        # Récupération de la position de la correspondance maximale
        _, _, min_loc, max_loc = cv2.minMaxLoc(result)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        print (str(max_loc))
        print (str(min_loc))
        print (str(max_val))

        # # Affichage de la correspondance maximale
        # cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

        # # Affichage de l'image résultat
        # cv2.imshow("Result", screenshot)
        # cv2.waitKey(0)
        # time.sleep(1)

        if max_val >= 0.8:
            x, y = max_loc
            pyautogui.moveTo((x1/2)+x, (y1/2)+y)
            pyautogui.doubleClick(button='left') # double clic avec le bouton gauche

            find_image = True
            break


    return find_image


def test_if_still_food(dossier) :
    # Capture d'écran partielle
    x1, y1, x2, y2 = 1200*2, 550*2, 1400*2, 640*2
    screenshot = np.array(pyautogui.screenshot(region=(x1, y1, x2, y2)))

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    try :
        find_image = test_if_find_image("plan", 100, 100, 300, 180)
    except Exception as e:
        # afficher l'exception, mais ne rien faire d'autre
        print(e) 
    
    if find_image :
        print("On est a l'extérieur du field => erreur, renvoyer comme quoi on a trouver de la nouriture") 
        # Ferme l'équipement
        pushTheAction("croix", 50, 50)
        find_image = True
    else :

        find_image = False
        for filepath in image_paths:
            # Lecture de l'image modèle
        # Lecture de l'image modèle
        # template = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/template.png")
            template = cv2.imread(filepath)

            # Afficher la taille de l'image
            print("dossier : ", dossier)
            # print("Taille de l'image template : ", template.shape)
            # print("Taille de l'image screenshot : ", screenshot.shape)

            # Conversion en niveaux de gris
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

            # Récupération des dimensions de l'image modèle
            h, w = gray_template.shape

            # Correspondance de modèle
            result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)

            # Récupération de la position de la correspondance maximale
            _, _, min_loc, max_loc = cv2.minMaxLoc(result)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            # print (str(max_loc))
            # print (str(min_loc))
            # print (str(max_val))

            if max_val >= 0.8:
                find_image = True
                break

            # # Affichage de la correspondance maximale
            # cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

            # # Affichage de l'image résultat
            # cv2.imshow("Result", screenshot)
            # cv2.waitKey(0)

    return find_image


def test_if_still_food_2(dossier) :
    now = datetime.datetime.now()
    print("La date et l'heure actuelles sont :", now)
    # Sauvegarde la capture d'écran avant le raise de l'erreur
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    # You need to dubbled the value
    x1, y1, x2, y2 = 1200*2, 550*2, 1400*2, 640*2
    cropped_screenshot = screenshot[y1:y2, x1:x2, :]

    cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/foods.png", cropped_screenshot)

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]
    
    find_image = False
    for filepath in image_paths:
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            find_image = True
            break
    
    return find_image

def test_if_still_places(dossier) :

    # Capture d'écran partielle
    x1, y1, x2, y2 = 136*2, 163*2, 660*2, 495*2
    screenshot = np.array(pyautogui.screenshot(region=(x1, y1, x2, y2)))

    image_dir = '/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/' + dossier
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    find_image = False
    for filepath in image_paths:
        # Lecture de l'image modèle
    # Lecture de l'image modèle
    # template = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/template.png")
        template = cv2.imread(filepath)

        # Afficher la taille de l'image
        print("dossier : ", dossier)
        # print("Taille de l'image template : ", template.shape)
        # print("Taille de l'image screenshot : ", screenshot.shape)

        # Conversion en niveaux de gris
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # Récupération des dimensions de l'image modèle
        h, w = gray_template.shape

        # Correspondance de modèle
        result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)

        # Récupération de la position de la correspondance maximale
        _, _, min_loc, max_loc = cv2.minMaxLoc(result)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # print (str(max_loc))
        # print (str(min_loc))
        # print (str(max_val))

        if max_val >= 0.8:
            find_image = True
            break

        # # Affichage de la correspondance maximale
        # cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

        # # Affichage de l'image résultat
        # cv2.imshow("Result", screenshot)
        # cv2.waitKey(0)

    return find_image

def stay_in_battle() :
    # Procedure pour voir si on a encore de la place dans le sac
    # Voir aussi que on a assé de nouriture pour continuer
    stay = True
    # Ouvre l'équipement
    pushTheAction("sac_map", 50, 50)
    time.sleep(1)
    
    # mettre la nouriture qui reste
    dragAndDropObject("baies", 50, 50, "left")
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")

    if not test_if_still_places("empty") :
        stay = False

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

    return stay

def live_in_the_field() : 
    i = 0
    j = 0
    while True :
        live = extract_live()
        try : 
            if not test_if_still_food("foods") :
                take_food_from_sac()
                j = j + 1
                if j > 5 : 
                    break
            if live <= 60 : 
                for i in range (0,3) :
                    pushTheAction("food_2", 50, 50)
                run_outside_of_the_field()
                break
            elif live <= 70 :
                for i in range (0,3) :
                    pushTheAction("food_2", 50, 50)
                for i in range (0,2) :
                    pushTheAction("food", 50, 50)
            elif live <= 80 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,3) :
                    pushTheAction("food_2", 50, 50)
            elif live <= 90 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,1) :
                    pushTheAction("food_2", 50, 50)
                for i in range (0,2) :
                    pushTheAction("food", 50, 50)
            elif live <= 100 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,1) :
                    pushTheAction("food_2", 50, 50)
            elif live <= 115 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,1) :
                    pushTheAction("food", 50, 50)
        
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

def live_in_the_field_2() : 
    i = 0
    while True :
        live = extract_live()
        try : 
            if not test_if_still_food("foods") :
                take_food_from_sac()
                i = i + 1
                if i > 5 : 
                    break
            elif live <= 50 :
                for i in range (0,4) :
                    pushTheAction("food_2", 50, 50)
                break
            elif live <= 60 : 
                for i in range (0,3) :
                    pushTheAction("food_2", 50, 50)
            elif live <= 70 :
                for i in range (0,2) :
                    pushTheAction("food_2", 50, 50)
                for i in range (0,2) :
                    pushTheAction("food", 50, 50)
            elif live <= 80 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,2) :
                    pushTheAction("food_2", 50, 50)
            elif live <= 90 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,1) :
                    pushTheAction("food_2", 50, 50)
                for i in range (0,1) :
                    pushTheAction("food", 50, 50)
            elif live < 100 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,1) :
                    pushTheAction("food", 50, 50)
        
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

def check_outside_field() :
    while True : 
        # Need to test if we are outside the field
        if test_if_outside_field("carte_globale") :
            print("carte_globale found")
            break