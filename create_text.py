import json

with open('comments.json') as json_file:
    data = json.load(json_file)

text = ''

for row in data:
    [comment_author, comment_text] = row

    text += comment_text + '\n\n\n'

with open('comments.txt', 'w') as outfile:
    outfile.write(text)