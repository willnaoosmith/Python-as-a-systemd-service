import json

configFile = open("configFiles/config.json")

def loadConfig():
	return json.load(configFile)

def unloadConfig():
	configFile.close()