from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aarbeienijs, emmertje van 5 lieter: 5 euro")
uitvoer.append("Slagraam, spuitbus van 1 liter: 2 euro")

print()
for item in uitvoer:
    print(item)