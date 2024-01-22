import json
import re


with open('comments.json') as json_file:
    data = json.load(json_file)

talents_all = []
pattern = re.compile("^\s*[\d\-]\W*([\w\s\d\'\"]+)")

for row in data:
    [comment_author, comment_text] = row

    lines = comment_text.split("\n")

    for i in range(0, len(lines)):
        line = lines[i]

        if "талант" in line.lower():
            j = i + 1
            while j < len(lines) and pattern.match(lines[j]):
                match = pattern.match(lines[j])
                group = match.groups(1)
                # match.regs[1]
                talents_all.append(group[0])
                j += 1
            i = j

json_string = json.dumps(talents_all, ensure_ascii=False)

with open('talents.json', 'w') as outfile:
    outfile.write(json_string)