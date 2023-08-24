import json

# Data to be written
dictionary = '[{ "name":"John", "age":30, "city":"New York"}]'

# Serializing json
json_object = json.loads(dictionary)
print(json_object)