import json

x = {
    'hilmar': 0,
    'orri': 1,
    'kuba': 0
}

jsonStr = json.dumps(x, indent=4)

a = json.loads(jsonStr)
print(a['hilmar'])

y = 'asdf'
z = '2'

