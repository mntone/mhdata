import json
from os import mkdir
from common.utils import getAllLocalizations, localizationPath

def convert(oldData):
	newData = dict(
		monsters=[]
	)
	for monsterId, monsterName in oldData['monsters'].items():
		monsterObject = dict(
			id=monsterId,
			name=monsterName,
		)
		newData['monsters'].append(monsterObject)

	return newData

def main():
	mkdir(localizationPath.replace('/localization/', '/localization_new/'))

	for path in getAllLocalizations():
		with open(path, encoding='utf8') as file:
			oldData = json.load(file)
			newData = convert(oldData)

			newPath = path.replace('/localization/', '/localization_new/')
			with open(newPath, 'w', encoding='utf8') as file2:
				json.dump(newData, file2, ensure_ascii=False, indent='\t')

main()
