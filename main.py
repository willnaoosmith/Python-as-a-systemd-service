# !/usr/bin/python
# -*- coding: utf-8 -*-

from handlers.messageHandler import messageHandler
from setup.LoggingSetup import LoggingSetup
from signal import signal, SIGTERM

try:

	def safeExit(*args):
		raise ValueError('safeExit')

	LoggingSetup()

	messageHandler("Starting service.", "info")
	
	signal(SIGTERM, safeExit)
			
	"""
		Your code code here
	"""

	messageHandler("Service started successfully!", "success")

except Exception as error:
	if str(error) == 'safeExit':
		pass
	
	else:
		messageHandler("An error ocurred!", "critical", error)

finally:
	messageHandler("Stopping service.", "info")

	"""
		Your exit code here
	"""

	messageHandler("Stopped service successfully!", "success")