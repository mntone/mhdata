import json
from common.utils import indexPath, monsterPath
from os import path

def convert(oldData):
	newData = dict(
		id=oldData['id'],
		localization=oldData['localization'],
		monsters=[]
	)
	for monsterId in oldData['monsters']:
		monsterFilepath = path.join(monsterPath, monsterId + '.json')
		with open(monsterFilepath, encoding='utf8') as file:
			monsterObject = dict(
				id=monsterId,
				type=json.load(file)['type']
			)
			newData['monsters'].append(monsterObject)

	return newData

def main():
	with open(indexPath, encoding='utf8') as file:
		oldData = json.load(file)
		newData = convert(oldData)

		newPath = indexPath.replace('/index.json', '/index_new.json')
		with open(newPath, 'w', encoding='utf8') as file2:
			json.dump(newData, file2, ensure_ascii=False, indent='\t')

main()
