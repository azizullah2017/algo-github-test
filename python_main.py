import json
import random
from typing import Dict, Text, Any, List, Union


class CollectCommands(object):
    """this class get some data from file and parse them by different function"""
    def __init__(self):
        data = []

    def readFromFile(self):
        """reading data from file"""
        try:
            with open('data.txt', 'r') as file:
                self.data = json.loads(file.read())
        except Exception as e:
            raise e
    
    def parse_commands(self)-> List:
        """get all the command of parse"""
        return [x for x in self.data if x.get('function')=='parse']

    def copy_commands(self) -> List:
        """get all command of copy"""
        return  [x for x in self.data if x.get('function')=='copy']

    def get_functional_commands(self,parse_commands, 
        copy_commands) -> list:
    """get randomly of list"""

        counter = 0
        functional_commands = []
        for row in parse_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'parse'
            new_row['_counter'] = counter
            functional_commands.append(new_row)
        counter = 0
        for row in copy_commands:
            counter += 1
            new_row = row.copy()
            new_row['_list'] = 'copy'
            new_row['_counter'] = counter
            functional_commands.append(new_row)
        
        return functional_commands

    def random_commands(self, random_no)->list:
        return random.sample(self.data, random_no)

obj = CollectCommands()
obj.readFromFile()