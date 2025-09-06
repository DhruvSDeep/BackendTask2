import requests as r
import csv

mat = []

#Accessing list of types
typeList = r.get("https://pokeapi.co/api/v2/type").json()['results']

simpleTypeList = []
for i in typeList:
    simpleTypeList.append(i['name'])

lis = ['', '']
for i in typeList:
    if (i['name'] != 'stellar' and i['name'] != 'unknown'):
        lis.append(i['name'])
mat.append(lis)
lisEmpty = []
for i in range(len(lis)):
    lisEmpty.append("")
mat.append(lisEmpty)



for i in typeList:

    if (i['name'] != 'stellar' and i['name'] != 'unknown'):          #excluding stellar and unknown
        
        tem = [i['name'], '']
        for k in range(len(simpleTypeList)-2):
            tem.append(1)

        a = r.get(i['url']).json()['damage_relations']      #supereffective
        for j in a['double_damage_from']:
            col = simpleTypeList.index(j['name']) + 2
            tem[col] = 2
        

        for j in a['half_damage_from']:                    #not very effective
            col = simpleTypeList.index(j['name']) + 2
            tem[col] = 0.5

        for j in a['no_damage_from']:                        #immunity
            col = simpleTypeList.index(j['name']) + 2
            tem[col] = 0




        mat.append(tem)
        



    #In the form of a csv for easy visualisation of 2d array as a table
f = open('rep.csv', 'w+')
writer = csv.writer(f)
writer.writerows(mat)
f.close()

