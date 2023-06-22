import cv2
import sys

import numpy as np
import pyautogui
import time



from multiprocessing import freeze_support
import procedure as procedure

import multiprocessing

debug = True
number_of_time_to_do = 0
number_of_time_to_do_farm = 0
test = 0
 
def all_steps(queue, event, i) :
    time.sleep(2)
    procedure.hide_objectif()
    # procedure.boite_inconue()

    procedure.pushTheAction("food_2", 50, 50)
    procedure.pushTheAction("food_2", 50, 50)

    time.sleep(1)
    procedure.vider_sac()

    procedure.movement(340, 656, 0.3)

    procedure.recycle()

    procedure.movement(216, 688, 0.7)
    procedure.movement(304, 631, 0.4)

    procedure.vider_sac()

    procedure.prendre_detruire("pierre")
    time.sleep(1)
    procedure.prendre_detruire("blocs")
    time.sleep(1)
    procedure.prendre_detruire("bois")
    time.sleep(1)
    procedure.prendre_detruire("planches")
    time.sleep(1)

    procedure.prendre_equipement_used()
    procedure.vider_equipement_poche()
    procedure.after_vider_equipement_poche()

    # -- procedure.carpet()
    time.sleep(1)
    procedure.movement(195, 689, 0.7)
    # time.sleep(1)
    # procedure.movement(285, 678, 0.6)
    
    procedure.take_water()

    procedure.boire(2)

    procedure.toilette()

    procedure.douche()

    procedure.remplir_eau()

    # -- procedure.carpet()
    time.sleep(1)
    procedure.movement(260, 734, 3.8)
    time.sleep(1)
    procedure.movement(253, 702, 1.2)

    procedure.reorganize_items_food()

    # -- procedure.carpet()
    time.sleep(1)
    procedure.movement(249, 678, 1.2)
    time.sleep(1)
    procedure.movement(285, 678, 0.7)

    # vider ce que j'ai dans mes poches comme nouriture
    procedure.vider_nouriture_poche()
    procedure.vider_sac()

    time.sleep(0)
    procedure.reorganize_items_items()

    # -- procedure.carpet()
    time.sleep(0)
    procedure.movement(344, 695, 2.7)
    procedure.movement(354, 675, 1.1)

    procedure.graines()

    procedure.movement(325, 675, 0.5)

    procedure.place_food_fridge()

    # -- procedure.carpet(')
    procedure.movement(245, 637, 1.7)

    procedure.metal()

    # -- procedure.carpet()
    procedure.movement(219, 754, 1.0)
    procedure.movement(344, 748, 1.4)
    procedure.movement(325, 650, 0.5)

    procedure.vider_sac()

    # Remplir les établis
    procedure.remplir_etablis()

    procedure.movement(340, 640, 1.0)

    # -- procedure.carpet()
    procedure.movement(279, 789, 2.1)
    procedure.movement(353, 751, 2.0)
    procedure.movement(322, 651, 0.3)

    procedure.vider_sac()

    procedure.herbes()

    # -- procedure.carpet()
    procedure.movement(350, 714, 0.7)
    procedure.movement(340, 760, 3.0)
    procedure.movement(336, 661, 1.0)
    procedure.movement(336, 698, 0.63)
    
    procedure.vider_sac()
    procedure.movement(340, 653, 0.3)

    procedure.take_items_from_base_to_colony()
    procedure.remplir_etabli_colonie()

    procedure.vider_sac()

    # Prendre les ressources qui sont dans le coffre de brol
    time.sleep(1)
    procedure.movement(349, 751, 1)
    procedure.take_items_to_treat()
    time.sleep(1)
    procedure.movement(303, 634, 0.5)
    time.sleep(1)
    procedure.deposer_vetements()
    time.sleep(1)
    procedure.movement(200, 650, 0.8)
    time.sleep(1)
    procedure.vider_sac()

    time.sleep(1)
    procedure.movement(339, 657, 0.3)
    # need to wait 1 minutes
    procedure.wait_until_next_action(i, 1, "Attendre le recycleur")
    procedure.recycle()

    time.sleep(1)
    procedure.carpet()
    # procedure.movement(331, 652, 0.3)

    time.sleep(1)
    procedure.go_to_farm()

    # Normally Need to wait 11 minutes pour arriver
    time.sleep(2)
    procedure.stopApplication()
    procedure.wait_until_next_action(i, 11, "go_to_farm")
    procedure.startApplication()

    procedure.farm_and_back_to_home()

    # # Je dois attendre 11 minutes
    procedure.stopApplication()
    procedure.wait_until_next_action(i, 11, "back_to_home")
    procedure.startApplication()

    # Je dois entrer dans la ville
    time.sleep(1)
    procedure.pushTheAction("entrer", 50, 50)
    time.sleep(8)

    event.set()
def farm_only(queue, event, j) :

    time.sleep(1)
    procedure.hide_objectif()
    procedure.hide_objectif()

    procedure.vider_sac()

    procedure.movement(340, 656, 0.3)

    procedure.recycle()

    procedure.movement(216, 688, 0.7)
    procedure.movement(304, 631, 0.4)

    procedure.prendre_detruire("pierre")
    procedure.prendre_detruire("blocs")
    # procedure.prendre_pierre()
    # procedure.detruire_pierre()
    # procedure.prendre_blocs()
    # procedure.detruire_blocs()

    procedure.prendre_equipement_used()
    procedure.vider_equipement_poche()
    procedure.after_vider_equipement_poche()

    procedure.carpet()
    # time.sleep(1)
    # procedure.movement(195, 689, 0.7)
    # time.sleep(1)
    # procedure.movement(285, 678, 0.6)

    procedure.go_to_farm()

    # Normally Need to wait 11 minutes pour arriver
    time.sleep(2)
    procedure.stopApplication()
    procedure.wait_until_next_action(j, 11, "go_to_farm")
    procedure.startApplication()

    procedure.farm_and_back_to_home()

    # # Je dois attendre 11 minutes
    procedure.stopApplication()
    procedure.wait_until_next_action(j, 11, "back_to_home")
    procedure.startApplication()

    # Je dois entrer dans la ville
    time.sleep(1)
    procedure.pushTheAction("entrer", 50, 50)
    time.sleep(8)

    event.set()


if __name__ == '__main__':
    freeze_support()

    if not debug : 
        procedure.startApplication()
        # For testing without restart the application each time
        time.sleep(2)

        procedure.enterCamp()
    else :
        pyautogui.click(800, 400, button ='left') 
        pyautogui.hotkey('command', 'tab')
        time.sleep(2)

    for x in range(test):
        event1 = multiprocessing.Event()
        event2 = multiprocessing.Event()
        p1 = multiprocessing.Process(target=procedure.dead_or_not, args=(None, event1))
        p2 = multiprocessing.Process(target=procedure.test1, args=(None, event2))
        p1.start()
        p2.start()

        while True:
            if event1.is_set():
                p2.terminate()  # Arrêter le processus p2 si le processus p1 s'est terminé
                break
            if event2.is_set():
                p1.terminate()  # Arrêter le processus p1 si le processus p2 s'est terminé
                break

        p1.join()
        p2.join()

        event1.clear()
        event2.clear()
        print("End of the " + str(x) + " iteration")
      


    for j in range(number_of_time_to_do_farm):
        event1 = multiprocessing.Event()
        event2 = multiprocessing.Event()
        p1 = multiprocessing.Process(target=procedure.dead_or_not, args=(None, event1))
        p2 = multiprocessing.Process(target=farm_only, args=(None, event2, j))
        p1.start()
        p2.start()

        while True:
            if event1.is_set():
                p2.terminate()  # Arrêter le processus p2 si le processus p1 s'est terminé
                break
            if event2.is_set():
                p1.terminate()  # Arrêter le processus p1 si le processus p2 s'est terminé
                break

        p1.join()
        p2.join()

        event1.clear()
        event2.clear()
        print("End of the " + str(j) + " iteration")
        

    for i in range(number_of_time_to_do):
        event1 = multiprocessing.Event()
        event2 = multiprocessing.Event()
        p1 = multiprocessing.Process(target=procedure.dead_or_not, args=(None, event1))
        p2 = multiprocessing.Process(target=all_steps, args=(None, event2, i))
        p1.start()
        p2.start()

        while True:
            if event1.is_set():
                p2.terminate()  # Arrêter le processus p2 si le processus p1 s'est terminé
                break
            if event2.is_set():
                p1.terminate()  # Arrêter le processus p1 si le processus p2 s'est terminé
                break

        p1.join()
        p2.join()

        event1.clear()
        event2.clear()
        print("End of the " + str(i) + " iteration")

    if not debug :
        procedure.stopApplication()
        time.sleep(10)
    else :
        pyautogui.click(800, 400, button ='left') 
        pyautogui.hotkey('command', 'tab')
        time.sleep(1)

# Testing phase
    if debug :
        time.sleep(1)
        pyautogui.click(800, 400, button ='left') 
        pyautogui.hotkey('command', 'tab')
        time.sleep(1)

        # procedure.movement(200, 740, 1)
        # procedure.movement(200, 800, 7)

        # procedure.go_to_farm()
        procedure.go_to_calcaire()
        # procedure.farm_and_back_to_home()

        # procedure.kill()