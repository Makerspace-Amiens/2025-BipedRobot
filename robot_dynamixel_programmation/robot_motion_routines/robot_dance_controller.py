from dynamixel_sdk import *
import time
import sys

# Configuration de base
DEVICENAME = 'COM3'
BAUDRATE = 1000000
PROTOCOL_VERSION = 1.0

# Mapping des moteurs (ID)
RIGHT_HIP = 9
RIGHT_KNEE = 12
RIGHT_ANKLE = 10

LEFT_HIP = 14
LEFT_KNEE = 16
LEFT_ANKLE = 18

DXL_IDS = [RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, LEFT_HIP, LEFT_KNEE, LEFT_ANKLE]

# Positions Initiales
INIT_POSITIONAL_RIGHT_HIP = 347
INIT_POSITIONAL_RIGHT_KNEE = 500
INIT_POSITIONAL_RIGHT_ANKLE = 550

INIT_POSITIONAL_LEFT_HIP = 682
INIT_POSITIONAL_LEFT_KNEE = 601
INIT_POSITIONAL_LEFT_ANKLE = 450

INITIAL_POSITIONS = {
    RIGHT_HIP: INIT_POSITIONAL_RIGHT_HIP,
    RIGHT_KNEE: INIT_POSITIONAL_RIGHT_KNEE,
    RIGHT_ANKLE: INIT_POSITIONAL_RIGHT_ANKLE,
    LEFT_HIP: INIT_POSITIONAL_LEFT_HIP,
    LEFT_KNEE: INIT_POSITIONAL_LEFT_KNEE,
    LEFT_ANKLE: INIT_POSITIONAL_LEFT_ANKLE
}

# Adresses des registres Dynamixel
ADDR_TORQUE_ENABLE = 24
ADDR_LED = 25
ADDR_GOAL_POSITION = 30
ADDR_MOVING_SPEED = 32
ADDR_PRESENT_VOLTAGE = 42

# Constantes de contrôle
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
LED_ON = 1
LED_OFF = 0
DEFAULT_MOVING_SPEED = 300

# Initialisation du SDK Dynamixel
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Vérification de la communication
def open_connection():
    if not portHandler.openPort():
        print("Échec d’ouverture du port. Arrêt du programme.")
        sys.exit(1)
    else:
        print("Port série ouvert.")

    if not portHandler.setBaudRate(BAUDRATE):
        print("Échec du réglage du baudrate. Arrêt du programme.")
        sys.exit(1)
    else:
        print("Baudrate réglé.")

def initialize_servos():
    """
    Initialise tous les servomoteurs listés dans DXL_IDS.
    Active le couple, règle la vitesse par défaut et allume la LED.
    Vérifie la tension initiale.
    """
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
        else:
            print("Couple activé.")

        # Réglage vitesse
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_MOVING_SPEED, DEFAULT_MOVING_SPEED)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur réglage vitesse pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False
        else:
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
        else:
            print(f"Tension initiale : {dxl_voltage / 10:.1f} V")
    return True

# Envoie des commandes de position à plusieurs servomoteurs
def move_servos(positions_dict):
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

# Déplace les servomoteurs vers les positions cibles
def move_to_position(target_positions, duration=1.0):
  
    if not move_servos(target_positions):
        return False
    time.sleep(duration)
    return True

# Réglages Initialisation Servomoteurs
def set_initial_positions():
    print("\nRéglage des positions initiales des servomoteurs...")
    if not move_to_position(INITIAL_POSITIONS, duration=1.5):
        print("Échec du réglage des positions initiales.")
        return False
    print("Positions initiales réglées avec succès.")
    return True

# Routine de Danse
def perform_dance_steps(num_sequences=2): # num_sequences = nbr de fois que la séquence doit être exécutée
    print("\nDébut de la routine de danse dynamique et expressive améliorée pour la stabilité...")

    # Décalages pour les mouvements de danses
    KNEE_BEND_DEEP = 100
    KNEE_BEND_LIGHT = 40
    HIP_SWING_LATERAL = 60
    HIP_PITCH_FORWARD = 15
    ANKLE_ROLL_LEAN = 15
    ANKLE_PITCH_TOE_UP = 15

    # Durées des étapes de danse
    DUR_VERY_FAST = 0.2
    DUR_FAST = 0.3
    DUR_MEDIUM = 0.5
    DUR_SLOW = 0.7
    DUR_PAUSE_SHORT = 0.09
    DUR_PAUSE_MEDIUM = 0.3

    current_positions = INITIAL_POSITIONS.copy()

    for sequence_count in range(num_sequences):
        print(f"\n--- Séquence de danse {sequence_count + 1} (Plus Stable) ---")

        # Étape 1: Le "Robot Pop"
        print("1. Mouvement 'Robot Pop' (droit)")
        target_pos = current_positions.copy()
        target_pos[RIGHT_HIP] = INITIAL_POSITIONS[RIGHT_HIP] + HIP_SWING_LATERAL
        if not move_to_position(target_pos, DUR_FAST): return False
        time.sleep(DUR_PAUSE_SHORT) 

        print("2. Mouvement 'Robot Pop' (gauche)")
        target_pos = INITIAL_POSITIONS.copy()
        target_pos[LEFT_HIP] = INITIAL_POSITIONS[LEFT_HIP] - HIP_SWING_LATERAL
        if not move_to_position(target_pos, DUR_FAST): return False
        time.sleep(DUR_PAUSE_SHORT)

        if not move_to_position(INITIAL_POSITIONS, DUR_MEDIUM): return False
        current_positions = INITIAL_POSITIONS.copy()
        time.sleep(DUR_PAUSE_SHORT)

        # Étape 3: "Mini-shuffle" 
        print("3. Mini-shuffle droit")
        target_pos = INITIAL_POSITIONS.copy()
        target_pos[RIGHT_HIP] = INITIAL_POSITIONS[RIGHT_HIP] + int(HIP_SWING_LATERAL * 0.6)
        target_pos[LEFT_KNEE] = INITIAL_POSITIONS[LEFT_KNEE] - int(KNEE_BEND_LIGHT * 1.0)
        if not move_to_position(target_pos, DUR_FAST): return False
        if not move_to_position(INITIAL_POSITIONS, DUR_FAST): return False

        print("4. Mini-shuffle gauche")
        target_pos = INITIAL_POSITIONS.copy()
        target_pos[LEFT_HIP] = INITIAL_POSITIONS[LEFT_HIP] - int(HIP_SWING_LATERAL * 0.6)
        target_pos[RIGHT_KNEE] = INITIAL_POSITIONS[RIGHT_KNEE] - int(KNEE_BEND_LIGHT * 1.0)
        if not move_to_position(target_pos, DUR_FAST): return False
        if not move_to_position(INITIAL_POSITIONS, DUR_FAST): return False
        
        # Répétition pour plus de dynamisme avec les mouvements agrandis
        print("5. Mini-shuffle droit")
        target_pos = INITIAL_POSITIONS.copy()
        target_pos[RIGHT_HIP] = INITIAL_POSITIONS[RIGHT_HIP] + int(HIP_SWING_LATERAL * 0.6)
        target_pos[LEFT_KNEE] = INITIAL_POSITIONS[LEFT_KNEE] - int(KNEE_BEND_LIGHT * 1.0)
        if not move_to_position(target_pos, DUR_FAST): return False
        if not move_to_position(INITIAL_POSITIONS, DUR_FAST): return False

        print("6. Mini-shuffle gauche")
        target_pos = INITIAL_POSITIONS.copy()
        target_pos[LEFT_HIP] = INITIAL_POSITIONS[LEFT_HIP] - int(HIP_SWING_LATERAL * 0.6)
        target_pos[RIGHT_KNEE] = INITIAL_POSITIONS[RIGHT_KNEE] - int(KNEE_BEND_LIGHT * 1.0)
        if not move_to_position(target_pos, DUR_FAST): return False
        if not move_to_position(INITIAL_POSITIONS, DUR_FAST): return False
        
        current_positions = INITIAL_POSITIONS.copy()
        time.sleep(DUR_PAUSE_MEDIUM)

    print("\nRoutine de danse terminée")
    return True

# Désactive le couple et éteint les LEDs de tous les servomoteurs.
def shutdown_servos(): 
    print("\nExtinction des servos et désactivation du couple...")
    for dxl_id in DXL_IDS:
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_OFF)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Avertissement: Échec d'extinction de la LED pour le servo {dxl_id}.")

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Avertissement: Échec de désactivation du couple pour le servo {dxl_id}.")
        else:
            print(f"    Servo {dxl_id} désactivé.")

# Programme principal
if __name__ == "__main__":
    try:
        open_connection()

        if not initialize_servos():
            print("Erreur critique lors de l'initialisation des servos. Arrêt du programme.")
            sys.exit(1)

        if not set_initial_positions():
            print("Erreur critique lors du réglage des positions initiales. Arrêt du programme.")
            sys.exit(1)

        if not perform_dance_steps(num_sequences=2):
            print("Erreur critique lors de l'exécution de la danse. Arrêt du programme.")
            sys.exit(1)

        print("\nProgramme terminé avec succès. Les mouvements de danse ont été effectués.")

    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}. Arrêt du programme.")
        sys.exit(1)
    finally:
        shutdown_servos()
        portHandler.closePort()