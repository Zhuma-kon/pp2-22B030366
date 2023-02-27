import re
def Snaketocamel(s):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)

s="Camels_was_always_better"

print(CamelToSnake(s))
