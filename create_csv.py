# import csv
import json
import pandas as pd

with open('comments.json') as json_file:
    data = json.load(json_file)
    # print(data)

# with open('comments.csv', 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#
#     for row in data:
#         wr.writerow(row)

df = pd.DataFrame(data, columns=['Автор', 'Текст комментария'])

df.to_excel('comments.xlsx', sheet_name='Комментарии', index=False)
