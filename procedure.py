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

def reorganize_items_food() :
    # Déplacer le personnage a la position ou ce trouve le coffre ou tout les objets pour s'équiper son
    movement(225, 770, 0.5)

    # Ouvre le coffre
    pushTheAction("main", 50, 50)

    # Prendre les carottes, carottes_preparee, baies qui restent.
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")

    dragAndDropObject("baies", 50, 50, "right")
    dragAndDropObject("baies", 50, 50, "right")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

    # Doit aller au frigo
    movement(330, 770, 1.50)

    # Ouvrir le frigo
    pushTheAction("main", 50, 50)

    # Trouver les baies
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")
    dragAndDropObject("baies", 50, 50, "left")
    dragAndDropObject("baies", 50, 50, "left")

    # Fermer le frigo
    pushTheAction("croix", 50, 50)



def graines() :
    take_graines_charbons()

    planter_graines()

    aller_cuisiniere()

    cuisiner_carottes()


def equip_yourself() :
    # Déplacer le personnage a la position ou ce trouve le coffre ou tout les objets pour s'équiper son
    movement(225, 770, 0.5)

    # Ouvre le coffre
    pushTheAction("main", 50, 50)

    # Tout trier 
    pushTheAction("order_box", 50, 50)

    dragAndDropObject("hachette", 50, 50, "right")
    dragAndDropObject("hachette", 50, 50, "right")
    dragAndDropObject("hachette", 50, 50, "right")

    dragAndDropObject("pioche", 50, 50, "right")

    dragAndDropObject("lance", 50, 50, "right")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)

    # Placer l'équipement
    dragAndDropObject("lance", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

    # Doit aller au frigo
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
    dragAndDropObject("baies", 50, 50, "right")

    # mettre de l'équipement
    dragAndDropObject("baies", 50, 50, "left")
    dragAndDropObject("carottes_cuisinee", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

def wait_until_next_action (minutes) :

    subprocess.call('caffeinate &', shell=True)
    for i in range(60 * minutes, 0, -10):
        print("Prochaine exécution dans", i, "secondes")
        time.sleep(10)
        if i < 100 :
            pyautogui.moveTo(200/2, 200/2)

    subprocess.call('killall caffeinate', shell=True)


def go_to_calcaire() :
    # # try to avoid the pub
    # pyautogui.click(1207, 719, button ='left') 

    # Je dois fermer les popups 
    pushTheAction_2("fermer", 50, 50)

    # Je dois fermer les popups 
    pushTheAction_2("plus_tard", 50, 50)

    # pyautogui.click(200, 200, button ='left') 
    # pushTheAction("calcaire", 50, 50)

    # Need to test if you return or not to home
    while True :
        # pushTheAction("home", 10, 10)
        pushTheAction_2("calcaire", 150, 150)

        try : 
            time.sleep(2)
            pushTheAction_2("marcher", 50, 50)
            break
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

def go_to_farm() :

    # je dois équipper mon personnage
    equip_yourself()

    # Quitter la zone pour aller farmer, après avoir mis dans le recycleur
    # Déplacer le personnage vers la position pour partir
    movement(250, 757, 8)

    time.sleep(5)

    go_to_calcaire()

    # Normally Need to wait 11 minutes pour arriver
    time.sleep(2)
    stopApplication()
    wait_until_next_action(11)
    startApplication()
    
    # Cliquer sur ENTRER
    time.sleep(2)
    pushTheAction("entrer", 50, 50)

    time.sleep(7)
    live = extract_live()

    farm_and_back_to_home()

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
            pyautogui.doubleClick(button='left') # double clic avec le bouton gauche
            find_image = True
            break

    time.sleep(1)
    if object == 'hachette' :    
        pyautogui.moveTo(200, 250)
        pyautogui.doubleClick(button='left')
    elif object == 'pioche_craft' :
        pyautogui.moveTo(350, 250)
        pyautogui.doubleClick(button='left')
    
    pushTheAction("creer", 50, 50)

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
            break
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

def farm() :
    print ("Farme the field")
    # Push the button to automate the action 
    pushTheAction("auto", 50, 50)

    p1 = multiprocessing.Process(target=live_in_the_field)
    p2 = multiprocessing.Process(target=stay_in_live)
    p1.start()
    while True :
        live = extract_live()
        print ("p1 is alive = "+ str(p1.is_alive()))
        print ("p2 is alive = "+ str(p2.is_alive()))
        try : 
            if live < 69 :
                break
            

            if need_tools("need_tools", 50, 50) == "Inventory_full" :
                break

            if inventory_full("inventory_full", 0, 0) :
                break

            if inventory_full("no_more_items", 0, 0) :
                break
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

        # De temps en temps on sort de la zone il faut pouvoir y rentrer à nouveau
        pushTheAction("entrer", 50, 50)
            
    p1.terminate()
    
    p2.start()
    # Je n'ai plus de nouriture je dois fuir
    run_outside_of_the_field()
    p2.terminate()

def run_outside_of_the_field() :
    try : 
        
        movement(50, 670, 15)   

    except Exception as e:
        # afficher l'exception, mais ne rien faire d'autre
        print(e) 


def farm_and_back_to_home() :
    farm()

    back_to_home()

    # # Je dois attendre 11 minutes
    stopApplication()
    wait_until_next_action(11)
    startApplication()

    # Je dois entrer dans la ville
    time.sleep(1)
    pushTheAction("entrer", 50, 50)

def remplir_etablis() :

    print("Remplir les établis de bois et de pierre")

    # Prendre dans le coffre le minerais de fer
    # Ouvrir le coffre
    pushTheAction("gear", 50, 50)

    dragAndDropObject("minerai_fer", 50, 50, "right")
    dragAndDropObject("charbons", 50, 50, "right")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    movement(313, 680, 1)

    # Ouvrir la cabane
    pushTheAction("gear", 50, 50)

    # Prendre 2 stack de bois
    dragAndDropObject("bois", 50, 50, "right")
    dragAndDropObject("bois", 50, 50, "right")

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
    remplir_etabli_avec("blocs", "pierre", 50, 50)

    # Aller a l'établi de pierre
    time.sleep(1)
    movement(310, 686, 0.50)
    # 
    remplir_etabli_avec("blocs", "pierre", 50, 50)

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

    # # Prendre le charbon qui a été fait.
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

    dragAndDropObject("minerai_fer_sac", 50, 50, "left")
    dragAndDropObject("charbons_sac", 50, 50, "left")

    dragAndDropObject("barre_fer", 50, 50, "right")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # # Aller au fourneau de haut a gauche
    # time.sleep(1)
    # movement(240, 748, 0.90)

    # # Ouvrir le coffre
    # time.sleep(1)
    # pushTheAction("gear", 50, 50)

    # dragAndDropObject("charbons_sac", 50, 50, "left")
    # dragAndDropObject("minerai_fer_sac", 50, 50, "left")

    # dragAndDropObject("barre_fer", 50, 50, "right")

    # # Ferme le coffre
    # pushTheAction("croix", 50, 50)

    carpet()

    vider_sac()

    carpet()

    herbes()

    carpet()

    time.sleep(1)
    vider_sac()

def herbes() :
    # prendre de l'herbe
    # coffre de rangement
    movement(225, 770, 0.2)

    # Ouvrir le coffre
    pushTheAction("gear", 50, 50)

    dragAndDropObject("herbes", 50, 50, "right")
    dragAndDropObject("tissus", 50, 50, "right")

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

    dragAndDropObject("tissus_epais", 50, 50, "right")
    dragAndDropObject("tissus_sac", 50, 50, "left")

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


def vider_sac() :
    # Je dois vider mon sac
    # vider le bois les pierres dans la cabane
    movement(313, 690, 0.25)

    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 770) 
    pyautogui.click(button='left') # double clic avec le bouton gauche

    # range le coffre
    pushTheAction("order_box", 50, 50)

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

    # vider le reste dans le coffre
    time.sleep(1)
    movement(225, 770, 0.5)

    # aller dans mon sac et mettre ce que j'ai ramassé dans ma poche
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)

    # vider ce que j'ai dans les poches
    dragAndDropObject("lance", 50, 50, "right")
    dragAndDropObject("baies", 50, 50, "right")
    dragAndDropObject("carottes_cuisinee", 50, 50, "right")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)

    time.sleep(1)
    pushTheAction("main", 50, 50)

    # Place tout les objets dans le coffre
    pyautogui.moveTo(1110, 750) 
    pyautogui.click(button='left') # double clic avec le bouton gauche

    # range le coffre
    pushTheAction("order_box", 50, 50)
    # Ferme le coffre
    pushTheAction("croix", 50, 50)


def extract_live() :
    now = datetime.datetime.now()
    print("La date et l'heure actuelles sont :", now)
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
        nombre = "60"

    now = datetime.datetime.now()
    print("La date et l'heure actuelles sont :", now)
    return nombre





def startApplication() :


    subprocess.Popen(["open", "-a", "Last Day On Earth: Survival.app"])

    # Doit attendre que l'application se lance
    time.sleep(15)

    loading_screen = cv2.imread("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/loading_screen.png", cv2.IMREAD_GRAYSCALE)
    # Attendre jusqu'au moment ou l'application est chargée
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
        pyautogui.click(1400/2, 1160/2, button ='left') 
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
    elif dossier == "creer" :
        x, y = 2100 - 50, 1450 - 50

    x = x + x_plus
    y = y + y_plus
    pyautogui.click(x/2, y/2, button ='left') 

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
    
    x, y = 800, 170
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

    time.sleep(2)

    try :
        pushTheAction_2("redemarrer", 50, 50)
    except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

    time.sleep(4)

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

    if not find_image:
        # Sauvegarde la capture d'écran avant le raise de l'erreur
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)

        x1, y1 = 422 - 50, 1314 - 50
        x2, y2 = 10, 10
        if dossier == "gear"  :
            x1, y1 = 2220 - 50, 1550 - 50
            x2, y2 = x1 + 350, y1 + 350
        elif dossier == "main"  :
            x1, y1 = 2220 - 50, 1550 - 50
            x2, y2 = x1 + 350, y1 + 350
        elif dossier == "calcaire" :
            x1, y1 = 160 - 50, 1280 - 50
            x2, y2 = x1 + 350, y1 + 350
        elif dossier == "home" :
            x1, y1 = 2180 - 50, 300 - 50
            x2, y2 = x1 + 350, y1 + 350
        elif dossier == "marcher" :
            x1, y1 = 930 - 0, 560 - 0
            x2, y2 = 1070, 610
        elif dossier == "fermer" :
            x1, y1 = 930 - 0, 560 - 0
            x2, y2 = 1070, 610
        elif dossier == "plus_tard" :
            x1, y1 = 675 - 0, 600 - 0
            x2, y2 = 800, 640
        elif dossier == "croix_pub" : 
            x1, y1 = 1291 - 0, 20 - 0
            x2, y2 = 1350, 66
        elif dossier == "prendre" : 
            x1, y1 = 933 - 0, 536 - 0
            x2, y2 = 1058, 569
        elif dossier == "boite_inconnue" : 
            x1, y1 = 876*2 - 0, 831*2 - 0
            x2, y2 = 923*2, 869*2

        cropped_screenshot = screenshot[y1:y2, x1:x2, :]

        if dossier == "fermer" :
            print("Pas de popup à fermer, continuer")
        elif dossier == "plus_tard" :
            print("Pas de popup à mettre plus tard, continuer")
        else :
            print("Image not found : " + dossier)
            i = 1
            while os.path.exists("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/" + dossier + "/" + dossier + "_" + str(i) + ".png"):
                i += 1
            cv2.imwrite("/Users/thononpierre/Documents/Projet/Python/Project/LDOE/images/" + dossier + "/" + dossier + "_" + str(i) + ".png", cropped_screenshot)

            raise ImageNotFound(dossier)
        
        

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

def take_graines_charbons() :
    # Aller dans le coffre
    movement(220, 750, 0.4)

    # Ouvre le coffre
    time.sleep(1)
    pushTheAction("main", 50, 50)

    # Prendre les graines
    dragAndDropObject("graines", 50, 50, "right")
    dragAndDropObject("graines", 50, 50, "right")

    # Prendre le nécessaire pour cuire
    dragAndDropObject("charbons", 50, 50, "right")
    dragAndDropObject("carottes", 50, 50, "right")

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def carpet() :
    time.sleep(1)
    push_home_button(2600, 500, 0, 0)
    time.sleep(8)
    push_home_button(2600, 500, 0, 0)
    time.sleep(8)

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
    movement(310, 745, 0.50)

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
    pyautogui.moveTo(185, 230) 
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
    pyautogui.click(button='left') # double clic avec le bouton gauche

    # Ferme le coffre
    pushTheAction("croix", 50, 50)

def stopApplication() :

    # Pour stopper l'application
    pyautogui.press('esc')
    pyautogui.moveTo(1900/2, 1050/2) 
    pyautogui.click(button='left') # double clic avec le bouton gauche

def stay_in_live() : 
    try :
        while True : 
            live = extract_live()
            if live < 80 :
                for i in range (0,2) :
                    pushTheAction("food_2", 50, 50)
            try :         
                movement(50, 670, 15)   
            except Exception as e:
                # afficher l'exception, mais ne rien faire d'autre
                print(e) 
    
    except Exception as e:
        # afficher l'exception, mais ne rien faire d'autre
        print(e) 

def take_food_from_sac() :
    
    # Ouvre l'équipement
    pushTheAction("sac", 50, 50)

    dragAndDropObject("baies", 50, 50, "left")

    # Ferme l'équipement
    pushTheAction("croix", 50, 50)


def test_if_still_food(dossier) :
    # Capture d'écran partielle
    x1, y1, x2, y2 = 1200*2, 550*2, 1400*2, 640*2
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
        print("Taille de l'image template : ", template.shape)
        print("Taille de l'image screenshot : ", screenshot.shape)

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



def live_in_the_field() : 
    while True :
        live = extract_live()
        
        try : 
            if not test_if_still_food("foods") :
                take_food_from_sac()
            elif live < 70 :
                for i in range (0,3) :
                    pushTheAction("food", 50, 50)
                    time.sleep(1)
                live = extract_live()
                if live < 70 :
                    break
            elif live <= 80 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,2) :
                    pushTheAction("food", 50, 50)
                    time.sleep(1)
            elif live < 100 :
                print("Je vais devoir prendre de la nouriture")
                for i in range (0,1) :
                    pushTheAction("food", 50, 50)
                    time.sleep(1)
        
        except Exception as e:
            # afficher l'exception, mais ne rien faire d'autre
            print(e) 

def check_outside_field() :
    while True : 
        # Need to test if we are outside the field
        if test_if_outside_field("carte_globale") :
            print("carte_globale found")
            break