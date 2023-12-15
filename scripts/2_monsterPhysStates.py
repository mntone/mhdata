import json
from os import mkdir
from common.utils import getAllMonsters, monsterPath

def convert(oldData):
	newData = dict(
		id=oldData['id'],
		version=oldData['version'],
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
				if key == 'state':
					if val == 'postbreak':
						valueObject['states'] = ['broken'] # Replace new keyword as Broken
					else:
						valueObject['states'] = [val]
				else:
					valueObject[key] = val # Copy other pairs
			physiologyObject['values'].append(valueObject)
		newData['physiologies'].append(physiologyObject)

	return newData

def main():
	mkdir(monsterPath.replace('/monsters/', '/monsters_new/'))

	for path in getAllMonsters():
		with open(path, encoding='utf8') as file:
			oldData = json.load(file)
			newData = convert(oldData)

			newPath = path.replace('/monsters/', '/monsters_new/')
			with open(newPath, 'w', encoding='utf8', newline='\n') as file2:
				json.dump(newData, file2, ensure_ascii=False, indent='\t')
				file2.write('\n')

main()
