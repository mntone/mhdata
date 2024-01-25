from os import path, walk

titles = ['mhrise', 'mhworld']
indexPath = 'mhrise/index.json'
localizationPath = 'localization/'
monsterBasePath = 'monsters/'

def getAllLocalizations():
	for root, _, files in walk(localizationPath):
		for file in files:
			yield path.join(root, file)

def getAllMonsters(basePath):
	for root, _, files in walk(basePath):
		for file in files:
			yield path.join(root, file)
