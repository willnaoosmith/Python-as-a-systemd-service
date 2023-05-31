from loaders.config import config, unloadConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def mailSender(message):
	try:			
		msg = MIMEMultipart()
		msg['Subject'] = config["mail"]["message"]["subject"]
		msg['From'] = config["mail"]["message"]["from"]
		msg['To'] = next((recipient["mail"] for recipient in config["mail"]["recipients"] if recipient["type"] == "to"), None)		

		if msg['To'] == None:
			raise ValueError("No default recipient set on config file!")

		msg.add_header('Content-Type','text/html')
		msg.attach(MIMEText(message, 'html'))

		mailserver = SMTP(config["mail"]["smtp"]["server"], config["mail"]["smtp"]["port"])
		mailserver.connect(config["mail"]["smtp"]["server"], config["mail"]["smtp"]["port"])
		mailserver.ehlo()
		mailserver.starttls()
		mailserver.ehlo()
		mailserver.login(config["mail"]["smtp"]["user"], config["mail"]["smtp"]["password"])
		
		mailserver.sendmail(msg['From'], [msg['To']], msg.as_string())
		
		mailserver.quit()
	
	except Exception as error:
		#Oh no
		pass
