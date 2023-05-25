from loaders.config import loadConfig, unloadConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def mailSender(message):
	try:
		config = loadConfig()["mail"]
	
		msg = MIMEMultipart()
		msg['Subject'] = config["message"]["subject"]
		msg['From'] = config["message"]["from"]
		msg['To'] = next((recipient["mail"] for recipient in config["recipients"] if recipient["type"] == "to"), None)		

		if msg['To'] == None:
			raise ValueError("No default recipient set on config file!")

		msg.add_header('Content-Type','text/html')
		msg.attach(MIMEText(message, 'html'))

		mailserver = SMTP(config["smtp"]["server"], config["smtp"]["port"])
		mailserver.connect(config["smtp"]["server"], config["smtp"]["port"])
		mailserver.ehlo()
		mailserver.starttls()
		mailserver.ehlo()
		mailserver.login(config["smtp"]["user"], config["smtp"]["password"])
		
		mailserver.sendmail(msg['From'], [msg['To']], msg.as_string())
		
		mailserver.quit()
		unloadConfig()
	
	except Exception as error:
		#Oh no
		pass
