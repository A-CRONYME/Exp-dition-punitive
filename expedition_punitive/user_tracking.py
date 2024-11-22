import sherlock
import os

def track_user(username, output_dir="sherlock_results"):
    """
    Utilise Sherlock pour suivre les comptes associés à un username et les gens associés.
    
    Args:
        username : Le pseudo ou l'identité à suivre.
        output_dir : Dossier où enregistrer les résultats.
    Returns:
        dict: Résultats trouvés par Sherlock.
    """
    try:
        # Créer le dossier de résultats si nécessaire
        os.makedirs(output_dir, exist_ok=True)

        # Lancer Sherlock
        results = sherlock.sherlock(username, output_dir=output_dir)

        print(f"Résultats pour {username} enregistrés dans {output_dir}.")
        return results

    except Exception as e:
        print(f"Erreur lors du suivi de {username} : {e}")
        return {}