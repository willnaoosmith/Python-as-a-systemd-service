from colorist import Color, BrightColor, BgColor, Effect
from functions.mailSender import mailSender
import logging

def getTraceback(traceback, mailFormatted=False):
	trace = ""	
	if traceback:		
		files = ""
		counter = 1
		linebreak = "\n" if not mailFormatted else "<br />"

		for file in traceback['trace']:			
			files += f"{'└──' if counter == len(traceback['trace']) else '├'}{'──' * counter}{file['filename']} line {file['line']}.{linebreak}"
			counter += 1

		trace = f"{Effect.UNDERLINE}{traceback['message']}{Effect.UNDERLINE_OFF}\n{files}" if not mailFormatted else f"<p><b>{traceback['message']}.</b></p>{files}"

	return trace

def success(message):
	logging.info(f"{Color.GREEN}{Effect.BOLD}[SUCCESS]{Effect.BOLD_OFF}{Color.OFF}: {message}")
	

def info(message):
	logging.info(f"{Color.CYAN}{Effect.BOLD}[INFO]{Effect.BOLD_OFF}{Color.OFF}: {message}")
	

def warning(message):
	logging.warning(f"{Color.YELLOW}{Effect.BOLD}[WARNING]{Effect.BOLD_OFF}{Color.OFF}: {message}")
	

def error(message, traceback=None):		
	logging.error(f"{Color.RED}{Effect.BOLD}[ERROR]{Effect.BOLD_OFF}{Color.OFF}: {message} {getTraceback(traceback)}")
	

def critical(message, traceback=None):
	logging.critical(f"{Color.BLACK}{BgColor.WHITE}{Effect.BLINK}{Effect.BOLD}{Effect.BOLD}[CRITICAL]{Effect.BOLD_OFF}{BgColor.OFF}{Effect.BLINK_OFF}{Effect.BOLD_OFF}{Color.OFF}: {message} {getTraceback(traceback)}")
	mailSender(f"""
		<h2>{message}</h2>{getTraceback(traceback, True)}
	""")