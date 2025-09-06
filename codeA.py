import requests as r
import json 

#accessing given file
f = open("pokemon.txt", "r")
a = f.readlines()
f.close()
dict = {}



#creating dictionary
for i in a:
    vals = (r.get(f"https://pokeapi.co/api/v2/pokemon/{i}").json())

    name = vals['name']
    idee = vals['id']


    #list of abilities
    ability = []
    abilityTemp = vals['abilities']
    for j in abilityTemp:
        ability.append(j['ability']['name'])


    #list of types
    Ptype = []
    PtypeTemp = vals['types']
    for k in PtypeTemp:
        Ptype.append(k['type']['name'])

    isLeg = vals['is_legendary']
    isMyth = vals['is_mythical']
    
    
    dict[name] = {
        "id": idee, "abilities": ability, "types": Ptype, "is_legendary": isLeg, "is_mythical": isMyth}
    
    


oup = open("jason.json", "w+")
json.dump(dict, oup, indent=4)
oup.close()

