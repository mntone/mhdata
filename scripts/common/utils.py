from os import path, walk

localizationPath = 'mhrise/localization/'

def getAllLocalizations():
	for root, _, files in walk(localizationPath):
		for file in files:
			yield path.join(root, file)
