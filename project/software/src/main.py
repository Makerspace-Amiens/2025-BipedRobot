
from cmdmoteur.test_servo import test_servomoteurs

if __name__ == "__main__":
    print("Début de l'exécution du programme principal.")

    try:
        # Appel de la fonction test_servomoteurs
        print("Appel de la fonction test_servomoteurs()...")
        test_servomoteurs()
        print("Test des servomoteurs terminé avec succès.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'exécution du test : {e}")
    
    print("Fin de l'exécution du programme principal.")
