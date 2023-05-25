from logging.handlers import RotatingFileHandler
import logging

def LoggingSetup():	
	logging.basicConfig(
	  handlers=[RotatingFileHandler(
	  	"./log.txt", 
	  	maxBytes=104857600, backupCount=1
	  )],
	  level=logging.INFO,
	  format="[%(asctime)s]: %(message)s",
	  datefmt='%d/%m/%Y %H:%M:%S'
	)