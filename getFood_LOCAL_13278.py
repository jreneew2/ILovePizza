import http.client, urllib.request, urllib.parse, urllib.error, base64, json

from itertools import *

headers = {
    # Request headers
    'Subscription-Key': 'c054021f657b44d592f9987476eb4935',
}

params = urllib.parse.urlencode({
})

JSONTODUMP = {}

#GET LIST OF RECIPES
try:
    conn = http.client.HTTPSConnection('api.wegmans.io')
    conn.request("GET", "/meals/recipes/?api-version=2018-10-18&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

recipeList = json.loads(data)
actualRecipeList = recipeList['recipes']
#LOOP THROUGH RECIPES
for recipe in islice(actualRecipeList, 0, 30):
    #GET RECIPE DATA
    try:
        conn = http.client.HTTPSConnection('api.wegmans.io')
        conn.request("GET", "/meals/recipes/" + str(recipe['id']) + "?api-version=2018-10-18&%s" % params, "{body}", headers)
        response = conn.getresponse()
        recipeData = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    recipeJson = json.loads(recipeData)
    ingredients = json.loads(json.dumps(recipeJson['ingredients']))
    #LOOP THROUGH INGREDIENTS
    INGREDIENTSLIST = {}
    for ingredient in ingredients:
        if 'sku' in ingredient:
            sku = str(ingredient['sku'])
            try:
                conn = http.client.HTTPSConnection('api.wegmans.io')
                conn.request("GET", "/products/" + sku + "/prices/1?api-version=2018-10-18&%s" % params, "{body}", headers)
                response = conn.getresponse()
                ingredientData = response.read()
                conn.close()
            except Exception as e:
                print("[Errno {0}] {1}".format(e.errno, e.strerror))
            foodData = json.loads(ingredientData)
            if 'price' in foodData:
                INGREDIENTSLIST[ingredient['name']] = foodData['price']
            else:
                INGREDIENTSLIST[ingredient['name']] = 0
        else:
            INGREDIENTSLIST[ingredient['name']] = 0
    JSONTODUMP[recipeJson['name']] = INGREDIENTSLIST
    print("Added recipe")

with open('data.json', 'w') as outfile:
    json.dump(JSONTODUMP, outfile)