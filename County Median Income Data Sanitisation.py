import csv
countyandwages = {}

countyTax = open("Median Earned Income By County.csv", "r")

csvReader = csv.reader(countyTax)
next(csvReader)
for row in csvReader:
    if not (row[5] == ''):
        if row[1] not in countyandwages:
            countyandwages[row[1]] = [int(row[5])]
        else:
            countyandwages[row[1]].append(int(row[5]))
print(countyandwages)
counties = [
    "Carlow", "Cavan", "Clare", "Cork", "Donegal", "Dublin", "Galway", "Kerry",
    "Kildare", "Kilkenny", "Laois", "Leitrim", "Limerick", "Longford", "Louth",
    "Mayo", "Meath", "Monaghan", "Offaly", "Roscommon", "Sligo", "Tipperary",
    "Waterford", "Westmeath", "Wexford", "Wicklow"
]
#Oscar's code used the traditional counties of Ireland instead of the administrative ones, so I combined them into the traditonal counties
countyandwages["Cork"] = []
countyandwages["Galway"] = []
countyandwages["Dublin"] = []
for county in countyandwages:
    if county not in counties:
        if "Cork" in county:
            countyandwages["Cork"] += countyandwages[county]
        elif "Galway" in county:
            countyandwages["Galway"] += countyandwages[county]
        else:
            countyandwages["Dublin"] += countyandwages[county]
i=0
#This code removes said counties from the list
counties2 = list(countyandwages.keys()) 
for county in counties2:
    if county not in counties:
        countyandwages.pop(county)
    i += 1
for county in countyandwages:
    countyandwages[county] = sum(countyandwages[county])/len(countyandwages[county])
import matplotlib.pyplot as plt
avg_wage = list(countyandwages.values())
#Oscar's code
populations = [
    61968, 81704, 127938, 584156, 167084, 1458154, 277737, 156458, 247774, 104160,
    91877, 35199, 209536, 46751, 139703, 137970, 220826, 65288, 83150, 70259,
    70198, 167895, 127363, 96221, 163919, 155851
]


fig, ax1 = plt.subplots()
plt.xticks(fontsize=6)
color = 'tab:red'
ax1.set_xlabel('Counties', fontsize=12)
ax1.set_ylabel('Population',  fontsize=12, color='blue')
ax1.plot(counties, populations)
ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Median Wage',color='red')
ax2.plot(counties, avg_wage, color='red')
ax2.tick_params(axis='y')

fig.tight_layout()
plt.show()

        
        

