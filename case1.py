# test if it has all the parse command
assert obj.parse_commands() == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
# check return type
assert type(obj.parse_commands()) == list
# check of it has all copy commnads