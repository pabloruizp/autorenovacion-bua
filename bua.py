##Script auto renovar los prestamos

import smtplib
from email.mime.text import MIMEText
from selenium import webdriver ##Para instalar la libreria:  pip3 install -U selenium
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
chrome_options=options

id = "TU ID"
nip = "TU NIP"
url = "http://gaudi.ua.es/uhtbin/cgisirsi/0/0/0/29/124/X/3"
fecha_i = [] 

##Descargar el webdriver segun vuestra version de Chrome: https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(r"LA RUTA DE TU WEBDRIVER",options=chrome_options)
driver.get(url)

##Escribe vuestro user y password
driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input").send_keys(id)
driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input").send_keys(nip)

##Inicia sesion
driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr/td/form/table/tbody/tr[3]/td/input[1]").click()


iteraciones = int(driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr/td/form/table/tbody/tr[2]/td/strong").text)

for i in range(iteraciones):
    fecha_i.append(driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr/td/form/table/tbody/tr["+str(i+4)+"]/td[3]/strong").text)

##Marca renovar todos los libros
driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr/td/form/table/tbody/tr[3]/td/input[2]").click()
driver.find_element_by_class_name("searchbutton").click()

email_body = "Los siguientes libros no se han podido renovar correctamente: \n\n" 
send = False

for i in range(iteraciones):
    try:
        driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr/td/table/tbody/tr[2]/td/dl["+str(i+1)+"]/dd/strong").text

    except:
        email_body = email_body + "\n\n" + driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr/td/table/tbody/tr[2]/td/dl["+str(i+1)+"]/dd").text + "\n" + fecha_i[i]
        send = True


driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr/td/table/tbody/tr[3]/td/a").click()

##Cierra el navegador
driver.close()

if send:
    # Establecemos conexion con el servidor smtp de gmail
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login("TU GMAIL","TU PASSWORD")

    # Construimos el mensaje simple
    mensaje = MIMEText(str(email_body))
    mensaje['From']="TU EMAIL"
    mensaje['To']="TU EMAIL"
    mensaje['Subject']="ESTOS LIBROS NO SE HAN PODIDO RENOVAR CORRECTAMENTE"

    # Envio del mensaje
    mailServer.sendmail("TU EMAIL","TU EMAIL",mensaje.as_string())