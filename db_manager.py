from typing import Dict
import json
import os
import sys


class DBManager:
    def __init__(self) -> None:
        cwd = os.path.dirname(sys.argv[0])
        self.path = os.path.join(cwd, 'xc_data.json')

    def get_all(self) -> Dict:
        return self.__load()

    def get(self, title: str) -> str | None:
        data = self.__load()
        return data.get(title, None)

    def set(self, title: str, text: str):
        data = self.__load()
        data[title] = text
        self.__save(data)

    def remove(self, title: str) -> bool:
        data = self.__load()
        if title not in data:
            return False
        del data[title]
        self.__save(data)
        return True

    def __load(self) -> Dict:
        if not os.path.exists(self.path):
            return {}
        with open(self.path, 'r') as f:
            return json.load(f)

    def __save(self, data: Dict):
        with open(self.path, 'w') as f:
            json.dump(data, f)

