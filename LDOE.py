import cv2
import sys

import numpy as np
import pyautogui
import time



from multiprocessing import freeze_support
import procedure as procedure


debug = True

if __name__ == '__main__':
    freeze_support()

    if not debug : 
        procedure.startApplication()

    for i in range(0):

        # For testing without restart the application each time
        time.sleep(1)

        procedure.enterCamp()

        # Je dois vider mon sac
        time.sleep(8)

        procedure.vider_sac()

        procedure.carpet()

        procedure.boite_inconue()

        procedure.graines()

        procedure.carpet()

        procedure.vider_sac()

        procedure.reorganize_items_food()

        procedure.carpet()

        procedure.go_to_farm()

        time.sleep(8)

        # Je dois vider mon sac
        procedure.vider_sac()

        # Remplir les établis
        procedure.remplir_etablis()

        procedure.carpet()

        procedure.vider_sac()

        procedure.carpet()

        procedure.recycle()

        procedure.carpet()

        # procedure.boite_inconue()

    if not debug :
        procedure.stopApplication()
        time.sleep(10)

    time.sleep(1)
    # # Remonter l'allée jusqu'au établis de bois

    # procedure.go_to_farm()
    # procedure.boite_inconue()

    procedure.reorganize_items_food()


    # # procedure.carpet()

    # # Je dois entrer dans la ville
    # # procedure.pushTheAction("entrer", 50, 50)

    # # Je dois vider mon sac
    # procedure.vider_sac()

    # # Remplir les établis
    # procedure.remplir_etablis()

    # procedure.carpet()

    # procedure.graines()

    # procedure.carpet()

    # procedure.vider_sac()

    # procedure.boite_inconue()

    # procedure.carpet()

    # procedure.recycle()

    # procedure.farm_and_back_to_home()

    # procedure.farm()c

    # procedure.back_to_home()

    # procedure.run_outside_of_the_field()

    # procedure.extract_live()

    # procedure.back_to_home()