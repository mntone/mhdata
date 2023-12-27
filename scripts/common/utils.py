from os import path, walk

indexPath = 'mhrise/index.json'
localizationPath = 'mhrise/localization/'
monsterPath = 'mhrise/monsters/'

def getAllLocalizations():
	for root, _, files in walk(localizationPath):
		for file in files:
			yield path.join(root, file)

def getAllMonsters():
	for root, _, files in walk(monsterPath):
		for file in files:
			yield path.join(root, file)
