from twilio.rest import Client
import os

def enviar_alerta_sms(paciente_id, aceleracion):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))

    mensaje = f"⚠️ Possible fall detected for {paciente_id}. Acceleration: {aceleracion}"

    try:
        message = client.messages.create(
            body=mensaje,
            from_=os.getenv("TWILIO_PHONE"),
            to=os.getenv("NUMERO_DESTINO")  # Tu número verificado con Twilio
        )
        print(f"📨 Sent message: SID {message.sid}")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")
