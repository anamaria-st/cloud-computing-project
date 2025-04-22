from twilio.rest import Client
import os
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path

def enviar_alerta_sms(paciente_id, aceleracion):
    sid = os.getenv("TWILIO_SID")
    token = os.getenv("TWILIO_TOKEN")
    print("SID found:", sid)
    client = Client(sid, token)

    mensaje = f"⚠️ Possible fall detected for {paciente_id}. Acceleration: {aceleracion}"

    try:
        message = client.messages.create(
            body=mensaje,
            from_=os.getenv("TWILIO_PHONE"),
            to=os.getenv("NUMERO_DESTINO")
        )
        print(f"📨 Sent message: SID {message.sid}")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")


# Cargar variables del .env
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

def enviar_alerta_correo(paciente_id, aceleracion):
    remitente = os.getenv("EMAIL_USER")
    destinatario = os.getenv("EMAIL_DESTINO")
    contraseña = os.getenv("EMAIL_PASS")

    asunto = "⚠️ Possible Fall Alert"
    cuerpo = f"Patient {paciente_id} might have fallen. Acceleration: {aceleracion} g."

    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(remitente, contraseña)
            servidor.send_message(mensaje)
        print("📧 Email sent successfully")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
