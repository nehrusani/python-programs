#If you have a JSON string, you can parse it by using the json.loads() method.
import json

x = '{"name":"john","age":"39","citya":"dehli"}'
y = json.loads(x)
print(y["age"])