import re
def change(string):
    txt=re.sub(r'(?<!^)(?=[A-Z])', "_", string)
    return re.sub(r'([A-Z])', lambda x: x.group(1).lower(), txt)

string="snakeCaseIsNotBadToo"
print(change(string))