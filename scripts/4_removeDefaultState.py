import json
from os import mkdir, path
from common.utils import getAllMonsters, titles, monsterBasePath

def convert(oldData):
	newData = dict(
		id=oldData['id'],
		version=oldData['version'],
		type=oldData['type'],
		physiologies=[]
	)
	for physiology in oldData['physiologies']:
		physiologyObject = dict(
			parts=physiology['parts'],
			values=[],
		)
		for value in physiology['values']:
			valueObject = dict()
			for key, val in value.items():
				if key == 'states':
					if val != ['default']:
						valueObject['states'] = val
				else:
					valueObject[key] = val # Copy other pairs
			physiologyObject['values'].append(valueObject)
		newData['physiologies'].append(physiologyObject)

	return newData

def main():
	for title in titles:
		monstersDir = path.join(title, monsterBasePath)
		mkdir(monstersDir.replace('monsters/', 'monsters_new/'))
		for monsterPath in getAllMonsters(monstersDir):
			with open(monsterPath, encoding='utf8') as file:
				oldData = json.load(file)
				newData = convert(oldData)

				newPath = monsterPath.replace('monsters/', 'monsters_new/')
				with open(newPath, 'w', encoding='utf8', newline='\n') as file2:
					json.dump(newData, file2, ensure_ascii=False, indent='\t')
					file2.write('\n')

main()
