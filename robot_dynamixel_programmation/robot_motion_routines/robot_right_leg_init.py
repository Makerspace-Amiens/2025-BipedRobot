from dynamixel_sdk import *
import time
import sys

# --- Configuration Générale ---
DEVICENAME = 'COM3' 
BAUDRATE = 1000000   
PROTOCOL_VERSION = 1.0 

# --- IDs des Servomoteurs de la Jambe Droite ---
RIGHT_HIP = 9
RIGHT_KNEE = 12
RIGHT_ANKLE = 10

DXL_IDS = [RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE] # Liste des IDs des servos à contrôler

# --- Adresses des registres Dynamixel ---
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
MOVING_SPEED = 150

# --- Initialisation du SDK Dynamixel ---
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

def open_connection():
    """Ouvre le port série et configure le baudrate."""
    print("Tentative d'ouverture du port série...")
    if not portHandler.openPort():
        print("Échec d’ouverture du port. Vérifie le nom du port et les permissions.")
        return False
    print("Port série ouvert avec succès.")

    print("Tentative de réglage du baudrate...")
    if not portHandler.setBaudRate(BAUDRATE):
        print("Échec du réglage du baudrate. Vérifie la valeur et la connexion.")
        return False
    print(f"Baudrate réglé à {BAUDRATE}.")
    return True

def initialize_servos():
    """Initialise le couple, la vitesse et la LED pour chaque servomoteur (jambe droite)."""
    print("\n--- Initialisation des servomoteurs de la Jambe Droite ---")
    for dxl_id in DXL_IDS:
        print(f"\nInitialisation du servo ID {dxl_id}...")

        # Activation du couple
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur d'activation du couple pour le servo {dxl_id}. Résultat: {packetHandler.getTxRxResult(dxl_comm_result)}, Erreur DXL: {packetHandler.getRxPacketError(dxl_error)}.")
            return False
        print("Couple activé.")

        # Réglage vitesse
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_MOVING_SPEED, MOVING_SPEED)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur de réglage vitesse pour le servo {dxl_id}. Résultat: {packetHandler.getTxRxResult(dxl_comm_result)}, Erreur DXL: {packetHandler.getRxPacketError(dxl_error)}.")
            return False
        print(f"Vitesse réglée à {MOVING_SPEED} ({MOVING_SPEED * 0.111:.1f} tr/min).")

        # Allumage LED
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_ON)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur d'allumage LED pour le servo {dxl_id}. Résultat: {packetHandler.getTxRxResult(dxl_comm_result)}, Erreur DXL: {packetHandler.getRxPacketError(dxl_error)}.")
            return False
        print("LED allumée.")

        # Lecture tension
        dxl_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_VOLTAGE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur de lecture tension pour le servo {dxl_id}. Résultat: {packetHandler.getTxRxResult(dxl_comm_result)}, Erreur DXL: {packetHandler.getRxPacketError(dxl_error)}.")
            return False
        print(f"Tension : {dxl_voltage / 10:.1f} V")
    print("\nTous les servomoteurs de la jambe droite sont initialisés.")
    return True

def move_servos(positions_dict):
    """Déplace les servomoteurs vers les positions spécifiées."""
    groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_GOAL_POSITION, 2)

    for dxl_id, pos in positions_dict.items():
        param_goal_position = [DXL_LOBYTE(pos), DXL_HIBYTE(pos)]
        if not groupSyncWrite.addParam(dxl_id, param_goal_position):
            print(f"Échec d'ajout du paramètre pour le servo ID {dxl_id}.")
            groupSyncWrite.clearParam()
            return False

    dxl_comm_result = groupSyncWrite.txPacket()
    if dxl_comm_result != COMM_SUCCESS:
        print(f"Erreur lors de l'envoi du paquet groupé : {packetHandler.getTxRxResult(dxl_comm_result)}.")
        groupSyncWrite.clearParam()
        return False
    print("Commande de mouvement groupé envoyée avec succès.")

    groupSyncWrite.clearParam()
    return True

def shutdown_servos():
    """Désactive le couple et éteint les LEDs de tous les servomoteurs (jambe droite)."""
    print("\n--- Extinction des servos de la Jambe Droite et désactivation du couple ---")
    for dxl_id in DXL_IDS:
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_OFF)
        time.sleep(0.05) # Petit délai pour la stabilité
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        print(f"Servo {dxl_id} désactivé.")
        time.sleep(0.05) # Petit délai pour la stabilité
    print("Tous les servomoteurs de la jambe droite sont éteints.")
    
# --- Programme principal ---
if __name__ == "__main__":
    try:
        if not open_connection():
            sys.exit(1)

        if not initialize_servos():
            print("Erreur critique lors de l'initialisation. Arrêt du programme.")
            sys.exit(1)

        # Exemple de mouvement vers une position cible pour la jambe droite
        print("\nDéplacement de la jambe droite vers les positions cibles...")
        goal_positions_right_leg = {
            RIGHT_HIP: 335,
            RIGHT_KNEE: 589,
            RIGHT_ANKLE: 436
        }

        if not move_servos(goal_positions_right_leg):
            print("Échec du mouvement vers les positions cibles pour la jambe droite.")
            sys.exit(1)
        
        print("Toutes les positions cibles ont été envoyées. Attente du mouvement...")
        time.sleep(2)
        print("Mouvement vers les positions cibles terminé avec succès pour la jambe droite.")

        print("\nProgramme principal terminé avec succès.")

    except Exception as e:
        print(f"\nUne erreur inattendue est survenue: {e}. Arrêt du programme.")
        sys.exit(1)
    finally:
        shutdown_servos()
        portHandler.closePort()
        print("Port série fermé.")