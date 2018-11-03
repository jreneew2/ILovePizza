import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Subscription-Key': 'c054021f657b44d592f9987476eb4935',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.wegmans.io')
    conn.request("GET", "/meals/recipes/15484?api-version=2018-10-18&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

recipe = json.loads(data)
ingredients = json.loads(json.dumps(recipe['ingredients']))

print('Recipe: ' + recipe['name'])
print('Ingredients: ')
for ingredient in ingredients:
    print(ingredient['name'] + ' ' + ingredient['price'])