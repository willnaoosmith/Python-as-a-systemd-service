import json

configFile = open("configFiles/config.json")
config = json.load(configFile)

def unloadConfig():
	configFile.close()