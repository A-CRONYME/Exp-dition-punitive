from expedition_punitive.scheduler import schedule_email_randomized

def main():
    print("Bienvenue dans l'application Expédition Punitive.")
    
    # Configurer les informations de l'email et le fichier joint
    to_email = "destinataire@example.com"
    subject = "Message posthume"
    body = "Ceci est un message posthume. Prenez soin de vous."
    attachment_path = "chemin/vers/votre_fichier.pdf"

    # Spécifier la plage de délais en secondes (simple test en secondes, a modifier pour des semaines, mois, etc.)
    min_delay = 30
    max_delay = 120

    # Planifier l'envoi aléatoire de l'email avec le fichier joint
    schedule_email_randomized(to_email, subject, body, attachment_path, min_delay, max_delay)

if __name__ == "__main__":
    main()
