import urllib.request

req = urllib.request.Request('http://datos.gob.gt/api/dataset/38751d6a75e9dce18a84302aaef9631d')
response = urllib.request.urlopen(req)
result = response.read()
print(result)

