cijfer_1 = 12

def mijn_functie_1(cijfer_1):
    argumentenlijst = [2, 4, 10, 12]

    if cijfer_1 in argumentenlijst:
        return cijfer_1 * cijfer_1
    else:
        return None
    

resultaat_1 = mijn_functie_1(cijfer_1)
if resultaat_1 is not None:
    print(f"Bij het getal {cijfer_1} hoort het bijbehorende getal {resultaat_1}.")
else:
    print(f"Het getal {cijfer_1} komt niet voor in de lijst")




def bereken_functie_2(a,b):
    uitvoerlijstfunctie_2 = []
    uitvoerlijstfunctie_2.append(a + b)
    uitvoerlijstfunctie_2.append(a - b)
    uitvoerlijstfunctie_2.append(a * b)
    uitvoerlijstfunctie_2.append(a / b)

    return uitvoerlijstfunctie_2

print(bereken_functie_2(12, 3))

def mijn_functie_2(cijfer1, cijfer2):
    mapping = {
        (12, 3): [15, 9, 36, 4],
        (12, 2): [14, 10, 24, 6],
        (10, 5): [15, 5, 50, 2],
        (100, 20): [120, 80, 2000, 5]
    }
    key = (cijfer1, cijfer2)
    return mapping.get(key, None)

cijfer_1 = 100
cijfer_2 = 20
output_functie_2 = mijn_functie_2(cijfer_1, cijfer_2)
if output_functie_2:
    print(f"Resultaten voor getal2 {cijfer_1} en {cijfer_2}: {output_functie_2}")
else:
    print(f"Geen resultaten gevonden voor getal2 {cijfer_2}.")