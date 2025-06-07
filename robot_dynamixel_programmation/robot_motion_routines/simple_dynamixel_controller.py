from dynamixel_sdk import *
import time

# --- Configuration du servomoteur ---
DEVICENAME = 'COM3'  
BAUDRATE = 1000000   
PROTOCOL_VERSION = 1.0 

DXL_ID = 18          # ID du Servomoteurs à Tester

# --- Adresses des registres Dynamixel ---
ADDR_TORQUE_ENABLE = 24
ADDR_LED = 25
ADDR_GOAL_POSITION = 30
ADDR_MOVING_SPEED = 32
ADDR_PRESENT_VOLTAGE = 42

# --- Constantes de contrôle ---
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
LED_ON = 1
LED_OFF = 0
MOVING_SPEED = 300 

# --- Initialisation du SDK Dynamixel ---
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

# --- Fonctions utilitaires ---

def open_dynamixel_port():
    """Ouvre le port série et règle le baudrate."""
    if not portHandler.openPort():
        print("Échec d’ouverture du port.")
        quit()
    print("Port série ouvert.")

    if not portHandler.setBaudRate(BAUDRATE):
        print("Échec du réglage du baudrate.")
        quit()
    print("Baudrate réglé.")

def initialize_servo(dxl_id):
    """Active le couple, règle la vitesse et allume la LED du servomoteur."""
    print(f"Initialisation du servomoteur ID {dxl_id}...")

    # Activer le couple
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print(f"Erreur de communication (couple): {packetHandler.getTxRxResult(dxl_comm_result)}")
    elif dxl_error != 0:
        print(f"Erreur Dynamixel (couple): {packetHandler.getRxPacketError(dxl_error)}")
    else:
        print("Couple activé.")

    # Régler la vitesse
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_MOVING_SPEED, MOVING_SPEED)
    if dxl_comm_result != COMM_SUCCESS:
        print(f"Erreur réglage vitesse: {packetHandler.getTxRxResult(dxl_comm_result)}")
    elif dxl_error != 0:
        print(f"Erreur Dynamixel (vitesse): {packetHandler.getRxPacketError(dxl_error)}")
    else:
        print(f"Vitesse configurée à {MOVING_SPEED} (environ {MOVING_SPEED * 0.111:.1f} tr/min)")

    # Allumer la LED et lire la tension
    packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_ON)
    dxl_voltage, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, dxl_id, ADDR_PRESENT_VOLTAGE)
    if dxl_comm_result != COMM_SUCCESS:
        print(f"Erreur lecture tension: {packetHandler.getTxRxResult(dxl_comm_result)}")
    elif dxl_error != 0:
        print(f"Erreur Dynamixel (tension): {packetHandler.getRxPacketError(dxl_error)}")
    else:
        print(f"Tension lue : {dxl_voltage / 10:.1f} V")

def move_servo_to_position(dxl_id, position, delay=2):
    """Déplace le servomoteur vers une position cible et attend."""
    print(f"Déplacement vers position {position}...")
    packetHandler.write2ByteTxRx(portHandler, dxl_id, ADDR_GOAL_POSITION, position)
    time.sleep(delay)

def shutdown_servo(dxl_id):
    """Désactive le couple et éteint la LED du servomoteur."""
    packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_LED, LED_OFF)
    packetHandler.write1ByteTxRx(portHandler, dxl_id, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
    print("Couple désactivé.")

def close_dynamixel_port():
    """Ferme le port série."""
    portHandler.closePort()
    print("Port série fermé.")

# --- Programme principal ---
if __name__ == "__main__":
    open_dynamixel_port()
    initialize_servo(DXL_ID)

    # Déplacement du servomoteur vers la position 200 (remise à zéro)
    move_servo_to_position(DXL_ID, 200)

    shutdown_servo(DXL_ID)
    close_dynamixel_port()