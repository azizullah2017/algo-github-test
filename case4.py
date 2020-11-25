# check if two randomize object is selected
assert len(obj.random_commands(2)) == 2
# check return type
assert type(obj.random_commands(2)) == list