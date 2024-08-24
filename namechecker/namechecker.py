from json import load
from os import getcwd

class Namechecker:
    def __init__(self, name):
        self.name = name

    def printSpecs(self):
        path = f"{getcwd()}/namechecker/public/values.json"
        with open(path) as data:
            values = load(data)
            data.close()
            name = self.name
            for i in name.lower():
                print(values[i], end=' ')
