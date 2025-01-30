import json

string_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format)

key = "answe"
if key in obj:
    print(obj[key])
else:
    print(f"There is no {key} in obj")