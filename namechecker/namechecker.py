from json import load
from os import getcwd
from namechecker.duplicate import RemoveDuplicate
class Namechecker:
    def __init__(self, name):
        self.name = name

    def printSpecs(self):
        path = f"{getcwd()}/namechecker/public/values.json"
        with open(path) as data:
            values = load(data)
            data.close()
            name = self.name
            name = RemoveDuplicate(name).removeDuplicate()
            print("Your name represents -> ", end=' ')
            for i in name:
                print(values[i], end=' ')
            print('\n')
