import urllib


fo = open('dataSeguridad.json', 'w')
url = 'http://datos.codeandomexico.org/api/action/datastore_search?limit=5&q=title:jones'
fileobj = urllib.urlopen(url)
resp = fileobj.read()
print type(resp)
fo.write(resp)

fo.close()
