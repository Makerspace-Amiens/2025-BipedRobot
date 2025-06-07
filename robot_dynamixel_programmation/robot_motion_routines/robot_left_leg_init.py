from dynamixel_sdk import *
import time

# --- Configuration Générale ---
DEVICENAME = 'COM3'  
BAUDRATE = 1000000   
PROTOCOL_VERSION = 1.0

# --- IDs des Servomoteurs de la Jambe Gauche ---
LEFT_ANKLE = 14
LEFT_KNEE = 16
LEFT_FOOT = 18

DXL_IDS = [LEFT_ANKLE, LEFT_KNEE, LEFT_FOOT] 

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
MOVING_SPEED = 300 # Vitesse de déplacement

# --- Initialisation du SDK Dynamixel ---
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

def open_connection():
    """Ouvre le port série et configure le baudrate."""
    print("Tentative d'ouverture du port série...")
    if not portHandler.openPort():
        print("Échec d’ouverture du port. Vérifiez le nom du port et les permissions.")
        return False
    print("Port série ouvert avec succès.")

    print("Tentative de réglage du baudrate...")
    if not portHandler.setBaudRate(BAUDRATE):
        print("Échec du réglage du baudrate. Vérifiez la valeur et la connexion.")
        return False
    print(f"Baudrate réglé à {BAUDRATE}.")
    return True

def initialize_servos():
    """Initialise le couple, la vitesse et la LED pour chaque servomoteur (jambe gauche)."""
    print("\n--- Initialisation des servomoteurs de la Jambe Gauche ---")
    for dxl_id in DXL_IDS:
        print(f"\nConfiguration du servo ID {dxl_id}...")

        # Activer le couple
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS or dxl_error != 0:
            print(f"Erreur d'activation du couple pour le servo {dxl_id}. Résultat: {packetHandler.getTxRxResult(dxl_comm_result)}, Erreur DXL: {packetHandler.getRxPacketError(dxl_error)}.")
            return False
        print("Couple activé.")

        # Régler la vitesse
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
    print("\nTous les servomoteurs de la jambe gauche sont initialisés.")
    return True

def execute_sync_movements(movements):
    """Exécute une série de mouvements synchronisés pour les servos de la jambe gauche."""
    for i, goal_positions in enumerate(movements):
        print(f"\nDéplacement {i+1} vers positions : {goal_positions}")
        groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_GOAL_POSITION, 2)

        # Assurez-vous que le nombre de positions correspond au nombre d'IDs de servos
        if len(goal_positions) != len(DXL_IDS):
            print(f"Erreur: Le nombre de positions ({len(goal_positions)}) ne correspond pas au nombre de servos ({len(DXL_IDS)}).")
            groupSyncWrite.clearParam()
            continue

        for dxl_id, pos in zip(DXL_IDS, goal_positions):
            param_goal_position = [DXL_LOBYTE(pos), DXL_HIBYTE(pos)]
            groupSyncWrite.addParam(dxl_id, param_goal_position)

        dxl_comm_result = groupSyncWrite.txPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print(f"Erreur envoi groupé : {packetHandler.getTxRxResult(dxl_comm_result)}")

        groupSyncWrite.clearParam()
        time.sleep(2)

def shutdown_servos():
    """Désactive le couple et éteint les LEDs de tous les servomoteurs (jambe gauche)."""
    print("\n--- Extinction des servos de la Jambe Gauche et désactivation du couple ---")
    for dxl_id in DXL_IDS:
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_OFF)
        time.sleep(0.05) 
        packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        print(f"Servo {dxl_id} désactivé.")
        time.sleep(0.05)
    print("Tous les servomoteurs de la jambe gauche sont éteints.")
    
# --- Programme principal ---
if __name__ == "__main__":
    try:
        if not open_connection():
            sys.exit(1)

        if not initialize_servos():
            print("Erreur critique lors de l'initialisation. Arrêt du programme.")
            sys.exit(1)

        # Séquence de mouvements pour la jambe gauche
        all_positions_left_leg = [
            [200, 300, 400],  
            [700, 600, 500],  
            [512, 512, 512], 
        ]
        execute_sync_movements(all_positions_left_leg)

        print("\nProgramme principal terminé avec succès.")

    except Exception as e:
        print(f"\nUne erreur inattendue est survenue: {e}. Arrêt du programme.")
        sys.exit(1)
    finally:
        shutdown_servos()
        portHandler.closePort()
        print("Port série fermé.")