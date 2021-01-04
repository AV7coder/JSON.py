import json
with open('data.json') as json_file:
    dict_of_json=json.load(json_file)
print(dict_of_json)

# this to read a json file and print it