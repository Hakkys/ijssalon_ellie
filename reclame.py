from algemene_functies import mijn_functie_2

smaak = "aardbei"
prijs = 4
korting = 0.1

def aanbieding_1():
    global smaak
    global prijs
    global korting
    korting_bedrag = prijs * korting
    prijs_na_korting = prijs - korting_bedrag

    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {prijs_na_korting:.2f} euro."

print(aanbieding_1())


"""
maandag = 220
dinsdag = 430
woensdag = 125
donderdag = 160
vrijdag = 205
zaterdag = 90
zondag = 345
btw9 = 0.09

def inkomsten_totaal():
    global maandag
    global dinsdag
    global woensdag
    global donderdag
    global vrijdag
    global zaterdag
    global zondag
    global btw9
    inkomstenvdweek = maandag + dinsdag + woensdag + donderdag + vrijdag + zaterdag + zondag

    return inkomstenvdweek

totaal_inkomsten = inkomsten_totaal()
btw9_overinkomsten = btw9 * totaal_inkomsten
#print(f"Het totaal van de inkomsten deze week is €{totaal_inkomsten:.2f} euro")
print(f"Het totaal van de inkomsten deze week is €{totaal_inkomsten:.2f} euro, waarover €{btw9_overinkomsten} euro BTW betaald dient te worden") 
"""


def inkomsten_totaal(inkomsten, btw9):
    totaal_inkomsten = sum(inkomsten)
    btw9_bedrag = totaal_inkomsten * btw9
    
    return f"Het totaal van alle inkomsten van deze week is €{totaal_inkomsten:.2f} euro, waarover €{btw9_bedrag:.2f} euro BTW betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btwpercentage9 = 0.09
resultaat = inkomsten_totaal(inkomsten, btwpercentage9)
print(resultaat)


#laag_en_hoog functie
def laag_en_hoog(mijn_lijst):
    laagste_waarde = min(mijn_lijst)
    hoogste_waarde = max(mijn_lijst)

    return [laagste_waarde, hoogste_waarde]

#inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten)
print(f"Laagste waarde: {resultaat[0]}, Hoogste waarde: {resultaat[1]}")

#gemiddelde functie
def gemiddelde(inkomsten):
    totaal_inkomsten = sum(inkomsten)
    aantal_dagen = len(inkomsten)
    gemiddelde_inkomsten = totaal_inkomsten / aantal_dagen

    return f"De gemiddelde inkomsten deze week zijn €{gemiddelde_inkomsten:.2f} euro."

gemiddelde_inkomsten = gemiddelde(inkomsten)
print(gemiddelde_inkomsten)

#functie meervoudig
def meervoudig(mijn_lijst):
    result_meervourdig =  laag_en_hoog(mijn_lijst)
    return result_meervourdig

invoer_lijst = [10,5,3,2,1,2,9] 
resultaat_meervoudig = meervoudig(invoer_lijst)
print(f"Hoogste waarde: {resultaat_meervoudig[1]}, Laagste waarde: {resultaat_meervoudig[0]}")

#functie combinatie
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer_combinatie = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer_combinatie

resultaat_combinatie = combinatie(invoer_lijst)
print(resultaat_combinatie)