import re
def split(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

string="ThisExampleIsSoBadICan'tStand"
print(split(string))