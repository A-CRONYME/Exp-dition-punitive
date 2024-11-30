import time
import random
from expedition_punitive.email_sender import send_email

def schedule_emails_randomized(emails, subject, body, attachment_path=None, min_delay=10, max_delay=60):
    """
    Planifie l'envoi d'emails à plusieurs destinataires à des moments aléatoires dans une plage donnée.

    Args:
        emails (list): Liste des adresses email récupérées.
        subject (str): Le sujet de l'email.
        body (str): Le corps du message.
        attachment_path (str): Chemin du fichier à joindre (facultatif).
        min_delay (int): Délai minimum en secondes avant l'envoi de chaque email.
        max_delay (int): Délai maximum en secondes avant l'envoi de chaque email.
    """
    try:
        for email in emails:
            # Générer un délai aléatoire entre min_delay et max_delay
            delay = random.randint(min_delay, max_delay)
            print(f"L'email pour {email} sera envoyé dans {delay} secondes.")
            
            # Attendre le délai aléatoire
            time.sleep(delay)

            # Envoyer l'email
            send_email(email, subject, body, attachment_path)
            print(f"Email envoyé à {email}.")

    except Exception as e:
        print(f"Erreur lors de la planification ou de l'envoi : {e}")

    except KeyboardInterrupt:
        print("Processus d'envoi annulé par l'utilisateur.")
