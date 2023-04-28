import cv2
import sys

import numpy as np
import pyautogui
import time



from multiprocessing import freeze_support
import procedure as procedure


debug = False
number_of_time_to_do = 15


if __name__ == '__main__':
    freeze_support()

    if not debug : 
        procedure.startApplication()
        # For testing without restart the application each time
        time.sleep(1)

        procedure.enterCamp()
    else :
        pyautogui.click(800, 400, button ='left') 
        pyautogui.hotkey('command', 'tab')
        time.sleep(1)

    for i in range(number_of_time_to_do):
        time.sleep(1)
        # procedure.boite_inconue()

        procedure.vider_sac()

        procedure.prendre_equipement_used()
        procedure.vider_equipement_poche()

        procedure.movement(206, 706, 0.65) # -- procedure.carpet()
        
        procedure.take_water()

        procedure.boire()

        procedure.toilette()

        procedure.douche()

        procedure.remplir_eau()

        # -- procedure.carpet()
        time.sleep(1)
        procedure.movement(260, 734, 3.8)
        time.sleep(1)
        procedure.movement(253, 702, 1.2)

        procedure.recycle()
        # -- procedure.carpet()
        time.sleep(1)
        procedure.movement(201, 668, 0.7)
        time.sleep(1)
        procedure.movement(285, 678, 0.5)

        procedure.reorganize_items_food()

        # -- procedure.carpet()
        time.sleep(1)
        procedure.movement(249, 678, 1.2)
        time.sleep(1)
        procedure.movement(285, 678, 0.7)

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
        
        procedure.recycle()

        # # -- procedure.carpet()
        procedure.movement(200, 650, 1.0)
        procedure.movement(322, 651, 0.4)

        procedure.go_to_farm()

        # Normally Need to wait 11 minutes pour arriver
        time.sleep(2)
        procedure.stopApplication()
        procedure.wait_until_next_action(11)
        procedure.startApplication()

        procedure.farm_and_back_to_home()


        # # Je dois attendre 11 minutes
        procedure.stopApplication()
        procedure.wait_until_next_action(11)
        procedure.startApplication()

        # Je dois entrer dans la ville
        time.sleep(1)
        procedure.pushTheAction("entrer", 50, 50)
        time.sleep(8)

    if not debug :
        procedure.stopApplication()
        time.sleep(10)
    else :
        pyautogui.click(800, 400, button ='left') 
        pyautogui.hotkey('command', 'tab')
        time.sleep(1)

    # time.sleep(1)
    pyautogui.click(800, 400, button ='left') 
    pyautogui.hotkey('command', 'tab')
    time.sleep(1)


    procedure.farm_and_back_to_home()

    # procedure.farm_and_back_to_home()
    # procedure.carpet()
    # procedure.go_to_farm()

    # Quitter la zone pour aller farmer, après avoir mis dans le recycleur
    # Déplacer le personnage vers la position pour partir
    # procedure.movement(250, 757, 8)

    # time.sleep(5)

    # procedure.go_to_calcaire()

    # procedure.carpet()
    # # procedure.equip_yourself()
    # procedure.metal()
    # procedure.go_to_etabli_metal2()

    # Aller aux autres coffres
    # procedure.movement(315, 650, 0.5)
    # procedure.go_to_coffre_items() 
    # Je dois prendre de la pierre et du bois dans le coffre
    # procedure.carpet()
    # procedure.movement(313, 690, 0.25)
    # procedure.create_suit()   
    # procedure.dress_suit()
    # procedure.vider_sac()
    # procedure.prendre_equipement_used()
    # procedure.vider_equipement_poche()

    # # procedure.boite_inconue()

    # # Je dois vider mon sac
    # procedure.vider_sac()

    # procedure.reorganize_items_food()

    # procedure.carpet()

    # procedure.graines()

    # procedure.carpet()

    # procedure.vider_sac()

    # procedure.carpet()

    # # Remplir les établis
    # procedure.remplir_etablis()

    # procedure.carpet()

    # procedure.vider_sac()

    # procedure.carpet()

    # procedure.recycle()

    # procedure.carpet()


    # # procedure.go_to_farm()
    

    # # procedure.farm_field()
    # # procedure.farm()
    # # procedure.test_if_stay_same_place(550, 330, 800, 670, 0.30)

    # # procedure.test_if_find_image("plus_tard", 660, 590, 810, 645)
    # # procedure.go_to_calcaire()
    

    # procedure.go_to_farm()

    # # Normally Need to wait 11 minutes pour arriver
    # time.sleep(2)
    # procedure.stopApplication()
    # time.sleep(10)
    # procedure.startApplication()

    # # # Je dois attendre 11 minutes
    # procedure.stopApplication()
    # time.sleep(10)
    # procedure.startApplication()
    # time.sleep(10)

    # # Je dois entrer dans la ville
    # time.sleep(1)
    # procedure.pushTheAction("entrer", 50, 50)
    # time.sleep(8)