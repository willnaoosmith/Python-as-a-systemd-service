from functions import logging
from os import path

def messageHandler(message, type, HandledError=None):
	
	try:
		fullTrackeback = None

		if HandledError != None:			
			trace = []
			traceback = HandledError.__traceback__			

			while traceback is not None and path.realpath(".") in traceback.tb_frame.f_globals["__file__"]:

				trace.append({
					"filename": traceback.tb_frame.f_code.co_filename,
					"line": traceback.tb_lineno
				})

				traceback = traceback.tb_next

			fullTrackeback = {
				'message': HandledError,
				'trace': trace
			}

	except Exception as error:
		pass

	try:
		match type:
			case 'success':
				logging.success(message)

			case 'info':
				logging.info(message)

			case 'warning':
				logging.warning(message)

			case 'error':
				logging.error(message, fullTrackeback)

			case 'critical':
				logging.critical(message, fullTrackeback)
			
			case _:
				error("Erro")

	except Exception as error:
		logging.error("Um erro aconteceu!", error)