# check return type
assert type(obj.copy_commands()) == list 
# check if all the commands are copy
assert obj.copy_commands() == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]