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
for county in countyandwages:
    print(county)
    print("The mean wage for", county, "is", round(sum(countyandwages[county])/len(countyandwages[county])))

        
        

