import urllib

url = 'http://www.acme.com/products/3322'
response = urllib.urlopen(url).read()