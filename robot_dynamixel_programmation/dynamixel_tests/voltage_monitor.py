from dynamixel_sdk import *
import time
import sys

# --- Configuration Générale ---
DEVICENAME = 'COM3'
BAUDRATE = 1000000
PROTOCOL_VERSION = 1.0

# --- IDs des Servomoteurs des Jambes ---
RIGHT_HIP = 9
RIGHT_KNEE = 12
RIGHT_ANKLE = 10

LEFT_HIP = 14
LEFT_KNEE = 16
LEFT_ANKLE = 18

DXL_IDS = [RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, LEFT_HIP, LEFT_KNEE, LEFT_ANKLE]

# --- Positions Initiales ---
INITIAL_POSITIONS = {
    RIGHT_HIP: 330,
    RIGHT_KNEE: 500,
    RIGHT_ANKLE: 550,
    LEFT_HIP: 690,
    LEFT_KNEE: 600,
    LEFT_ANKLE: 450
}

# --- Adresses des Registres Dynamixel ---
ADDR_TORQUE_ENABLE = 24
ADDR_LED = 25
ADDR_GOAL_POSITION = 30
ADDR_MOVING_SPEED = 32
ADDR_PRESENT_VOLTAGE = 42

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
    """Ouvre le port série et configure le baudrate. Quitte en cas d'échec."""
    if not portHandler.openPort():
        print("Échec d’ouverture du port. Arrêt du programme.")
        sys.exit(1)
    print("Port série ouvert.")

    if not portHandler.setBaudRate(BAUDRATE):
        print("Échec du réglage du baudrate. Arrêt du programme.")
        sys.exit(1)
    print("Baudrate réglé.")

def initialize_servos():
    """Initialise tous les servomoteurs: active le couple, règle la vitesse et allume la LED.
    Vérifie la tension initiale."""
    print("\n--- Initialisation des servomoteurs ---")
    for dxl_id in DXL_IDS:
        print(f"\nInitialisation du servo ID {dxl_id}...")

        # Activation du couple
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur d'activation du couple pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False
        print("Couple activé.")

        # Réglage vitesse
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_MOVING_SPEED, DEFAULT_MOVING_SPEED)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur de réglage vitesse pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False
        print(f"Vitesse réglée à {DEFAULT_MOVING_SPEED} (~{DEFAULT_MOVING_SPEED * 0.111:.1f} tr/min)")

        # Allumage LED
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_ON)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur d'allumage LED pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False

        # Lecture tension
        dxl_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_VOLTAGE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur lecture tension pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False
        print(f"Tension initiale : {dxl_voltage / 10:.1f} V")
    return True

def move_servos(positions_dict):
    """Envoie des commandes de position à plusieurs servomoteurs simultanément."""
    groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_GOAL_POSITION, 2)
    for dxl_id, pos in positions_dict.items():
        param_goal_position = [DXL_LOBYTE(pos), DXL_HIBYTE(pos)]
        if not groupSyncWrite.addParam(dxl_id, param_goal_position):
            print(f"Échec d'ajout du paramètre pour le servo ID {dxl_id}.")
            groupSyncWrite.clearParam()
            return False
    
    dxl_comm_result = groupSyncWrite.txPacket()
    if dxl_comm_result != COMM_SUCCESS:
        print(f"Erreur envoi groupé : {packetHandler.getTxRxResult(dxl_comm_result)}.")
        groupSyncWrite.clearParam()
        return False
    
    groupSyncWrite.clearParam()
    return True

def move_to_position(target_positions, duration=1.0):
    """Déplace les servomoteurs vers les positions cibles, en gérant la durée du mouvement."""
    if not move_servos(target_positions):
        return False
    time.sleep(duration)
    return True

def set_initial_positions():
    """Définit les positions initiales pour tous les servomoteurs et lit la tension après."""
    print("\nRéglage des positions initiales des servomoteurs...")
    if not move_to_position(INITIAL_POSITIONS, duration=1.5):
        print("Échec du réglage des positions initiales.")
        return False
    print("Positions initiales réglées avec succès.")
    read_all_servo_voltages()
    return True

def read_all_servo_voltages():
    """Lit et affiche la tension actuelle de tous les servomoteurs Dynamixel."""
    print("\n--- Tension actuelle des Servomoteurs ---")
    all_ok = True
    for dxl_id in DXL_IDS:
        dxl_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_VOLTAGE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"  Erreur lecture tension pour servo ID {dxl_id}: {packetHandler.getTxRxResult(dxl_comm_result) if dxl_comm_result != COMM_SUCCESS else packetHandler.getRxPacketError(dxl_error)}.")
            all_ok = False
        else:
            voltage_val = dxl_voltage / 10.0
            print(f"  Servo ID {dxl_id}: {voltage_val:.1f} V {'(Basse!)' if voltage_val < 9.0 else ''}")
    print("---------------------------------------")
    return all_ok

def shutdown_servos():
    """Désactive le couple de tous les servomoteurs et éteint leurs LEDs."""
    print("\nExtinction des servos et désactivation du couple...")
    for dxl_id in DXL_IDS:
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_OFF)
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Avertissement: Échec de désactivation du couple pour le servo {dxl_id}.")
        else:
            print(f"    Servo {dxl_id} désactivé.")

# --- Programme Principal ---
if __name__ == "__main__":
    try:
        open_connection()

        if not initialize_servos():
            print("Erreur critique lors de l'initialisation des servos. Arrêt du programme.")
            sys.exit(1)

        if not set_initial_positions():
            print("Erreur critique lors du réglage des positions initiales. Arrêt du programme.")
            sys.exit(1)

        print("\nProgramme terminé avec succès.")

    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}. Arrêt du programme.")
        sys.exit(1)
    finally:
        shutdown_servos()
        portHandler.closePort()