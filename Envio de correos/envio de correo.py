#Luis Cipriano Rodriguez Gonzalez
#1753573
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def enviar_correo(destinatario, asunto, cuerpo, ruta_imagen):
    # Configura los detalles del servidor SMTP y tu cuenta de correo
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587  # Puerto típico para STARTTLS
    usuario = ''#Es nuestro correo desde donde enviaremos el mensaje
    contraseña = '' #Contraseña de aplicacion 

    # Configura el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Agrega el cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, 'html'))

    # Agrega la imagen adjunta
    with open(ruta_imagen, 'rb') as archivo_imagen:
        imagen_adjunta = MIMEImage(archivo_imagen.read(), name='imagen_adjunta.png')
        mensaje.attach(imagen_adjunta)

    try:
        # Inicia una conexión segura con el servidor SMTP
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()

        # Inicia sesión en tu cuenta de correo
        servidor.login(usuario, contraseña)

        # Envía el correo
        servidor.sendmail(usuario, destinatario, mensaje.as_string())

        # Cierra la conexión
        servidor.quit()
        print("Correo con imagen adjunta enviado correctamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Uso del script
destinatario = '' #Destinatario del correo
asunto = '' #Asunto del correo
cuerpo='' #Cuerpo del correo en formato html
ruta_imagen = '' #ruta de la imagen que vamos adjuntar

enviar_correo(destinatario, asunto, cuerpo, ruta_imagen)
