import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time


# Función para crear el informe
def crear_informe():
    # Este es un ejemplo simple de crear un informe
    informe = "Este es tu informe diario.\nTodo está funcionando bien."
    with open("informe_diario.txt", "w") as file:
        file.write(informe)


# Función para enviar el correo
def enviar_correo():
    # Crear el informe
    crear_informe()

    # Configuración del correo
    fromaddr = "tu_correo@gmail.com"
    toaddr = "destinatario@ejemplo.com"

    # Crear el objeto MIMEMultipart
    msg = MIMEMultipart()

    # Configuración del mensaje
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Informe Diario"

    # Cuerpo del correo
    body = "Adjunto encontrarás el informe diario."

    # Adjuntar el cuerpo al mensaje
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo
    filename = "informe_diario.txt"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    # Configuración del servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "tu_contraseña")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


# Configurar el cronograma
schedule.every().day.at("09:00").do(enviar_correo)

# Mantener el script en ejecución
while True:
    schedule.run_pending()
    time.sleep(1)