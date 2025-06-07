from dynamixel_sdk import *
import time
import sys

# --- Configuration Générale ---
DEVICENAME = 'COM3'
BAUDRATE = 1000000
PROTOCOL_VERSION = 1.0

# --- IDs des Servomoteurs ---
RIGHT_HIP = 9
RIGHT_KNEE = 12
RIGHT_ANKLE = 10
LEFT_HIP = 14
LEFT_KNEE = 16
LEFT_ANKLE = 18

DXL_IDS = [RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, LEFT_HIP, LEFT_KNEE, LEFT_ANKLE]

# --- Adresses des Registres Dynamixel ---
ADDR_TORQUE_ENABLE = 24
ADDR_LED = 25
ADDR_GOAL_POSITION = 30 # Inutilisé pour la lecture seule
ADDR_MOVING_SPEED = 32
ADDR_PRESENT_VOLTAGE = 42
ADDR_PRESENT_POSITION = 36

# --- Constantes de Contrôle ---
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
LED_ON = 1
LED_OFF = 0
DEFAULT_MOVING_SPEED = 300

# --- Initialisation du SDK Dynamixel ---
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

def open_connection():
    """Ouvre le port série et règle le baudrate. Quitte en cas d'échec."""
    if not portHandler.openPort():
        print("Échec d’ouverture du port. Arrêt du programme.")
        sys.exit(1)
    print("Port série ouvert.")

    if not portHandler.setBaudRate(BAUDRATE):
        print("Échec du réglage du baudrate. Arrêt du programme.")
        sys.exit(1)
    print("Baudrate réglé.")

def initialize_servos():
    """
    Initialise tous les servomoteurs : active le couple, règle la vitesse et allume la LED.
    Vérifie la tension initiale.
    """
    print("\n--- Initialisation des servomoteurs ---")
    for dxl_id in DXL_IDS:
        print(f"\nInitialisation du servo ID {dxl_id}...")

        # Activation du couple
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print(f"Erreur communication pour le servo ID {dxl_id}: {packetHandler.getTxRxResult(dxl_comm_result)}. Arrêt de l'initialisation.")
            return False
        elif dxl_error != 0:
            print(f"Erreur Dynamixel pour le servo ID {dxl_id}: {packetHandler.getRxPacketError(dxl_error)}. Arrêt de l'initialisation.")
            return False
        print("Couple activé.")

        # Réglage vitesse
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_MOVING_SPEED, DEFAULT_MOVING_SPEED)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur réglage vitesse pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False
        print(f"Vitesse réglée à {DEFAULT_MOVING_SPEED} (~{DEFAULT_MOVING_SPEED * 0.111:.1f} tr/min)")

        # Allumage LED
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_ON)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur allumage LED pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False

        # Lecture tension
        dxl_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_VOLTAGE)
        if dxl_comm_result != COMM_SUCCESS:
            print(f"Erreur lecture tension pour le servo ID {dxl_id}: {packetHandler.getTxRxResult(dxl_comm_result)}. Arrêt de l'initialisation.")
            return False
        elif dxl_error != 0:
            print(f"Erreur Dynamixel (tension) pour le servo ID {dxl_id}: {packetHandler.getRxPacketError(dxl_error)}. Arrêt de l'initialisation.")
            return False
        print(f"Tension initiale : {dxl_voltage / 10:.1f} V")
    return True

def get_present_positions():
    """Lit et retourne les positions actuelles de tous les servomoteurs."""
    present_positions = {}
    print("\nLecture des positions actuelles des servomoteurs...")
    for dxl_id in DXL_IDS:
        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS:
            print(f"Erreur communication lecture position pour le servo ID {dxl_id}: {packetHandler.getTxRxResult(dxl_comm_result)}.")
            return None
        elif dxl_error != 0:
            print(f"Erreur Dynamixel lecture position pour le servo ID {dxl_id}: {packetHandler.getRxPacketError(dxl_error)}.")
            return None
        present_positions[dxl_id] = dxl_present_position
        print(f"  Servo ID {dxl_id}: {dxl_present_position}")
    return present_positions

def shutdown_servos():
    """Désactive le couple et éteint les LEDs de tous les servomoteurs."""
    print("\n--- Extinction des servos et désactivation du couple ---")
    for dxl_id in DXL_IDS:
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_OFF)
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        print(f"    Servo {dxl_id} désactivé.")

# --- Programme Principal ---
if __name__ == "__main__":
    try:
        open_connection()

        if not initialize_servos():
            print("Erreur critique lors de l'initialisation des servos. Arrêt du programme.")
            sys.exit(1)
        
        print("\nPrêt à lire les positions. Le robot ne va pas bouger.")
        input("Appuyez sur Entrée pour lire les positions actuelles...")

        present_positions = get_present_positions()

        if present_positions is None:
            print("Impossible de récupérer toutes les positions. Arrêt.")
            sys.exit(1)

        print("\nPositions lues avec succès.")

    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}. Arrêt du programme.")
        sys.exit(1)
    finally:
        shutdown_servos()
        portHandler.closePort()
        print("Port série fermé.")