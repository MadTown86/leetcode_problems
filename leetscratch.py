dicter = dict()
import json

dicter['0'] = {"My First Entry": [{'Nested1': "Res1"}, {'Nested2': "Res2"}]}
dicter['2'] = {"My Second Entry": [{'Nested1': "Res1"}, {'Nested2': "Res2"}]}
dicter['1'] = {"My Third Entry": [{'Nested1': "Res1"}, {'Nested2': "Res2"}]}
dicter['-1'] = {"My Fourth Entry": [{'Nested1': "Res1"}, {'Nested2': "Res2"}]}

with open('inputtest.txt', 'w') as f:
    f.truncate()
    json.dump(dicter, f, indent=4, sort_keys=False, separators=(', ', ': '))
