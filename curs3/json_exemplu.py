import json


# Folosit la deserializare json.loads()

# Folosit la serializare json.dumps()
d = {'hello':'salut'}
print(d)
print(type(d))


serializarea = json.dumps(d)
print(serializarea)
print(type(serializarea))


deserializare = json.loads(serializarea)
print(deserializare)
print(type(deserializare))