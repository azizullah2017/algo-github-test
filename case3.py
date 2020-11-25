# check the return type
assert type(obj.get_functional_commands(obj.parse_commands(), obj.copy_commands()))  == list
# check if all functional commands are there
assert obj.get_functional_commands(obj.parse_commands(), obj.copy_commands()) == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]