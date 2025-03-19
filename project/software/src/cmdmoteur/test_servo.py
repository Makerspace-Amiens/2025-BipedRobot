import os
import time
from dynamixel_sdk import *  


DEVICENAME = "COM3"  
BAUDRATE = 1000000  
PROTOCOL_VERSION = 1.0 

ADDR_TORQUE_ENABLE = 24
ADDR_GOAL_POSITION = 30
ADDR_PRESENT_POSITION = 36
ADDR_PRESENT_TEMPERATURE = 43
ADDR_PRESENT_VOLTAGE = 42

TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
DXL_MIN_POSITION = 512 - 200  
DXL_MAX_POSITION = 512 + 200  

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

def test_servomoteurs():
    # Ouvrir le port
    if not portHandler.openPort():
        print("Échec de l'ouverture du port")
        exit()
    if not portHandler.setBaudRate(BAUDRATE):
        print("Échec du paramétrage du baudrate")
        exit()

    print("Port ouvert avec succès !")

    # Scanner les servomoteurs connectés
    print("Recherche des servomoteurs...")
    id_list = []
    for dxl_id in range(1, 254):
        dxl_model_number, dxl_comm_result, dxl_error = packetHandler.ping(portHandler, dxl_id)
        if dxl_comm_result == COMM_SUCCESS:
            id_list.append(dxl_id)
            print(f"Servomoteur détecté : ID {dxl_id}, Modèle {dxl_model_number}")

    if not id_list:
        print("Aucun servomoteur détecté !")
        portHandler.closePort()
        exit()

    # Test des servomoteurs
    for dxl_id in id_list:
        print(f"Activation du couple pour le moteur ID {dxl_id}")
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)

        print("Lecture des données...")
        dxl_position, _, _ = packetHandler.read2ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_POSITION)
        dxl_temperature, _, _ = packetHandler.read1ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_TEMPERATURE)
        dxl_voltage, _, _ = packetHandler.read1ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_VOLTAGE)

        print(f"Moteur {dxl_id} - Position : {dxl_position}, Température : {dxl_temperature}°C, Tension : {dxl_voltage / 10.0}V")
        
        # Test de mouvement
        goal_position = DXL_MAX_POSITION if dxl_position < 512 else DXL_MIN_POSITION
        print(f"Déplacement vers {goal_position}...")
        packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_GOAL_POSITION, goal_position)
        time.sleep(1.5)

        # Vérification
        dxl_position, _, _ = packetHandler.read2ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_POSITION)
        print(f"Nouvelle position du moteur {dxl_id} : {dxl_position}")
        
        # Désactivation du couple
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        print(f"Moteur {dxl_id} désactivé")

    # Fermeture du port
    portHandler.closePort()
    print("Test terminé !")
