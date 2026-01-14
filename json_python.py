import json

json_data = '{"name":"Иван",  "age":30, "student": true}'
parsed_json = json.loads(json_data)

print(parsed_json)