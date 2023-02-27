import re
reppy=[" ", ",", "."]
text="I go to school. Well, it's done."

for c in reppy:
    text=text.replace(c, ":")
print(text)
