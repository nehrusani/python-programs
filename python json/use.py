# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json
x = {"name":"john","age":"39","city":"dehli"}
y = json.dumps(x)
print(y)