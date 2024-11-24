import time
import random
from expedition_punitive.email_sender import send_email

def schedule_email_randomized(to_email, subject, body, attachment_path=None, min_delay=10, max_delay=60):
    """
    Planifie l'envoi d'un email à un moment aléatoire dans une plage de temps donnée.

    Args:
        to_email (str): L'adresse email du destinataire.
        subject (str): Le sujet de l'email.
        body (str): Le corps du message.
        attachment_path (str): Chemin du fichier à joindre (facultatif).
        min_delay (int): Délai minimum en secondes avant l'envoi.
        max_delay (int): Délai maximum en secondes avant l'envoi.
    """
    try:
        # Générer un délai aléatoire entre min_delay et max_delay
        delay = random.randint(min_delay, max_delay)
        print(f"L'envoi de l'email est programmé dans {delay} secondes.")

        # Attendre le délai aléatoire
        time.sleep(delay)

        # Envoyer l'email
        send_email(to_email, subject, body, attachment_path)

    except Exception as e:
        print(f"Erreur lors de la planification de l'email : {e}")

    except KeyboardInterrupt:
        print("Envoi annulé par l'utilisateur.")
