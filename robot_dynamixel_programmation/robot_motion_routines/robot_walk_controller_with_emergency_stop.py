from dynamixel_sdk import *
import time
import sys
import keyboard

# Configuration de base
DEVICENAME = 'COM3'
BAUDRATE = 1000000
PROTOCOL_VERSION = 1.0

# Mapping des moteurs (ID)
RIGHT_HIP = 9
RIGHT_ANKLE = 12
RIGHT_KNEE = 10

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

emergency_stop_triggered = False

def emergency_stop_callback(event):
    global emergency_stop_triggered
    if event.name == 'space':
        emergency_stop_triggered = True
        print("\n!!! TOUCHE ESPACE DÉTECTÉE - ARRÊT D'URGENCE !!!")

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
    Initialise tous les servomoteurs.
    """
    for dxl_id in DXL_IDS:
        print(f"\nInitialisation du servo ID {dxl_id}...")

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print(f"Erreur communication pour le servo ID {dxl_id}: {packetHandler.getTxRxResult(dxl_comm_result)}. Arrêt de l'initialisation.")
            return False
        elif dxl_error != 0:
            print(f"Erreur Dynamixel pour le servo ID {dxl_id}: {packetHandler.getRxPacketError(dxl_error)}. Arrêt de l'initialisation.")
            return False
        else:
            print("Couple activé.")

        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_MOVING_SPEED, DEFAULT_MOVING_SPEED)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur réglage vitesse pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False
        else:
            print(f"Vitesse réglée à {DEFAULT_MOVING_SPEED} (~{DEFAULT_MOVING_SPEED * 0.111:.1f} tr/min)")

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_ON)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur allumage LED pour le servo ID {dxl_id}. Arrêt de l'initialisation.")
            return False

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

def move_servos(positions_dict):
    global emergency_stop_triggered
    if emergency_stop_triggered:
        return False

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
    global emergency_stop_triggered
    if emergency_stop_triggered:
        return False
    
    if not move_servos(target_positions):
        return False
    
    start_time = time.time()
    while time.time() - start_time < duration:
        if emergency_stop_triggered:
            return False
        time.sleep(0.01)
    return True

def set_initial_positions():
    global emergency_stop_triggered
    print("\nRéglage des positions initiales des servomoteurs...")
    if not move_to_position(INITIAL_POSITIONS, duration=2.0):
        if emergency_stop_triggered:
            print("Arrêt d'urgence lors du réglage des positions initiales.")
        return False
    print("Positions initiales réglées avec succès.")
    
    start_time = time.time()
    while time.time() - start_time < 1.5:
        if emergency_stop_triggered:
            print("Arrêt d'urgence pendant la pause initiale.")
            return False
        time.sleep(0.01)
    return True

def perform_walk_steps(num_steps=4):
    global emergency_stop_triggered
    print("\nDébut de la routine de marche...")

    time.sleep(5)

    DUR_STEP_PHASE = 1.2
    DUR_PLANT = 0.6
    DUR_PAUSE_BETWEEN_STEPS = 0.4

    KNEE_LIFT_OFFSET = 80
    HIP_SWING_OFFSET = 60
    HIP_LATERAL_SHIFT_OFFSET = 25

    current_positions = INITIAL_POSITIONS.copy()

    for step_count in range(num_steps):
        if emergency_stop_triggered:
            print("Arrêt d'urgence avant le début du pas.")
            return False

        print(f"\n--- Pas {step_count + 1} ---")

        print("Phase 1 (Droit): Levée et balancement jambe droite...")
        target_pos_right_lift_swing = {
            RIGHT_HIP: 351,
            LEFT_HIP: 722,
            RIGHT_KNEE: 639,
            RIGHT_ANKLE: 384,
            LEFT_KNEE: 573,
            LEFT_ANKLE: 453
        }
        if not move_to_position(target_pos_right_lift_swing, DUR_STEP_PHASE): return False
        current_positions = target_pos_right_lift_swing.copy()

        print("Phase 2 (Droit): Pose pied droit et transfert de poids à droite...")
        target_pos_right_plant = {
            RIGHT_HIP: 377,
            LEFT_HIP: 713,
            RIGHT_KNEE: 617,
            RIGHT_ANKLE: 345,
            LEFT_KNEE: 394,
            LEFT_ANKLE: 486
        }
        if not move_to_position(target_pos_right_plant, DUR_PLANT): return False
        current_positions = target_pos_right_plant.copy()
        
        start_time = time.time()
        while time.time() - start_time < DUR_PAUSE_BETWEEN_STEPS:
            if emergency_stop_triggered:
                print("Arrêt d'urgence pendant la pause entre les phases.")
                return False
            time.sleep(0.01)

    print("\nRetour à la position initiale...")
    if not move_to_position(INITIAL_POSITIONS, 1.5):
        if emergency_stop_triggered:
            print("Arrêt d'urgence lors du retour à la position initiale.")
        return False
    
    print("\nRoutine de marche terminée.")
    return True


def shutdown_servos():
    """
    Désactive le couple et éteint les LEDs de tous les servomoteurs.
    """
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

if __name__ == "__main__":
    keyboard.on_press(emergency_stop_callback)

    try:
        open_connection()

        if not initialize_servos():
            print("Erreur critique lors de l'initialisation des servos. Arrêt du programme.")
            sys.exit(1)

        if not set_initial_positions():
            if emergency_stop_triggered:
                print("Le programme s'est arrêté en raison de l'arrêt d'urgence.")
            sys.exit(1)

        if not perform_walk_steps(num_steps=2):
            if emergency_stop_triggered:
                print("Le programme s'est arrêté en raison de l'arrêt d'urgence.")
            sys.exit(1)

        print("\nProgramme terminé avec succès. Les mouvements de marche ont été effectués.")

    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}. Arrêt du programme.")
        sys.exit(1)
    finally:
        keyboard.unhook_all()
        shutdown_servos()
        portHandler.closePort()