import cv2
import sys

import numpy as np
import pyautogui
import time



from multiprocessing import freeze_support
import procedure as procedure


debug = True
number_of_time_to_do = 0
 

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

        procedure.movement(216, 688, 0.7)

        procedure.recycle()
        # -- procedure.carpet()
        time.sleep(1)
        procedure.movement(201, 668, 0.7)
        time.sleep(1)
        procedure.movement(285, 678, 0.6)
        
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

        # need to wait 5 mins
        # procedure.wait_until_next_action(5)
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

    time.sleep(1)
    pyautogui.click(800, 400, button ='left') 
    pyautogui.hotkey('command', 'tab')
    time.sleep(1)

    
    # procedure.go_to_farm()

    # # Normally Need to wait 11 minutes pour arriver
    # time.sleep(2)
    # procedure.stopApplication()
    # procedure.wait_until_next_action(11)
    # procedure.startApplication()

    # procedure.farm_and_back_to_home()

    procedure.farm_field()

    # procedure.create_equipment()
    # procedure.create_and_dress_suit()
    # procedure.take_materiaux()

    # procedure.dress_suit()
