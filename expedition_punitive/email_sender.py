import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(to_email, subject, body, attachment_path=None):
    """Envoie un email avec ou sans pièce jointe."""
    from config import SMTP_SERVER, SMTP_PORT, EMAIL, PASSWORD

    try:
        # Création du message
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject

        # Ajouter le corps du message
        msg.attach(MIMEText(body, 'plain'))

        # Ajouter une pièce jointe (si fournie)
        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(attachment_path)}")
                msg.attach(part)

        # Envoyer l'email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
            print(f"Email envoyé à {to_email}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
